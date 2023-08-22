# Define a class named "Student" to represent individual students
class Student():
    def __init__(self, name, id):
        self.name = name  # Student's name
        self.id = id      # Student's ID

# Define a class named "University" to manage students' information
class University:
    def __init__(self):
        # Initialize an empty list to hold student instances (aggregation)
        self.list_of_studs = []

    # Method to admit a student to the university
    def admit_student(self, student):
        self.list_of_studs.append(student)  # Add the student to the aggregation

    # Method to expel a student from the university
    def expel_student(self, student):
        self.list_of_studs.remove(student)  # Remove the student from the aggregation

    # Method to display the list of students in the university
    def list_of_stud(self):
        for stud in self.list_of_studs:
            print(stud.name, stud.id)  # Print each student's name and ID

# Create an instance of the University class named "anna"
anna = University()

# Create an instance of the Student class named "Roger"
Roger = Student("Roger", "22ec050")

# Admit the student "Roger" to the university "anna"
anna.admit_student(Roger)

# Display the list of students in the university "anna"
anna.list_of_stud()
