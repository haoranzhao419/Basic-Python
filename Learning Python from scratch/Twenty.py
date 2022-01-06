class People:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __str__(self):
        return "(%s, %s)" % (self.name, self.city)

    __repr__ = __str__

    def moveto(self, newcity):
        name = self.name
        city = newcity.city
        return People(name, city)

    def __lt__(self, other):
        return self.city < other.city


a = People("Zhao haoran", "Dezhou")
b = People("Jishan", "Jinan")
c = b.moveto(a)
print(c)
s = list()
s.append(People("Zhao haoran", "dezhou"))
s.append(People("Jishan", "jinan"))
s.append(People("liyan", "zibo"))
s.append(People("yinbitong", "dongying"))
s.sort()
print(s)


class Teacher(People):
    def __init__(self, name, city, school):
        super().__init__(name, city)     # 父类方法初始化，只有名称，无self
        self.school = school

    def moveto(self, newschool):
        name = self.name
        city = self.city
        school = newschool.school
        return Teacher(name, city, school)

    def __str__(self):

        return "(%s, %s, %s)" % (self.name, self.city, self.school)

    __repr__ = __str__

    def __lt__(self, other):
        return self.school < other.school


z = list()
z.append(Teacher("Zhaohaoran", "dezhou", "wuzhong"))
z.append(Teacher("Jishan", "jinan", "yizhong"))
z.append(Teacher("liyan", "zibo", "jiuzhong"))
z.append(Teacher("yinbitong", "dongying", "sanzhong"))
z.sort()
print(z)
