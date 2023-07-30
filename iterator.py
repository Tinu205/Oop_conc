#iterator and generators
#iterators allows us to iterate over sequence of data efficiently itears ave two implements
#__iter__() and __next__()
#__iter__() returns the iter object itself
#__next__() return next element and raise stopiterations exception when eol is achived
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

# Using the iterator
numbers = [1, 2, 3, 4, 5]
my_iterator = MyIterator(numbers)

# for num in my_iterator:
#     print(num)
