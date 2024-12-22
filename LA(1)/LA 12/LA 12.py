class Toy():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"Item: {self.name}, {self.price}, available in {self.shop}"
        
class Car(Toy):
    def __init__(self, name, price, shop):
        super().__init__(name, price)
        self.shop = shop
        
tcar = Car("Hotwheels", 285, "toy kingdom")
print(tcar)
