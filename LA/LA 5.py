class Char():
    def __init__(self, name, role, heroType):
        self.name = name
        self.role = role
        self.heroType = heroType
        
    def describe(self):
        return f"Character details: {self.name}, {self.role}, {self.heroType}"

hero = Char("Yin", "Fighter", "Physical Burst dmg")
hero1 = Char("Ling", "Assassin", "Physical Burst dmg")

print(f'''
{hero.describe()}
{hero1.describe()}
''')
