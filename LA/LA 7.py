class Car():
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
     
    def describe(self):
        pass
        
car = Car("Audi", "white")
car2 = Car("toyota", "black")
print(car.brand)
print(car.color)
car.color = "red"
print(car.color)
print(car2.color)
