class item():
    """The base class for all rooms."""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n======\n{}\nValue: {}".format(self.name, self.description, self.value)