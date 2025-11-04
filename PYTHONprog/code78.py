# Single Inheritence
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species = "Dog")
        self.breed = breed
    
    def make_sound(self):
        print("Bark!")

a = Dog("Bruno", "Germen Shepherd")
a.make_sound()

b = Animal("Sunny", "Dog")
b.make_sound()