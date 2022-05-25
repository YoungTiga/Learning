class take_skip:

    def __init__(self,step,count):
        self.step = step
        self.count = count
        self.i = 0
        self.start = 1
    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.count:
            current = self.i
            self.i += self.step
            self.start += 1
            return current
        else:
            raise  StopIteration()


numbers = take_skip(10, 5)
for number in numbers:
    print(number)
