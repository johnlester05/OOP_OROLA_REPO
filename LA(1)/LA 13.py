class Animal():
    def __init__(self, name, fish_type):
        self.name = name
        self.fish_type = fish_type
    def describeAnimal(self):
        print(f"{self.name} {self.fish_type}")

class Fish(Animal):
    def __init__(self, name, fish_type, can_swim):
        super().__init__(name, fish_type)
        self.can_swim = True

fish1 = Fish("pipoy", "galunggong", True or False)

print(fish1.can_swim)
