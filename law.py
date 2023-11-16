#creating a polygon class
class Polygon:
    def __init__(self, sides):#intialize the function
        self.sides = sides
#function to display the sides
    def display_sides(self):
        print(f"Sides of the polygon: {', '.join(map(str, self.sides))}")

#creating a triangle in polygon class
class Triangle(Polygon):
    def __init__(self, sides):#intialize the function
        super().__init__(sides)
#function to calculate area
    def calculate_area(self):
        a, b, c = self.sides
        # Using Heron's formula to calculate the area of a triangle
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area
#function to calculate perimeter
    def calculate_perimeter(self):
        return sum(self.sides)

#creating a square in polygon class
class Square(Polygon):
    def __init__(self, side):#intialize the function
        super().__init__([side] * 4)
#function to calculate area
    def calculate_area(self):
        side = self.sides[0]
        area = side ** 2
        return area
#function to calculate perimeter
    def calculate_perimeter(self):
        return sum(self.sides)


#creating a rectangle in polygon class
class Rectangle(Polygon):
    def __init__(self, length, width):#intialize the function
        super().__init__([length, width, length, width])
#function to calculate area
    def calculate_area(self):
        length, width = self.sides[0], self.sides[1]
        area = length * width
        return area
#function to calculate perimeter
    def calculate_perimeter(self):
        return sum(self.sides)


# sample input:

triangle = Triangle([3, 4, 5])
print("Triangle:")
triangle.display_sides()
print("Area:", triangle.calculate_area())
print("Perimeter:", triangle.calculate_perimeter())

square = Square(4)
print("\nSquare:")
square.display_sides()
print("Area:", square.calculate_area())
print("Perimeter:", square.calculate_perimeter())

rectangle = Rectangle(5, 6)
print("\nRectangle:")
rectangle.display_sides()
print("Area:", rectangle.calculate_area())
print("Perimeter:", rectangle.calculate_perimeter())
