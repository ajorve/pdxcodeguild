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


class Polygon(Shape):
    def __init__(self, ss, t="polygon"):
        """create polygon, ss gives lengths of sides (at least 3 sides)"""
        print("In polygon __init__")
        Shape.__init__(self, t)
        self.sides = ss

    def __str__(self):
        print("In polygon __str__")
        res = Shape.__str__(self) + ", side lengths: " +\
              " ".join([str(l) for l in self.sides])
        return res

    def perimeter(self):
        print("In polygon perimeter")
        return sum(self.sides)


class Triangle(Polygon):
    def __init__(self, s1=1, s2=1, s3=1, t="triangle"):
        """create rectangle with sidelengths s1, s2, and s3"""
        Polygon.__init__(self, [s1, s2, s3], t)

    def area(self):
        """Heron's Formula"""
        print("In triangle area")
        semip = sum(self.sides)/2.0
        prod = semip*(semip-self.sides[0])*(semip-self.sides[1])*(semip-self.sides[2])
        return math.sqrt(prod)


class Rectangle(Polygon):
    def __init__(self, w: object = 1, h: object = 1, t: object = "rectangle") -> object:
        """create rectangle of width w and height h"""
        Polygon.__init__(self, [w, h], t)

    def __str__(self):
        print("in rectangle __str__")
        res = Polygon.__str__(self)+ ", width: " + str(self.sides[0]) + \
              ", height: " + str(self.sides[1])
        return res

    def area(self):
        print("in rectangle area")
        return self.sides[0]*self.sides[1]


class Square(Rectangle):
    def __init__(self, l=1, t="square"):
        Rectangle.__init__(self, l, l, t)


class Circle(Shape):
    def __init__(self, r=1, t="circle"):
        """create circle, argument gives radius"""
        Shape.__init__(self,t)
        self.radius = r

    def __str__(self):
        res = Shape.__str__(self) + ", radius: " + "%.2f" % self.radius
        return res

    def perimeter(self):
        return 2*math.pi * self.radius

    def area(self):
        return math.pi*self.radius * self.radius


def demo():
    s = Shape()
    print("s prints as", s, "\n")

    p = Polygon([2, 2, 2, 2, 2])
    print("p prints as", p)
    print("perimeter of p is %.2f" % p.perimeter(),"\n")

    t = Triangle(2, 2, 3)
    print("t prints as", t)
    print("perimeter of t is %.2f" % t.perimeter())
    print("area of t is %.2f" % t.area(), "\n")

    r = Rectangle(2, 3)
    print("r prints as", r)
    print("perimeter of r is %.2f" % r.perimeter())
    print("area of r is %.2f" % r.area(), "\n")

    sq = Square(5)
    print("sq prints as", sq)
    print("perimeter of sq is %.2f" % sq.perimeter())
    print("area of sq is %.2f" % sq.area(), "\n")

    c = Circle()
    print("c prints as", c)
    print("perimeter of c is %.2f" % c.perimeter())
    print("area of c is %.2f" % c.area(), "\n")

    # polymorphism at work in the calls to s.perimeter() and s.area()!
    l = [p, t, r, sq, c]
    print("sum of perimeters is %.2f" % sum([s.perimeter() for s in l]))
    print("sum of areas is %.2f" % sum([s.area() for s in l]))
