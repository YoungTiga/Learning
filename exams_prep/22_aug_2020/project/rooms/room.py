class Room:

    def __init__(self,name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.appliances = []
        self.expenses = 0
        self.room_cost = 0



    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self,*args):
        for list_items in args:
            for item in list_items:
                self.expenses += item.get_monthly_expense()


    def total_cost(self):
        return self.room_cost+self.expenses

    def __str__(self):
        res = ""
        res += f"{self.family_name} with {self.members_count} members. " \
               f"Budget: {self.budget:.2f}$, " \
               f"Expenses: {self.expenses:.2f}$\n"

        for number,child in enumerate(self.children):
            res += f"--- Child {number+1} " \
                   f"monthly cost: {child.get_monthly_expense():.2f}$\n"
        res += f"--- Appliances monthly cost: " \
               f"{sum(x.get_monthly_expense() for x in self.appliances):.2f}$\n"
        return res