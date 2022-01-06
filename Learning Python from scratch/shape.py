import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)  # hypot(x, y) 等价于 sqrt(x*x + y*y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):   # __str__ 和 __repr__ 表达的其实是差不多的
        return "Point({0.x!r}, {0.y!r})".format(self)  # ！在format中的作用和【%r(s, d) % 内容】是类似的

    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)


class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def distance_from_origin(self):
        return math.sqrt(self.x ^ 2 + self.y ^ 2 + self.z ^ 2)

    def __eq__(self, other):
        return super().__eq__(other) and self.z == other.z

    def __str__(self):
        return "Point3D({0.x!r}, {0.y!r}, {0.z!r})".format(self)

    def __str__(self):
        return "({0.x!r}, {0.y!r}, {0.z!r})".format(self)


class Circle:
    def __init__(self, x, y, R):
        self.o = Point(x, y)
        # super.__init__()
        self.R = R

    def __eq__(self, other):
        return self.o == other.o and self.R == other.R

    def __str__(self):
        return "Circle({0.o.x!r}, {0.o.y!r}, {0.R!r})".format(self)

    def __str__(self):
        return "({0.o.x!r}, {0.o.y!r}, {0.R!r})".format(self)

    def area(self):
        return math.pi * self.R ** 2

    def perimeter(self):
        return math.pi * 2 * self.R
