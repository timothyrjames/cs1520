class Pet(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + ' is ' + str(self.age)

    def get_name(self):
        return self.name


pets = [
    Pet('Fido', 4),
    Pet('Spot', 7),
    Pet('Bubbles', 1),
]

print(pets[0])
