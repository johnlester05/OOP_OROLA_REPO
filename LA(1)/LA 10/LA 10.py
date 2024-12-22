class Vehicle():
    def __init__(self, brand, model, fuel):
        self.brand = brand
        self.model = model
        self.fuel = fuel
        
    def describe_Vehicle(self):
        return f"{self.brand}: a {self.model} that uses {self.fuel}"
        
class car(Vehicle):
    pass

audi = car("audi", "2011 model", "Gasoline")


class motorcycle(Vehicle):
    pass
mio = motorcycle("mio", "v2 model", "Diesel")
print(audi.describe_Vehicle())
print(mio.describe_Vehicle())
