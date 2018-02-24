import os
import initialize_dungeon

def entry_room():
    print(initialize_dungeon.entry_room)

def hallway():
    print(initialize_dungeon.hallway)

def chamber():
    print(initialize_dungeon.chamber)

playing = True
current_room = 'entry'
entry_room()

while playing:
    direction = input('What would you like to do: \n')

    if (direction.lower() == 'west' and current_room == 'entry'):
        os.system('cls')
        current_room = 'hallway'
        hallway()
    if (direction.lower() == 'east' and current_room == 'hallway'):
        os.system('cls')
        current_room = 'chamber'
        chamber()
    if (direction.lower() == 'west' and current_room == 'chamber'):
        os.system('cls')
        current_room = 'hallway'
        hallway()