class room():
    """The base class for all rooms."""
    def __init__(self, name, description, openings, contains):
        self.name = name
        self.description = description
        self.openings = openings
        self.contains = contains

    def __str__(self):
        return '{}\n======\n{}\n\nThere is an opening on the {} side.\n'.format(self.name, self.description, self.openings)
