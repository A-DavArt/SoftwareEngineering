class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def speak(self):
        return "Some sound"

dog = Animal("Rex", "Dog", 5)
print(f"{dog.name} is a {dog.species}({dog.age} y.o.)")
