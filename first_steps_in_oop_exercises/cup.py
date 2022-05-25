class Cup:
    def __init__(self,size,quantity):
        self.size = size
        self.quantity = quantity



    def status(self):
        return  self.size - self.quantity

    def fill(self, quan):
        if self.quantity + quan <= self.size:
            self.quantity += quan


# cup = Cup(10, 5)
# # print(cup.status())
# cup.fill(3)
# # cup.fill(20)
# print(cup.status())
cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
