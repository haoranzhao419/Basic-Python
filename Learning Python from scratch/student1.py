class People:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def get_name_age(self):
        return self.age, self.name  # 在get的方法中要用return

    def set_name_age(self, another_name, another_age):
        if isinstance(another_name, str):
            self.name = another_name  # 在set方法中不用写return（也不要写return）
        if isinstance(another_age, int):
            self.age = another_age  # 在set方法中不用写return（也不要写return）

    name_age = property(get_name_age, set_name_age)


class Course:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_name_score(self):
        return self.name, self.score

    def set_name_score(self, new_name, new_score):
        if isinstance(new_name, str):
            self.name = new_name
        if isinstance(new_score, int):
            self.score = new_score

    name_age = property(get_name_score, set_name_score)


class Student(People):
    def __init__(self, name, age, s_id, course):
        super().__init__(name, age)
        self.course = Course(course)  # 在这里调用了Course类中的一个实例course，并进行方法的初始化
        self.s_id = s_id
        # self.course = course

    def get_name_age(self):
        return super().get_name_age(), self.s_id

    def set_name_age(self, another_name, another_age):
        return super().set_name_age()

    def get_Course(self):
        return self.course.get_name_score
        # return course_name

    def set_Course(self, course):
        self.course = course

    def show_info(self):
        print(
            "student's name is " + self.name + "\n" + "student's age is" + self.age + "\n" + "student's id is " + self.s_id + "\n" +
            "student's course is " + self.course.get_name_score)

    name_age = property(get_name_age, set_name_age)


a = People("zhaohaoran", 19)
print(a.get_name_age)
print(a.get_name_age())  # 在这里必须加括号！！！
print(a.name_age)
a.name = "guobin"  # 这里利用set方法修改name和age的值
a.age = 18
print(a.name_age)