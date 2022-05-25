from project.animals.animal import Mammal

class Mouse(Mammal):
    ALLOWED_FOODS = ['Vegetable', 'Fruit']
    WEIGHT_MULTIPLIER = 0.10
    def __init__(self,name, weight,living_region):
        super().__init__(name, weight,living_region)

    @staticmethod
    def make_sound():
        return "Squeak"


class Dog(Mammal):
    ALLOWED_FOODS = ['Meat']
    WEIGHT_MULTIPLIER = 0.40
    def __init__(self,name, weight,living_region):
        super().__init__(name, weight,living_region)

    @staticmethod
    def make_sound():
        return "Woof!"

class Cat(Mammal):
    ALLOWED_FOODS = ['Vegetable','Meat']
    WEIGHT_MULTIPLIER = 0.30
    def __init__(self,name, weight,living_region):
        super().__init__(name, weight,living_region)

    @staticmethod
    def make_sound():
        return "Meow"

class Tiger (Mammal):
    ALLOWED_FOODS = ['Meat']
    WEIGHT_MULTIPLIER = 1.00
    def __init__(self,name, weight,living_region):
        super().__init__(name, weight,living_region)

    @staticmethod
    def make_sound():
        return "ROAR!!!"

