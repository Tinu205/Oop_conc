# TODO: Create the Base Shape Class
# - Define a class named `Shape` as the base class.
# - Add an `__init__` method to initialize common attributes.
# - Implement methods `calculate_area` and `calculate_perimeter` in the `Shape` class that raise a `NotImplementedError`.

# TODO: Create Subclasses for Specific Shapes
# - Define subclasses for different shapes (e.g., `Rectangle`, `Circle`, `Triangle`).
# - In each subclass, inherit from the `Shape` class.
# - Override the `calculate_area` and `calculate_perimeter` methods to provide specific implementations for each shape.

# TODO: Implement Shape Instances
# - Create instances of different shapes (e.g., rectangle, circle, triangle) using the subclasses.
# - Set attributes such as length, width, radius, or side lengths for each shape.

# TODO: Demonstrate Inheritance
# - Calculate and print the area and perimeter of each shape instance using the methods you defined in the subclasses.
# - Showcase how the inherited methods from the `Shape` base class are being used.

# TODO: Extra Challenges (Optional)
# - Create additional subclasses for different shapes (e.g., `Square`, `Pentagon`) and demonstrate how they fit into the shape hierarchy.
# - Implement a way to compare different shapes based on their areas or perimeters.
# - Add user input to create and interact with shape instances interactively.

# TODO: Comments and Documentation
# - Add appropriate comments to explain your code and the purpose of each class and method.
# - Write a brief documentation explaining the project and how the inheritance hierarchy works.

from abc import ABC,abstractmethod
class Shape(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def calculate_area(self):
        pass
    
    @abstractmethod
    def calculate_perimeter(self):
        # raise NotImplementedError("The subclass haven't been implemented")
        pass


class Rectangle(Shape):
    def __init__(self, name,lenght,breadth):
        super().__init__(name)
        self.name = name
        self.lenght = lenght
        self.breadth = breadth

    def calculate_area(self):
        print(f"Area of {self.name} -> {self.lenght*self.breadth}")
    def calculate_perimeter(self):
        print(f"Perimeter of {self.name} -> {2*(self.breadth+self.lenght)}")

class Square(Shape):
    def __init__(self,name,side):
        super().__init__(name)
        self.name = name
        self.side = side
    
    def calculate_area(self):
        area = self.side**2
        print(f"Area -> {area}")

    def calculate_perimeter(self):
        perimeter = self.side * 4
        print(f"Perimeter -> {perimeter}")

sq = Square("Flat",10)
sq.calculate_area()
sq.calculate_perimeter()

rec = Rectangle("Cot",60,40)
rec.calculate_perimeter()
rec.calculate_area()

## Will raise error
# dia = Shape("diamond") 
# dia.calculate_area()
# dia.calculate_perimeter()