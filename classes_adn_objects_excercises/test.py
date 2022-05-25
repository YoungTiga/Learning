class Test:
    def __init__(self,name,age):
        self.name = name
        self.age = age


class InheritTest(Test):
    def __init__(self, NAME,AGE):
        super().__init__(NAME,AGE)




testt = InheritTest("sad",13)

print(testt.name,testt.age)