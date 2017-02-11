# example inheritance heirarchy - shapes
# lkd, 04/20/09; rje 12/02/2011
import math


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"

    def __repr__(self):
        return self.__repr__()

    def __eq__(self):
        return self.__eq__()


class Shape(object):
    def __init__(self, t="shape"):
        print("In shape __init__:")
        self.tag = t

    def __str__(self):
        print("In shape __str__:")
        return self.tag

    def __repr__(self):
        print("In shape __repr__: ")
        return self.__str__()


class Rectangle(object):
    def __init__(self, w: object = 1, h: object = 1, t: object = "rectangle") -> object:
        """create rectangle of width w and height h"""
        Shape.__init__(self, [w, h], t)

    def __str__(self):
        print("in rectangle __str__")
        res = Polygon.__str__(self)+ ", width: " + str(self.sides[0]) + \
              ", height: " + str(self.sides[1])
        return res

    def area(self):
        print("in rectangle area")
        return self.sides[0]*self.sides[1]