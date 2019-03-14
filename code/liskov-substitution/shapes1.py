class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def name(self):
        return "Rectangle"

    def width(self):
        return self.__width

    def height(self):
        return self.__height

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2*(self.__width + self.__height)


class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)

    def name(self):
        return "Square"


def print_rect_info(shape):
    if not isinstance(shape, Rectangle):
        raise Exception("shape is not a Rectangle")
    print("{} {}x{}: area = {}, perimeter = {}".format(shape.name(), shape.width(), shape.height(), shape.area(), shape.perimeter()))


rect = Rectangle(2, 3)
print_rect_info(rect)

rect.set_width(4)
print_rect_info(rect)

square = Square(4)
print_rect_info(square)

square.set_height(5)
print_rect_info(square)  # Square 4x5!
