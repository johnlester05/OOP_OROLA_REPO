from abc import ABC, abstractmethod

class NinjaTurle(ABC):
    @property
    def alias(self):
        pass

class Leonardo(NinjaTurle):
    def __init__(self):
        self.__alias = "leo"
   
    @property
    def alias(self):
        return self.__alias

class Michelangelo(NinjaTurle):
    def __init__(self):
        self.__alias = "angelo"
   
    @property
    def alias(self):
        return self.__alias

class Donatello(NinjaTurle):
    def __init__(self):
        self.__alias = "brainy"
   
    @property
    def alias(self):
        return self.__alias


class Raphael(NinjaTurle):
    def __init__(self):
        self.__alias = "Raph"
   
    @property
    def alias(self):
        return self.__alias


if __name__ == "__main__":
    pong = Raphael() 
    print(pong.alias)  
    print("FOR TESTING ONLY Purposes")

#OOP1.py
import structure 

pong = structure.Raphael()
print(pong.alias)