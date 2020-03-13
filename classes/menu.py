"""
Menu handling file

- Every menu is of the Menu class
- Menus are initialized with an array of options

- What a menu option does is determined by the following table:
- "set_state_map": s.set_state('map')
- "exit": exit()

"""

from config import *
import sys


class Menu:

    def __init__(self, options, sel_index, results):
        self.options = options  # Array of strings
        self.results = results  # Array of strings
        self._sel_index = sel_index
        self.first_print = True

    @property
    def sel_index(self):
        return self._sel_index

    @sel_index.setter
    def sel_index(self, value):
        length = len(self.options)
        if value > length:
            self._sel_index = 1
        elif value < 1:
            self._sel_index = length
        else:
            self._sel_index = value

    @sel_index.deleter
    def sel_index(self):
        del self._sel_index

    def print_menu_center(self):
        if not self.first_print:
            print(t.move_up(len(self.options) + 1))
            for _ in range(len(self.options) + 1):
                print(t.clear_eol)
            print(t.move_up(len(self.options) + 2))

        count = 1
        for option in self.options:
            if self.sel_index == count:
                print(t.center("> " + str(count) + ". " + option))
            else:
                print(t.center(str(count) + ". " + option))
            count += 1
        self.first_print = False

    # Prints a menu at cursor where x and y is the top left of the menu
    # Specifically meant for use in the 'battle' state
    def battle_menu(self):
        output = []

        count = 1
        for option in self.options:
            if self.sel_index == count:
                output.append("> " + str(count) + ". " + option)
            else:
                output.append(str(count) + ". " + option)
            count += 1

        return output

    def decision(self):
        choice = self.results[(self.sel_index-1)]

        if choice == "set_state_map":
            s.set_state('map')
        elif choice == "exit":
            sys.exit()
