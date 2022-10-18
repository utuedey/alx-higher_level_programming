#!/usr/bin/python3
"""
The Rectangle class module
"""


class Rectangle:
    """Represent a Rectangle.
    Private instance attribute: width:
        -property def width(self): to retrieve it
        -property setter def width(self, value): to set it
    Private instance attribute: height:
        -property def height(self): to retrieve it
        -property setter def height(self, value): to set it:
    Instantiation with optional width and height:
    def __init__(self, width=0, height=0)
    Public instance method: def area(self):
    that returns the rectangle area
    Public instance method: def perimeter(self):
    that returns the rectangle perimeter
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize the data"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """Return the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height to value."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width to value."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__height == 0:
            return 0
        elif self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """Return a formatted string"""
        if self.__height == 0:
            return ""
        elif self.__width == 0:
            return ""
        else:
            my_string = ""
            for i in range(0, self.__height):
                for j in range(0, self.__width):
                    my_string += str(self.print_symbol)
                my_string += '\n'
            return my_string[:-1]

    def __repr__(self):
        """ return a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """del an instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Finds the biggest Rectangle based on the area
        Args:
            rect_1: Rectangle instance
            rect_2: Rectangle instance different from rect_1
        Returns:
            The instance with the biggest area
            or rect_1 if both rectangles have the same area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
