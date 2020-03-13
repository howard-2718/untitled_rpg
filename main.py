"""
Main file

- Welcome!
- This is an attempt at creating a command-line RPG.
"""

import os
import art


import inputs
from config import *
from classes.menu import Menu
from classes.entity import Player, Enemy
from classes.map import Map

# Set screen size
os.system('mode con: cols=140 lines=40')

# Draw the title screen
title = art.text2art("Untitled RPG", font='roman', chr_ignore=True)


# Currently, this function's only purpose is to center the title text.
def center_ascii(text, from_center_y):
    lines = []
    line = ""
    for part in text:
        if part == "\n":
            lines.append(line)
            line = ""
        else:
            line += part

    print(t.move_y((t.height // 2) + from_center_y))
    for line in lines:
        print(t.center(line))


center_ascii(title, -10)

cur_menu = Menu(["New Game", "Quit"], 1, ["set_state_map", "exit"])
cur_menu.print_menu()

cur_map = Map(0, 2, 2)

# Create the party
party.append(Player("Constantine", 1, 0, [100, 220],
                    150, 20, 40, 30, 30, 20,
                    10, 0, 10, 10, 9, 10,
                    100, 100, 100, 100, 100, 100, 100, [0]))

party.append(Player("Myosotis", 1, 0, [110, 235],
                    120, 25, 25, 20, 50, 40,
                    8, 0, 7, 7, 12, 10,
                    100, 100, 100, 100, 100, 100, 100, [0]))


with t.hidden_cursor():  # This hides the cursor, which is nice for game play but probably not for debugging
    with t.cbreak():
        val = ''
        while val.lower() != 'q':  # Press q to quit key input
            val = t.inkey()

            if s.get_state() == 'title':
                inputs.menu_key_handler(val, cur_menu)
            elif s.get_state() == 'map':
                inputs.map_key_handler(val, cur_map)
            elif s.get_state() == 'battle':
                pass

            if s.get_state() == 'title':
                inputs.menu_update(cur_menu)
            elif s.get_state() == 'map':
                inputs.map_update(cur_map)
            elif s.get_state() == 'battle':
                pass

        print(f'key input stopped.{t.normal}')

input("press ENTER to quit")

"""
Notes: 

    Element types:
        Earth
        Water
        Fire
        Air
        Dark
        Light
        Null
        
    Attack types:
        Physical
        Magical
        

    Cutscenes:
    - create array "cutscenes"
    - create function play_cutscene which takes an id (array index of cutscenes) and plays it
    - needs a state
    
    pyinstaller --hidden-import=jinxed.terminfo.vtwin10 --onefile main.py when building
    
    - Make a state machine
    - Put party status under map
    - Maybe split the window during combat into map and fight
    - have a menu to the right of the map and use a key to toggle between map movement and menu finagling
"""

"""
    To-do:

    - Figure out how the screen space is going to be divvied up
    - Re-vamp map drawing system
    - Make explored/unexplored tile system
    - Make a better way to quit the game 
    - Create some sort of item system 
    - Create skills system
    - Make lists for enemies and items
    - Encounter chances
    - Maybe add an inner border to the map
"""