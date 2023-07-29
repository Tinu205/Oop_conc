#Generator use yeild keyword to return value
class count:
    def __init__(self,data) -> None:
        self.data = data
        self.count  = 0
    def coutn(self):
        for item in self.data:
            yield item

value = count([1,2,3,4,5,6,7])

for item in value.coutn():
    print(item)