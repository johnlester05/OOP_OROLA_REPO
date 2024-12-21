class Char():
    def __init__(self, name, role):
        self.name = name
        self.role = role
        
    def describe(self):
        return f"Name: {self.name} and his/her role is {self.role}"
        
    def __str__(self):
        return f"Hello! my name is {self.name}"


hero = Char("Yin", "Fighter")
hero1 = Char("Ling", "Assassin")

print(hero.name)
print(hero.role)
print(hero.describe())
print("\n")
print(hero1.name)
print(hero1.role)
print(hero1.describe())
print("\n")
print(hero)