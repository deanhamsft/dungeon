import rooms
import items
import weapons
import money
import workbench
import descriptions

# Initialize all the items
small_bowl = items.item('Small bowl', descriptions.small_bowl_description, 1)
large_bowl = items.item('Large bowl', descriptions.large_bowl_description, 2)
medium_bowl = items.item('Medium bowl', descriptions.medium_bowl_description, 1)
slimey_goo = items.item('Slime', descriptions.slimey_goo_description, 0)

small_emerald = items.item('small Emerald', descriptions.small_emerald_description, 10)
large_diamond = items.item('large Diamond', descriptions.large_diamond_description, 25)
pile_of_gold_coins = items.item('Gold coins', descriptions.pile_of_gold_coins_description, 20)

thatched_matt = items.item('A thatched matt', descriptions.thatched_matt_description, 2)
floor_chains = items.item('floor chains', descriptions.floor_chains_description, 1)

wierd_hook = items.item('A strange hook', descriptions.wierd_hook_description, 4)
hanging_chains = items.item('Hanging chains', descriptions.hanging_chains_description, 1)
torch = items.item('a flickering torch', descriptions.torch_description, 1)

# Initialize all the weapons
large_knife = weapons.weapon('A large knife', descriptions.large_knife_description, 2, 4)
small_knife = weapons.weapon('A small knife', descriptions.small_knife_description, 1, 2)
small_hammer = weapons.weapon('A small hammer', descriptions.small_hammer_description, 2, 3)
small_pick = weapons.weapon('A small Pick', descriptions.small_pick_description, 1, 1)

# Initialize all the money
small_box_item_list = [small_emerald, large_diamond, pile_of_gold_coins]
small_box = workbench.workbench('A small box', descriptions.small_box_description, 3, small_box_item_list)

# create the items lists
rustic_bench_items_list = [small_bowl, medium_bowl, small_knife, slimey_goo, small_pick]
metal_bench_items_list = [large_bowl, large_knife, small_hammer, small_box]

# Initialize all the workbenches
rustic_bench = workbench.workbench('Rustic workbench', descriptions.rustic_bench_description, 10, rustic_bench_items_list)
metal_bench = workbench.workbench('Metal workbench', descriptions.metal_bench_description, 20, metal_bench_items_list)
restraining_table = workbench.workbench('Restraining table', descriptions.restraining_table_description, 15, [])

# # Initialize all the rooms
entry_room = rooms.room('Entry', descriptions.entry_description, ['West'], [thatched_matt])
hallway = rooms.room('Hallway', descriptions.hallway_description, ['East','West'], [torch])
chamber = rooms.room('Chamber', descriptions.chamber_description, ['West', 'East', 'South'], [rustic_bench, metal_bench, restraining_table])

# Initialize the dungeon