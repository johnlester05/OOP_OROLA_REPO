class ML():
    def __init__(self, name, role, hero_type):
        self.name = name
        self.role = role
        self.hero_type = hero_type
        
    def describe(self):
        return f'''Hero details:
Name: {self.name}
Role: {self.role}
Type: {self.hero_type}'''
    
hero = ML("Hayabusa", "Assassin", "Burst type Physical")
hero1 = ML("Beatrix", "Marksman", "Reap Type Physical")

print(f'''
Name: {hero.name}
Role: {hero.role}
Type: {hero.hero_type}

{hero.describe()}

Name: {hero1.name}
Role: {hero1.role}
Type:{hero1.hero_type}

{hero1.describe()}
''')
