class workbench():
    def __init__(self, name, description, value, contains):
        self.name = name
        self.description = description
        self.value = value
        self.contains = contains
        self.contains_str = "This bench contains: \n"
        for item in contains:
            self.contains_str = self.contains_str + ("\t{}\n".format(item.name))
    
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n{}".format(self.name, self.description, self.value, self.contains_str) 