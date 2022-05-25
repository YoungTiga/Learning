from project.fish.base_fish import BaseFish

class SaltwaterFish(BaseFish):
    ADDING_SIZE = 2
    def __init__(self, name: str, species: str, price: float):
        super().__init__(name,species,5,price)

    def eat(self):
        self.size +=self.ADDING_SIZE