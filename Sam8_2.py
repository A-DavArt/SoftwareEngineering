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
