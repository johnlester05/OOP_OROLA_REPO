class Phone():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def describePhone(self):
        return "My phone: "
        
class Android(Phone):
    def __init__(self, brand, model, price):
        super().__init__(brand, model)
        self.price = price
        
    def describe_phone(self):
        return f"Brand: {self.brand} {self.model} worth {self.price}"
 
cp1 = Android("Vivo", "V25 5G", "₱24,000")

class Les(Phone):
    def __init__(self, brand, model, price):
        super().__init__(brand, model)
        self.price = price
    def describe_phone(self):
        return f"Brand: {self.brand} {self.model} worth {self.price}"
 
cp2 = Les("Vivo", "S10e", "₱17,000")

class Ter(Phone):
    def __init__(self, brand, model, price):
        super().__init__(brand, model)
        self.price = price
    def describe_phone(self):
        return f"Brand: {self.brand} {self.model} worth {self.price}"
 
cp3 = Ter("Infinix", "Note10", "₱15,000")

print(f'''
{cp1.describe_phone()}
{cp2.describe_phone()}
{cp3.describe_phone()}
''')
