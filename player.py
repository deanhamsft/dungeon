import items

class player():
    """The base class for all rooms."""
    def __init__(self = '', name = '', description = ''):
        self.name = name
        self.description = description
        self.inventory = []

    def add(self, item):
        self.inventory.append(item)


    def __str__(self):
        if len(self.inventory) == 0:
            return "{}\n======\n{}\n".format(self.name, self.description)
        else:
            returnstr = "{}\n======\n{}\nInventory:\n".format(self.name, self.description)
            for thing in self.inventory:
                returnstr = returnstr + "\t{}\n".format(thing.name)
            return returnstr