from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    @staticmethod
    def  make_sound():
        pass


    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"

