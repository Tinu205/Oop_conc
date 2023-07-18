class Person:
    def __init__(self,name) -> None:
        self.name = name
    def greet(self):
        return f"Hello Mr.{self.name}"
jeff = Person("Zakku")
print(jeff.greet())
