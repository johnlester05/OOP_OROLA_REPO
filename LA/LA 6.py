class Laptop():
    def __init__(self, brand, model):
        self.brand = brand 
        self.model = model
        
    def laptop_info(self):
        pass
        
lt  = Laptop("Asus", "ROG")
print(lt.laptop_info)
