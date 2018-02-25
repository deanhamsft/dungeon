class room():
    """The base class for all rooms."""
    def __init__(self, name, description, openings, contains):
        self.name = name
        self.description = description
        self.openings = openings
        if len(openings) == 1:
            self.openings_str = '\nThere is an opening on the {} side.\n'.format(self.openings[0])

        if len(openings) > 1:
            i = 0
            for item in openings:
                if i == 0:
                    self.openings_str = '\nThere is an opening on the {}'.format(self.openings[i])
                elif i < len(openings) - 1:
                    self.openings_str = self.openings_str + (', {}'.format(self.openings[i]))
                elif i == len(openings) - 1:
                    self.openings_str = self.openings_str + (' and {} sides.\n'.format(self.openings[i]))
                i += 1

        self.contains = contains
        if len(contains) > 0:
            self.contains_str = 'This room contains: \n'
            for item in contains:
                self.contains_str = self.contains_str + ('\t{}\n'.format(item.name))
        elif len(contains == 0):
            self.contains_str = 'This room is otherwise empty.\n'

    def __str__(self):
        return '{}\n======\n{}\n\n{}\n{}'.format(self.name, self.description, self.openings_str, self.contains_str)
