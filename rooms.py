class room():
    """The base class for all rooms."""
    def __init__(self, name, description, openings):
        self.name = name
        self.description = description
        self.openings = openings

    def __str__(self):
        return '{}\n======\n{}\nThere is an opening on the {} side.\n'.format(self.name, self.description, self.openings)


entry_description = """You look around and see that you are in a dimmly lit room with stone walls.
at first the room appears empty but as your eyes adjust, you spy a fuzzy square outline on the floor 
on the west side. """

hallway_description = """You make your way into the darkened hallway.
The walls are rough stone, as though this is more a tunnel than a hallway.
On the dirt floor ahead of you, a small glint briefly catches your eye"""

chamber_description = """As you enter the chamber you see a large round room.
The walls are smooth stone, with many harnesses and strange metal instruments attached to them.
On the floor staw is spread out in the far quarter. 
Two thick wooden benches are crowded together to your left."""

entry_room = room("Entry", entry_description, "west")
hallway = room("Hallway", hallway_description, "East")
chamber = room("Chamber", chamber_description, "West")
