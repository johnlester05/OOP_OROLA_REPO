class Animal:
    def __init__(self,name):
        self.name = name
class Dog:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return "Bark!"
class Cat:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return "Meow!"
class Bird:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return "Chirp!"
class Fish:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return "..."

def animal_sounds(Animal):
    print(f"{animal.name} speaks: {animal.speak()}")

dog = Dog("Sheddy")
cat = Cat("Puss")
bird = Bird("Birdy")
fish = Fish("Fishda")

animals = [dog,cat,bird,fish]
for animal in animals:
    animal_sounds(animal)
