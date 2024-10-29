class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Dog")

    def speak(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Cat")

    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(f"{animal.name} says {animal.speak()}")

dog1 = Dog("Rex")
cat1 = Cat("Barsik")

animal_sound(dog1)
animal_sound(cat1)