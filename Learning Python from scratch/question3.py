class Student:
    name = ""
    age = ""

    def get_the_name(self):
        self.name = input("Please input your name: \n")

    def get_the_age(self):
        self.age = int(input("Please input your age: \n"))

    def modify_the_name(self):
        self.name = input("Please input the new name: \n")

    def modify_the_age(self):
        self.age = int(input("Please input the new age: \n"))

    def save_to_file(self):
        filename = input("Please input the path of the file: \n")
        with open(filename, "a") as f:
            f.write(self.name + " " + str(self.age))


stu = Student()
stu.get_the_age()
stu.get_the_name()
stu.modify_the_age()
stu.modify_the_name()
stu.save_to_file()