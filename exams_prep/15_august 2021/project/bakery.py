from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:

    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    def add_food(self, food_type: str, name: str, price: float):
        if food_type in ["Bread", "Cake"]:
            if any(x.name == name for x in self.food_menu):
                raise Exception(f"{food_type} {name} is already in the menu!")
            food = None
            if food_type == "Bread":
                food = Bread(name, price)
            else:
                food = Cake(name, price)
            self.food_menu.append(food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if drink_type in ["Tea", "Water"]:
            if any(x.name == name for x in self.drinks_menu):
                raise Exception(f"{drink_type} {name} is already in the menu!")
            drink = None
            if drink_type == "Tea":
                drink = Tea(name, portion, brand)
            elif drink_type == "Water":
                drink = Water(name, portion, brand)
            self.drinks_menu.append(drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type in ["InsideTable", "OutsideTable"]:
            if any(x.table_number == table_number for x in self.tables_repository):
                raise Exception(f"Table {table_number} is already in the bakery!")
            table = None
            if table_type == "InsideTable":
                table = InsideTable(table_number, capacity)
            elif table_type == "OutsideTable":
                table = OutsideTable(table_number, capacity)
            self.tables_repository.append(table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self,number_of_people: int):
        table = [x for x in self.tables_repository if not x.is_reserved and x.capacity>=number_of_people]
        if not table:
            return f"No available table for {number_of_people} people"
        curr_table = table[0]
        curr_table.reserve(number_of_people)
        return f"Table {curr_table.table_number} has been reserved for {number_of_people} people"

    def order_food(self,table_number: int,*args):
        table = [x for x in self.tables_repository if x.table_number == table_number]
        if not table:
            return f"Could not find table {table_number}"
        curr_table = table[0]
        has_foods = []
        missing_foods = []

        for food in args:
            if food in [x.name for x in self.food_menu]:
                curr_food = [x for x in self.food_menu if x.name == food][0]
                has_foods.append(curr_food)
                curr_table.order_food(curr_food)
            else:
                missing_foods.append(food)
        res = f"Table {table_number} ordered:\n"
        for food in has_foods:
            res += f"{food}\n"
        res += f"{self.name} does not have in the menu:\n"
        for food in missing_foods:
            res += food+"\n"
        return res.strip()

    def order_drink(self,table_number: int,*args):
        table = [x for x in self.tables_repository if x.table_number == table_number]
        if not table:
            return f"Could not find table {table_number}"
        curr_table = table[0]
        has_drinks = []
        missing_drinks = []

        for drink in args:
            if drink in [x.name for x in self.drinks_menu]:
                curr_drink = [x for x in self.drinks_menu if x.name == drink][0]
                has_drinks.append(curr_drink)
                curr_table.order_drink(curr_drink)
            else:
                missing_drinks.append(drink)
        res = f"Table {table_number} ordered:\n"
        for food in has_drinks:
            res += f"{food}\n"
        res += f"{self.name} does not have in the menu:\n"
        for food in missing_drinks:
            res += food + "\n"
        return res.strip()

    def leave_table(self,table_number: int):
        table = [x for x in self.tables_repository if x.table_number == table_number][0]
        table_bill = table.get_bill()
        self.total_income += table_bill
        table.clear()
        res = f"Table: {table_number}\n"
        res += f"Bill: {table_bill:.2f}"
        return  res

    def get_free_tables_info(self):
        res = ""
        for table in self.tables_repository:
            if not table.is_reserved:
                res += table.free_table_info()+"\n"
        return res.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
