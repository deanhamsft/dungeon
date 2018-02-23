import items

class money(items.item):
    def __init__(self, name, description, value, amount):
        self.amount = amount
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nAmount: {}\nValue: {}\n".format(self.name, self.description, self.amount, (self.amount * self.value)) 