"""
Input handling file
"""

from config import *
from classes.entity import Enemy
from classes.battle import Battle, print_battle_text


def menu_key_handler(key, menu):

    if key == '\x1b[B' or key == 's':
        menu.__setattr__('sel_index', menu.__getattribute__('sel_index') + 1)
    elif key == '\x1b[A' or key == 'w':
        menu.__setattr__('sel_index', menu.__getattribute__('sel_index') - 1)
    elif key == '\x1b[D' or key == 'a':
        menu.__setattr__('sel_index', menu.__getattribute__('sel_index') - 1)
    elif key == '\x1b[C' or key == 'd':
        menu.__setattr__('sel_index', menu.__getattribute__('sel_index') + 1)
    elif key == 'z':
        menu.decision()


def map_key_handler(key, map_):

    map_.__setattr__('prev_x', map_.__getattribute__('pos_x'))
    map_.__setattr__('prev_y', map_.__getattribute__('pos_y'))

    if key == '\x1b[B' or key == 's':
        map_.__setattr__('pos_y', map_.__getattribute__('pos_y') + 1)
    elif key == '\x1b[A' or key == 'w':
        map_.__setattr__('pos_y', map_.__getattribute__('pos_y') - 1)
    elif key == '\x1b[D' or key == 'a':
        map_.__setattr__('pos_x', map_.__getattribute__('pos_x') - 1)
    elif key == '\x1b[C' or key == 'd':
        map_.__setattr__('pos_x', map_.__getattribute__('pos_x') + 1)


def menu_update(menu):
    menu.print_menu_center()


def map_update(map_):
    map_.print_map()

    # Comment out the rest of the function to toggle between testing the map and testing battles
    with t.location():  # TODO: make HP and MP align
        for obj in party:
            print(obj.name + " ------- HP: " + str(obj.cur_hp) + "/" + str(obj.hp) +
                  "  MP: " + str(obj.cur_mp) + "/" + str(obj.mp))

    # TODO: encounter chances
    # Create battle here
    cur_enemies = [create_enemy(0, 1, 10), create_enemy(0, 1, 10)]
    s.cur_battle = Battle(cur_enemies)


def battle_update(battle):
    battle.update_menu()
    print_battle_text()


def create_enemy(enemy_id, lvl, xp):
    test_enemy = Enemy(*enemies[enemy_id])  # The asterisk unpacks the array to use as arguments
    test_enemy.lvl = lvl
    test_enemy.xp = xp
    return test_enemy
