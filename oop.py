class Person:
    def __init__(self,name) -> None:
        self.name = name
    def greet(self):
        return f"Hello Mr.{self.name}"
jeff = Person("Zakku")
# print(jeff.greet())

class pet:
    #tricks = []# dont use this since this is shared by all instances 
    type = "dog" #class variable shared by all instances
    def __init__(self,name) -> None:
        self.name = name
        self.tricks = []
    def add_tricks(self,trick):
        self.tricks.append(trick)
        
hel = pet("Panda")
bul = pet("snake")
#print(hel.type)#shared by all pets
# print(hel.name)#unique to hel

# print(bul.type)
# print(bul.name)

hel.add_tricks("Rollover")

print(hel.tricks)
print(bul.tricks)
