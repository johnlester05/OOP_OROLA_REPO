class Favorite_food:
    def __init__(self, egg, cooking_oil, onion, tomato):
        self.__egg= egg
        self.__cooking_oil = cooking_oil
        self.__onion = onion
        self.__tomato = tomato
       
       
    def __str__(self):
        return f'''Here are the list ingredients of my favorite food(Omelette):\n{self.__egg}eggs\n{self.__cooking_oil}L cooking oil\n{self.__onion} onion\n{self.__tomato} tomato'''
       
omelette = Favorite_food(2,1,1,1)
print(omelette)
