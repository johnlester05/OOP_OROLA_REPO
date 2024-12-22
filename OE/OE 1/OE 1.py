class hero ():
    def __init__ (self, name, role, dmg_type):
        self.name = name
        self.role = role
        self.dmg_type = dmg_type
     
    def describe(self):
        return f"hero name: {self.name}, role: {self.role}, attribute: {self.dmg_type}."
        
      
hero_mm = hero("ixia", "marksman", "physical attack")
hero_fighter = hero("arlott", "fighter", "physical attack")
hero_assassin = hero("julian", "assassin/fighter", "magic attack")
hero_mage = hero("zhuxin", "mage", "magic attack")
hero_tank = hero("atlas", "tank", "magic attack")

print(hero_mm.name)
print(hero_mm.role)
print(hero_mm.dmg_type)
print(hero_mm.describe())
print("\n")
print(hero_fighter.name)
print(hero_fighter.role)
print(hero_fighter.dmg_type)
print(hero_fighter.describe())
print("\n")
print(hero_assassin.name)
print(hero_assassin.role)
print(hero_assassin.dmg_type)
print(hero_assassin.describe())
print("\n")
print(hero_mage.name)
print(hero_mage.role)
print(hero_mage.dmg_type)
print(hero_mage.describe())
print("\n")
print(hero_tank.name)
print(hero_tank.role)
print(hero_tank.dmg_type)
print(hero_tank.describe())
