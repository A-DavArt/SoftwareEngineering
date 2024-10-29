class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.hungry = True

    def speak(self):
        return "Some sound"

    def eat(self):
        if self.hungry:
            print(f"{self.name} is eating.")
            self.hungry = False
        else:
            print(f"{self.name} is not hungry.")

cat = Animal("Barsik", "Cat", 3)
cat.eat()
cat.eat()

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, "Dog", age)

    def speak(self):
        return "Woof!"

bulldog = Dog("Rex", 4)
print(f"{bulldog.name}({bulldog.age}) says {bulldog.speak()}")