from abc import ABC,abstractmethod
class Astronaut(ABC):
    @abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value.count(" ") == len(value):
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def breathe(self):
        self.oxygen -= 10

    def increase_oxygen(self,amount: int):
        self.oxygen += amount
