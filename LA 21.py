class ScrambleEgg:
    def __init__(self, main_ingredient, onion, beated_eggs):
        self.main_ingredient = main_ingredient  # public
        self._onion = onion  # protected
        self.__beated_eggs = beated_eggs  # private
       
    def get_beated_eggs(self, times):  
        if times >= 14:
            return self.__beated_eggs  
        else:
            return "More!"
    
    def set_beated_eggs(self, new_beated_eggs):
        self.__beated_eggs = new_beated_eggs  # Setter method to update the private attribute
   
    def __str__(self):
        return f"Ingredient list of Scramble Egg is {self.main_ingredient}, {self.get_beated_eggs(14)}, {self._onion}"

scramble_eggs = ScrambleEgg("Eggs", "onions", "beated Eggs")
print(scramble_eggs.get_beated_eggs(1))  # Output: Secret!


scramble_eggs.set_beated_eggs("new beated eggs")
print(scramble_eggs.get_beated_eggs(14))  # Output: new beated eggs
print(scramble_eggs)  # Output: Ingredient list of Scramble Egg is Eggs, new beated eggs, onions