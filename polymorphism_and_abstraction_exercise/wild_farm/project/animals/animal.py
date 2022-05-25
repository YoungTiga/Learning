from abc import ABC,abstractmethod

from project.food import Food


class Animal(ABC):
    ALLOWED_FOODS =[]
    WEIGHT_MULTIPLIER = 1
    @abstractmethod
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    def feed(self,food:Food):
        if food.__class__.__name__ not in self.ALLOWED_FOODS:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity*self.WEIGHT_MULTIPLIER
        self.food_eaten += food.quantity
    @staticmethod
    def make_sound():
        pass
class Bird(Animal,ABC):
    @abstractmethod
    def __init__(self, name, weight,wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"
class Mammal(Animal, ABC):
    @abstractmethod
    def __init__(self, name, weight,living_region ):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"