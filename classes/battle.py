from config import t, s, party
from classes.entity import Enemy, Player
from classes.menu import Menu


class Battle:

    def __init__(self, enemies):
        self.party = party  # Could also just modify party itself, maybe
        self.enemies = enemies  # Should be array of Enemy objects

        self.y = 1

        # The battle area of the screen should have scrolling text as it gets filled up
        # No idea how to implement that

        s.set_state('battle')
        print(t.move_xy(71, self.y) + "A battle has begun!")

        # The battle loop
        while self.enemies:

            for player in self.party:
                self.print_battle_status()

                self.y += 2
                print(t.movexy(71, self.y) + "What will " + player.name + " do?")

                decision_menu = Menu(["Blah 1", "Blah 2"], 1, [])

                x = input()  # Temporary line to stop the while loop from going nuts

    def print_battle_status(self):
        self.y += 2
        for enemy in self.enemies:
            print(t.move_xy(71, self.y) + enemy.display_stats_battle())
            self.y += 1

        self.y += 1

        for player in party:
            print(t.move_xy(71, self.y) + player.display_stats_battle())
            self.y += 1

        self.y += 1

        print(t.move_xy(71, self.y) + "########################################")
