"""
Global variable declaration file
"""

from blessed import Terminal
from classes.state_machine import StateMachine

global t
t = Terminal()

global s
s = StateMachine()

global party
party = []

global maps
maps = [["111111111111111111111111111111",
         "100000000000000000000000000001",
         "100000000000000000000000000001",
         "100000000000000000000000000001",
         "100000000000000000000000000001",
         "100000000000000000000000000001",
         "100000000000000000000000000001",
         "100000000000000000000000000001",
         "100000000000000000000000000001",
         "100000000000000000000000000001",
         "100000000000000000000000000001",
         "100000000000000000000000000001",
         "100000000000000000000000000001",
         "100000000000000000000000000001",
         "100000000000000000000000000001",
         "100000000000000000000000000001",
         "100000000000000000000000000001",
         "100000000000000000000000000001",
         "100000000000000000000000000001",
         "111111111111111111111111111111"]]

# Global dictionary of all skills
global skills
skills = {
    0: ["Unholy Torrent", "Water", 0, 0, 120, 80, 0, 0, 0, 90, 3, "Summons a torrent of water to cascade upon the foe."]
}

# Global dictionary of all enemies
global enemies
enemies = {
    0: ["Tree Spirit", None, None, None, 100, 10, 30, 25, 20, 15, 0, 10, 6, 5, 4, 4, 0, 0, 0, 0, 0, 0, 0, [], 15]
}
