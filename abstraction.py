from abc import ABC, abstractmethod 

# Define an abstract base class 'Animal' using ABC (Abstract Base Class) module.
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # This method will be inherited and overridden by subclasses.

# Define a class 'Dog' that inherits from 'Animal'.
class Dog(Animal):
    def make_sound(self):
        print("Woof, Woof")  # Override the abstract method with a specific implementation.

# Define a class 'Cat' that inherits from 'Animal'.
class Cat(Animal):
    def make_sound(self):
        print("Meow, meow")  # Override the abstract method with a specific implementation.

# Create an instance of 'Cat' class.
tom = Cat()
tom.make_sound()  # Call the overridden method for Cat instance, prints "Meow, meow".

# Create an instance of 'Dog' class.
spike = Dog()
spike.make_sound()  # Call the overridden method for Dog instance, prints "Woof, Woof".
