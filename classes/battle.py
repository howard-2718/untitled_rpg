from config import t, s, party, battle_text
from classes.entity import Enemy, Player
from classes.menu import Menu


def print_battle_text():
    for index in range(0, len(battle_text)):
        if battle_text[index] is not "":
            print(t.move_xy(71, index + 1) + battle_text[index])


class Battle:

    def __init__(self, enemies):
        self.party = party  # Could also just modify party itself, maybe
        self.enemies = enemies  # Should be array of Enemy objects

        self.y = 0

        # The battle area of the screen should have scrolling text as it gets filled up
        # No idea how to implement that

        s.set_state('battle')
        battle_text[self.y] = "A battle has begun!"

        # The battle loop
        self.print_battle_status()

        self.y += 2
        battle_text[self.y] = "What will " + self.party[0].name + " do?"

        self.y += 1

        s.cur_menu = Menu(["Blah 1", "Blah 2"], 1, [])
        menu_text = s.cur_menu.battle_menu()
        for line in menu_text:
            self.y += 1
            battle_text[self.y] = line

    def update_menu(self):
        self.y -= 2  # Make this not just 2
        menu_text = s.cur_menu.battle_menu()
        for line in menu_text:
            self.y += 1
            battle_text[self.y] = line + "                  "  # This blank space prevents some odd behavior

    def print_battle_status(self):
        self.y += 2
        for enemy in self.enemies:
            battle_text[self.y] = enemy.display_stats_battle()
            self.y += 1

        self.y += 1

        for player in party:
            battle_text[self.y] = player.display_stats_battle()
            self.y += 1

        self.y += 1

        battle_text[self.y] = "########################################"

