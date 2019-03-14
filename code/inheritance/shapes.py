class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2*(self.__width + self.__height)


class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)


rect = Rectangle(2, 3)
print("rectangle 2x3: area = {}, perimeter = {}".format(rect.area(), rect.perimeter()))

square = Square(4)
print("square 4x4: area = {}, perimeter = {}".format(square.area(), square.perimeter()))
