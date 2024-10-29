class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.__age = age

    def speak(self):
        return "Some sound"

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age

rabbit = Animal("Bunny", "Rabbit", 2)
print(f"{rabbit.name} is {rabbit.get_age()} years old.")
rabbit.set_age(3)
print(f"{rabbit.name} is now {rabbit.get_age()} years old.")