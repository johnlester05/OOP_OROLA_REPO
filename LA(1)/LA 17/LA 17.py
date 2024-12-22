class Appliances:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def operate(self):
        print(f"{self.brand} Operating!")

    def info(self):
        print(f"{self.brand} model is {self.model}")

class WashingMachine(Appliances):
    def operate(self):
        print(f"{self.brand}: Washing clothes!")

class Refrigerator(Appliances):
    def operate(self):
        print(f"{self.brand} {self.model}: Keeping food cold!")

class Microwave(Appliances):
    def operate(self):
        print(f"{self.brand} {self.model}: Heating food!")


tcl = WashingMachine("TCL", "TWA 95")
samsung = Refrigerator("Samsung", "RS64")
whirpool = Microwave("Whirpool", "MWX 203")

for appl in [tcl, samsung, whirpool]:
    appl.operate()
    appl.info()
