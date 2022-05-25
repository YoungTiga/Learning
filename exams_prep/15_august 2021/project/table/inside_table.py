from project.table.table import Table

class InsideTable(Table):
    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number,capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if value < self.min_number or value>self.max_number:
            raise ValueError("Inside table's number must be between 1 and 50 inclusive!")
        self.__table_number = value

    @property
    def min_number(self):
        return 1


    @property
    def max_number(self):
        return 50