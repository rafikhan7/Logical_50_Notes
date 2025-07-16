# create a custom iterator class
class CustomIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            item = self.data[self.index]
            self.index += 1
            return item
        raise StopIteration

obj = CustomIterator([1, 2, 3, 4, 5])
for item in obj:
    print(item)