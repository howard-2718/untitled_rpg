"""
Map class file

- (0,0) is always the top-leftmost tile
- tile id 1 (#) denotes un-walkable tile
- tile id 0 (.) denotes walkable tile

- there is a 2d array "maps", in which all maps are stored
- each map is an array

"""

from config import *


class Map:

    def __init__(self, map_id, start_x, start_y):
        self.tile_data = maps[map_id]
        self.pos_x = start_x
        self.pos_y = start_y
        self.prev_x = 0
        self.prev_y = 0
        self.first_print = True

    def print_map(self):
        # If the player attempts to walk into an un-walkable tile, simply set their position to before.
        if self.tile_data[self.pos_y][self.pos_x] == "1":
            self.pos_x = self.prev_x
            self.pos_y = self.prev_y

        if self.first_print:
            print(t.home + t.clear)
            self.first_print = False

            # This bit draws screen dividers
            with t.location():
                for _ in range(40):
                    print(t.move_right(69)+"|")

            x = 0
            for row in self.tile_data:
                y = 0
                row_print = ""
                for tile in row:
                    if x == self.pos_y and y == self.pos_x:
                        row_print += t.green("@ ")
                    else:
                        # 0: Can walk on
                        # 1: Cannot walk on
                        if tile == "0":
                            row_print += t.white(". ")
                        elif tile == "1":
                            row_print += t.white("# ")
                    y += 1
                x += 1
                print(row_print)

            # This bit draws dividers too
            print("—————————————————————————————————————————————————————————————————————")
        else:
            # Set the cursor to the previous player location and print according to its number
            with t.location(self.prev_x * 2, self.prev_y + 1):
                prev_tile = self.tile_data[self.prev_y][self.prev_x]
                if prev_tile == "0":
                    print(t.white(". "))
                elif prev_tile == "1":
                    print(t.white("# "))

            # For every proceeding move, set the cursor to the new player co-ordinates and print the @
            # Ensure that this comes before printing . and #
            with t.location(self.pos_x * 2, self.pos_y + 1):
                print(t.green("@ "))
