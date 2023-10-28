class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Circle:
    def __init__(self, radius):
        self.radius = radius

def calculate_area(shape):
    if isinstance(shape, Rectangle):
        return shape.width * shape.height
    elif isinstance(shape, Circle):
        return 3.14159265359 * shape.radius ** 2

# Usage
rectangle = Rectangle(4, 5)
circle = Circle(3)

print("Area of rectangle:", calculate_area(rectangle))
print("Area of circle:", calculate_area(circle))

"""
In this example, we have two shape classes, Rectangle and Circle, and a 
calculate_area function that calculates the area of these shapes based on their types. 
The problem with this code is that if you want to add a new shape, say a Triangle, 
you would need to modify the calculate_area function, which violates the Open-Closed Principle.

Now, let's refactor this code to adhere to the Open-Closed Principle:

After OCP (Adhering to OCP):
"""


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159265359 * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

# Usage
rectangle = Rectangle(4, 5)
circle = Circle(3)
triangle = Triangle(6, 8)

shapes = [rectangle, circle, triangle]

for shape in shapes:
    print(f"Area of {shape.__class__.__name__}: {shape.calculate_area()}")
