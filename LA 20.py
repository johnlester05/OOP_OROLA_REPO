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
   
    def __str__(self):
        return f"Ingredient list of Scramble Egg is {self.main_ingredient}, {self.get_beated_eggs()}, {self._onion}"

scramble_eggs = ScrambleEgg("Eggs", "onions", "beated Eggs")
print(scramble_eggs.get_beated_eggs(1))