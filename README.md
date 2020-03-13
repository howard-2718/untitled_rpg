# untitled_rpg
(currently untitled) CLI RPG, drawing elements from many contemporaries
 
## Documentation
*Note: the documentation may or may not be out of date, and is also pretty barebones.*
\
\
At present, the code is not very complex yet; however, there are still
a lot of elements to go through. 

## Classes
In order to maintain some semblance of organization, below is a list of all
classes present in this project. See their related file for further
information.

##### State Machine
The best class to start off with is probably the **StateMachine** class, 
found in file *state_machine.py*. The purpose of this class is to keep track of
what state the game is currently in, and also store the current relevant
gameplay elements and update them as necessary (for example, the current
menu instance, or the current battle instance).

##### Menu
The **Menu** class, found in file *menu.py*, serves to create and handle numbered
menus, that are controlled via the arrow keys. The current menu item selected
is marked with a > before the number, and is denoted by variable *sel_index*.

##### Entity
The **Entity** class, located in file *entity.py* (wow, what a shocker), serves as
the basis for the **Player** and **Enemy** classes. *The rest to be written at a later 
date...*

##### Map
The **Map** class, located in file *map.py* handles most tasks related to the map 
located at the top left corner of the main gameplay screen.

##### Battle
Occasionally, the player's party will encounter a group of enemies. Of course,
these said enemies have to be defeated in order to progress in the game. Every
battle in this project is represented using the **Battle** class, located in
*battle.py*. 