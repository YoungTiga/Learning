class dictionary_iter:

    def __init__(self,dict):
        self.dict = dict
        self.keys = list(self.dict.keys())
        self.idx = 0
    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.dict):
            raise StopIteration()
        key = self.keys[self.idx]
        value = self.dict[key]
        self.idx += 1
        return (key,value)

result = dictionary_iter(({"name": "Peter", "age": 24}))
for x in result:
    print(x)
