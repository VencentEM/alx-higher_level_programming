#!/usr/bin/python3
"""
Rectangle Module python3
from models.base import Base
Base = __import__("base").Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle Class that inherits from Base super class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init method for Rectangle Class
        Arguments:
            - width (int): Width of the rectangle.
            - height (int): Height of the rectangle.
            - x (int): Horizontal position.
            - y (int): Vertical position.
            - id: Identifier.

        Raises:
            - TypeError: If the input is not an integer
            - ValueError: if either of width or height <= 0.
            - TypeError: If either of x or y is not an int.
            - ValueError: if either of x or y < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width Getter for rectangel class"""
        return self.__width

    @width.setter
    def width(self, width):
        """
        width Setter  for rectangel class

        args:
            - width (int): Width of the rectangle.
        """
        if type(width) is not int:
            raise TypeError(f"width must be an integer")
        elif width <= 0:
            raise ValueError(f"width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """height Getter for rectangel class"""
        return self.__height

    @height.setter
    def height(self, height):
        """
        height Setter for rectangel class

        args:
            - height (int): height of the rectangle.
        """
        if type(height) is not int:
            raise TypeError(f"height must be an integer")
        elif height <= 0:
            raise ValueError(f"height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """x Getter for rectangel class"""
        return self.__x

    @x.setter
    def x(self, x):
        """
        x Setter for rectangel class

        args:
            - x (int): x of the rectangle.
        """
        if type(x) is not int:
            raise TypeError(f"x must be an integer")
        elif x < 0:
            raise ValueError(f"x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """y Getter for rectangel class"""
        return self.__y

    @y.setter
    def y(self, y):
        """
        y Setter for rectangel class

        args:
            - y (int): y of the rectangle.
        """
        if type(y) is not int:
            raise TypeError(f"y must be an integer")
        elif y < 0:
            raise ValueError(f"y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """returns area of rectangle"""
        return self.__height * self.__width

    def display(self):
        """print Rectangel as # to stdout"""
        print("\n"*self.__y, end='')
        for i in range(self.__height):
            print(" "*self.__x, end='')
            for j in range(self.__width):
                print("#", end='')
            print("\n", end='')

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Format:
            "[Rectangle] (id) x/y - width/height"
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "\
               f"{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle.

        Args:
            *args: Variable positional arguments.
            **kwargs: Variable keyword arguments.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
                elif key == 'id':
                    self.id = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
