#!/usr/bin/python3
"""
Square Module python3
from models.rectangle import Rectangle
Rectangle = __import__("rectangle").Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class square that enhirit from rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor

        args:
            - size: int
            - x: int
            - y: int
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        Return a string representation of the rectangle.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - "\
               f"{self.size}"

    @property
    def size(self):
        """set the size of the square object"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Upadate the attribue value"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
                elif key == 'id':
                    self.id = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
        }
