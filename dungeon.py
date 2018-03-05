import os, sys
import initialize_dungeon, items, player
import help_strings

def inspect_item(room_name, instructions):
    room_of_interest = getattr(initialize_dungeon, room_name)
    room = room_of_interest
    for item in instructions:
        for things in room.contains:
            if things.name.lower().find(item) != -1:
                current_workbench = things
                print(things)
                if hasattr(current_workbench, 'contains'):
                    print(current_workbench)
                    for widgets in current_workbench.contains:
                        if widgets.name.lower().find(item) != -1:
                            print(widgets)


    

def parse_instructions(instruction):
    instructions = instruction.split()
    return instructions

name = input('Tell me your name adventurer : ')

playing = True
player = player.player(name)
os.system('cls')
current_room = 'entry_room'
current_workbench = items.item()
print(initialize_dungeon.entry_room)

while playing:
    instruction = input('What would you like to do: \n').lower()
    if instruction == '':
        os.system('cls')
        print(help_strings.help_look)
    else:
        instructions = parse_instructions(instruction)

        if (instructions[0] == 'go' or instructions[0] == 'walk' or instructions[0] == 'move'):
            if (instructions[1] == 'west' and current_room == 'entry_room'):
                os.system('cls')
                current_room = 'hallway'
                print(initialize_dungeon.hallway)
            elif (instructions[1] == 'west' and current_room == 'hallway'):
                os.system('cls')
                current_room = 'chamber'
                print(initialize_dungeon.chamber)
            elif (instructions[1] == 'east' and current_room == 'chamber'):
                os.system('cls')
                current_room = 'hallway'
                print(initialize_dungeon.hallway)
            elif (instructions[1] == 'east' and current_room == 'hallway'):
                os.system('cls')
                current_room = 'entry_room'
                print(initialize_dungeon.entry_room)
        elif instructions[0] == 'look' and len(instructions) == 1:
            room_of_interest = getattr(initialize_dungeon, current_room)
            os.system('cls')
            room = room_of_interest
            print(room)
        elif (instructions[0] == 'look' or instructions[0] == 'inspect' or instructions[0] == 'examine'):
            if instructions[1] == 'self':
                os.system('cls')
                print(player)
            else:
                os.system('cls')
                inspect_item(current_room, instructions)
        elif (instructions[0] == 'take'):
            room_of_interest = getattr(initialize_dungeon, current_room)
            room = room_of_interest
            for thing in room.contains:
                if thing.name.find(instructions[1]) != -1:
                    player.add(thing)
        elif instructions[0] == 'quit' or instructions[0] == 'exit':
            sys.exit(0)
        elif instructions[0] == 'help':
            os.system('cls')
            print(help_strings.help_look)
