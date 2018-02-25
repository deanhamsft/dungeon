import items

class workbench(items.item):
    def __init__(self, name, description, value, contains):
        self.contains = contains
        self.contains_str = "This bench contains: \n"
        for item in contains:
            self.contains_str = self.contains_str + ("\t{}\n".format(item.name))
        super().__init__(name, description, value)
    
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n{}".format(self.name, self.description, self.value, self.contains_str) 