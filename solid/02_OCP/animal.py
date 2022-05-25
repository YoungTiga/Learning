from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self):
        self.species = self.__class__.__name__

    @abstractmethod
    def get_species(self):
        return self.species

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def __init__(self):
        super().__init__()

    def get_species(self):
        return self.species

    def make_sound(self):
        return "Meow"


class Dog(Animal):

    def __init__(self):
        super().__init__()

    def get_species(self):
        return self.species


    def make_sound(self):
        return "Woof!"


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog()]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
