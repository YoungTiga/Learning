class sequence_repeat:
    def __init__(self,sequence,number):
        self.sequence = sequence
        self.number = number
        self.start = 0
    def __iter__(self):
        return  self

    def __next__(self):
        if self.number>=1:
            if self.start >= len(self.sequence):
                self.start = 0
            current = self.sequence[self.start]
            self.start += 1
            self.number -= 1
            return current
        else:
            raise StopIteration()

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
