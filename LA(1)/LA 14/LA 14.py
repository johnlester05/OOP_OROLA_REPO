class Spiderman():
    def __init__(self, name, age):
        self.name = name.upper()
        self.age = age
    
    def describeSpiderman(self):
        return f"Spider's man name is {self.name}, age {self.age}, movie title: {self.movieTitle}"

class Tobey(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name,age)
        self.movieTitle = movieTitle.upper()


tobey1 = Tobey("Tobey", 22, "Spiderman1")

class Andrew(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name,age)
        self.movieTitle = movieTitle.upper()

andrew1 = Andrew("Andrew", 23, "Spiderman2")

class Tom(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name,age)
        self.movieTitle = movieTitle.upper()

tom1 = Tom("Tom", 24, "Spiderman3")

print(tobey1.describeSpiderman())

print(tom1.describeSpiderman())

print(andrew1.describeSpiderman())
