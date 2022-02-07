class dog():

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_tricks(self, trick):
        self.tricks.append(trick)


d = dog('fido')
e = dog('buddy')
d.add_tricks('roll over')
e.add_tricks('play dead')
print(d.tricks, d.name)
print(e.tricks, e.name)
