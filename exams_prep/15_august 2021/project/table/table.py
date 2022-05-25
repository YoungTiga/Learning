from abc import ABC,abstractmethod

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):

    @abstractmethod
    def __init__(self,table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False




    @property
    @abstractmethod
    def min_number(self):
        pass


    @property
    @abstractmethod
    def max_number(self):
        pass

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self.__capacity = value

    def reserve(self,number_of_people: int):
        self.is_reserved = True
        self.number_of_people = number_of_people

    def order_food(self,baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self,drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        return sum(x.price for x in self.food_orders) + sum(x.price for x in self.drink_orders)

    def clear(self):
        self.is_reserved = False
        self.drink_orders = []
        self.food_orders = []
        self.number_of_people = 0

    def free_table_info(self):
        if not self.is_reserved:
            res= f"Table: {self.table_number}\n"
            res+=f"Type: {self.__class__.__name__}\n"
            res +=f"Capacity: {self.capacity}\n"
            return res.strip()
        return None
