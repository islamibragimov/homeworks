from abc import ABC, abstractmethod
import math
class AbstractShape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Circle(AbstractShape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r ** 2
    def perimeter(self):
        return 2 * math.pi * self.r
class Rectangle(AbstractShape): 
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h
    def perimeter(self):
        return 2 * (self.w + self.h)
while True:
    print("\nChoose a shape:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        radius = float(input("Enter the radius: "))
        shape = Circle(radius)
    elif choice == "2":
        width = float(input("Enter the width: "))
        height = float(input("Enter the height: "))
        shape = Rectangle(width, height)
    elif choice == "3":
        print("Salomat boshed!")
        break
    else:
        print("Choice nest-ku")
        continue
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")