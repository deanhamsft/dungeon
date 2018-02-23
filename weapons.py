import items

class weapon(items.item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nDamage: {}\nValue: {}\n".format(self.name, self.description, self.damage, self.value) 