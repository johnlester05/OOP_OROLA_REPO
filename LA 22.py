class BirthdayParty:
    def __init__(self, name, party_theme, list_of_foods):
        self.name = name
        self.party_theme = party_theme
        self.list_of_foods = list_of_foods

    def print_foods(self):
        print(f"Party Theme: {self.party_theme}")
        print("List of Foods:")
        for food in self.list_of_foods:
            print(f"- {food}")
        print("Special Dish:")
        self.__secret_dish()  

    def __secret_dish(self):
        print(f"Krabby {self.name}")


party1 = BirthdayParty("Alice", "Princess", ["Cake", "Spaghetti", "BBQ Chicken", "Halo Halo"])
party2 = BirthdayParty("Bob", "Superhero", ["Pizza", "Hot Dogs", "Chips", "Fruit Salad"])
party3 = BirthdayParty("Patty", "Pirate", ["Fish and Chips", "Cupcakes", "Pasta", "Brownies"])

print("Party 1 Foods:")
party1.print_foods()
print("\nParty 2 Foods:")
party2.print_foods()
print("\nParty 3 Foods:")
party3.print_foods()