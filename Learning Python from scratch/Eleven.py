num = [1, 2, 5, 6, 9]
num2 = [5, 9, 6, 2, 8]


def mul(a):
    return a * 3


print(list(map(mul, num)))
print(list(map(lambda a: a * 3, num)))  # lambda函数为匿名函数，冒号之前为函数的参数，之后为函数体
print(list(map(lambda a, b: a + 1.0 / b, num, num2)))


def func_test(*args):
    for arg, i in zip(args, range(len(args))):
        print("arg%d=%s" % (i, arg))  # %d 和 %s 的意思是digit，string，表示要放到字符串中的数据类型


func_test(12, 34, "abcd", True)


def func_test1(**kwargs):
    for key, val in kwargs.items():
        print("%s=%s" % (key, val))


func_test1(myname="Tom", sep="comma", age=23)


def func_test2(**kwargs):
    for key in kwargs:
        print(kwargs[key])
        print("%s" % key)


func_test2(myname="Tom", sep="comma", age=23)



