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
## Associations is simply relating one class with other class

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []  # List to hold associated courses

    def enroll(self, course):
        self.courses.append(course)

class Course:
    def __init__(self, course_code, title):
        self.course_code = course_code
        self.title = title

# Association example:
student1 = Student("Alice", "S123")
student2 = Student("Bob", "S456")

course1 = Course("C101", "Mathematics")
course2 = Course("C202", "History")

# Enrolling students in courses
student1.enroll(course1)
for course in student1.courses:
    print(f"- {course.title}")

##Aggriggations
## whole part of class contains methods of another class
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []  # List to hold associated Employee objects

    def add_employee(self, employee):
        self.employees.append(employee)

# Aggregation example:
employee1 = Employee("Alice", 101)
employee2 = Employee("Bob", 102)

department1 = Department("HR")
department1.add_employee(employee1)
department1.add_employee(employee2)

department2 = Department("Engineering")
department2.add_employee(employee1)

print(f"{employee1.name} is part of the {department1.name} department.")
print(f"{employee1.name} is also part of the {department2.name} department.")
##