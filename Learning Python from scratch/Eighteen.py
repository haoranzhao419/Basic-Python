class Force:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def show(self):
        print("Force<%s, %s>" % (self.x, self.y))

    def add(self, force2):
        x = self.x + force2.x  # force2也是Force类中的一个对象实例
        y = self.y + force2.y
        return Force(x, y)

    __add__ = add

    def __str__(self):
        return "F<%s, %s>" % (self.x, self.y)            # 这个函数与show()函数的作用是一样的

    # __repr__ = __str__    # 可有可无

    def __mul__(self, other):
        x, y = self.x * other, self.y * other
        return Force(x, y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)     # 返回一个逻辑值


f1 = Force(0, 1)
print(f1)
# f1.show()  # 由于f1就是指对象自己，所以show()中不需要再有参数调用了
# Force.show(f1)  # Force.show(f1) <=> f1.show()
f2 = Force(5, 9)
a = f2.add(f1)
a.show()
f3 = f1 + f2
print(f3)
f3 = f1 * 3.5
print(f3)
print(f1 == f2)

