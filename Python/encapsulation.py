class Student:
    """
    def __init__(self,name=None,roll_no=None):
        self._name = name
        self._roll_no = roll_no
    """

    def set_name(self,name):
        self._name =  name

    def set_roll(self,roll):
        self._roll_no = roll

    def get_name(self):
        print(f"Name: {self._name}")

    def get_roll(self):
        print(f"Roll: {self._roll_no}")

Ibuki = Student()
Ibuki.set_name("Ibuki")
Ibuki.get_name()
Ibuki.set_roll(123)
Ibuki.get_roll()
