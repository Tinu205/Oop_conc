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

# hel.add_tricks("Rollover")

# print(hel.tricks)
# print(bul.tricks)

class owner(pet):
    def __init__(self, name,owner) -> None:
        super().__init__(name)
        self.owner = owner
# petty = owner("Daisy","Homie")

# petty.add_tricks("Bark")
# print(petty.owner)

class sound(pet):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print("Woof")
# kutty = sound("patti")
# print(kutty.type)
# kutty.make_sound()
# print(isinstance(kutty,pet))
# print(isinstance(kutty,sound))

# Encapsulation and access modifers
class person:
    def __init__(self,name,age) -> None:
        self._name = name #protected that's can be view but can't be changed
        self.__age = age #can't be viwed or changed
        pass
    def get(self):
        return f"{self._name} is {self.__age} years old."
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def newage(self,newage):
        self.__age = newage
paari = person("Paari",22)
print(paari.get())

#print(paari.__age) wont work because it's protected
# print(paari.age)
# paari.__age = 12 #This wont work
# print(paari.age)
# paari.newage = 40
# print(paari.age) #Now the value is upadated

#### Class relaitonships ####
## Associations 
## Aggrigations
## compotions """Creating a instance of a class inside another class"""