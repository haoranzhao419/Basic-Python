class Student:
    def __init__(self, grade, name):  # 构造函数，对变量的值进行初始化
        self.grade = grade
        self.name = name

    def __lt__(self, other):
        return self.grade > other.grade

    def __str__(self):  # __str__这个函数是让输入的Student后面的两个参数， 能够输出
        return "(%d, %s)" % (self.grade, self.name)

    __repr__ = __str__  # 这一行必须有。
    # Student的正是字符串表示， 我们让他跟易读表示相同


s = Student(90, "i")
e = Student(75, "l")
print(s.grade < e.grade)
print(s)

a = list()
a.append(Student(70, "zhao"))
a.append(Student(90, "li"))
a.append(Student(32, "JIN"))
print(a)
a.sort()
print(a)
