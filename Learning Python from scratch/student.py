class People:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name_age(self):
        return self.__age, self.__name

    def set_name_age(self, another_name, another_age):
        if isinstance(another_name, str):
            self.__name = another_name
        if isinstance(another_age, int):
            self.__age = another_age


class Course:
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name_score(self):
        return self.__name, self.__score

    def set_name_score(self, new_name, new_score):
        if isinstance(new_name, str):
            self.__name = new_name
        if isinstance(new_score, int):
            self.__score = new_score


class Student(People):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.__id = id

    def get_name_age(self):
        return super().get_name_age(), self.__id

    def set_name_age(self, another_name, another_age):
        return super().set_name_age()

    course = Course()


