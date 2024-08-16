class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def calculate_area(self):
        return self.width * self.length

    def calculate_perimeter(self):
        return 2 * (self.width + self.length)

my_rectangle = Rectangle(2, 5)

area = my_rectangle.calculate_area()
perimeter = my_rectangle.calculate_perimeter()

print(f"Area of Rectangle: {area}")
print(f"Perimeter of Rectangle: {perimeter}")
