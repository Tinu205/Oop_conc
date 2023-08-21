# aggregation is like nested struct creating an instance of class inside another class
class Student():
    def __init__(self,name,id):
        self.name = name
        self.id = id

class University:
    def __init__(self):
        self.student = Student
        self.list_of_studs = []

    def admit_student(self,student):
        self.list_of_studs.append(student)
    def expel_student(self,student):
        self.list_of_studs.remove(student)
    def list_of_stud(self):
        for stud in self.list_of_studs:
            print(stud.name,stud.id)

anna = University()
Roger = Student("Roger","22ec050")
anna.admit_student(Roger)
anna.list_of_stud()