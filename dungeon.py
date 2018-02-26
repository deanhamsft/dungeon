import os
import initialize_dungeon

def inspect_item(room_name, instructions):
    room_of_interest = getattr(initialize_dungeon, room_name)
    room = room_of_interest
    for item in instructions:
        for things in room.contains:
            if things.name.find(item) != -1:
                print(things)
    

def parse_instructions(instruction):
    instructions = instruction.split()
    return instructions

playing = True
os.system('cls')
current_room = 'entry_room'
print(initialize_dungeon.entry_room)

while playing:
    instruction = input('What would you like to do: \n').lower()
    instructions = parse_instructions(instruction)

    if (instructions[0] == 'go' or instructions[0] == 'walk' or instructions[0] == 'move'):
        if (instructions[1] == 'west' and current_room == 'entry_room'):
            os.system('cls')
            current_room = 'hallway'
            print(initialize_dungeon.hallway)
        if (instructions[1] == 'west' and current_room == 'hallway'):
            os.system('cls')
            current_room = 'chamber'
            print(initialize_dungeon.chamber)
        if (instructions[1] == 'east' and current_room == 'chamber'):
            os.system('cls')
            current_room = 'hallway'
            print(initialize_dungeon.hallway)
        if (instructions[1] == 'east' and current_room == 'hallway'):
            os.system('cls')
            current_room = 'entry_room'
            print(initialize_dungeon.entry_room)
    elif instructions[0] == 'look' and len(instructions) == 1:
        room_of_interest = getattr(initialize_dungeon, current_room)
        os.system('cls')
        room = room_of_interest
        print(room)
    elif (instructions[0] == 'look' or instructions[0] == 'inspect' or instructions[0] == 'examine'):
        os.system('cls')
        inspect_item(current_room, instructions)
