# from django.template.defaultfilters import lower


# def lower_string(s):
#     a = lower(s)
#     b = list(a)
#     return b
#
#
# print(lower_string("UNIVERSITY"))


def show_lower(s):  # 要注意函数的嵌套！！！

    def is_lower(c):
        return c.islower()  # 返回的是一个布尔值

    return list(filter(is_lower, s))
    # a = list(s)
    # for i in a:
    # print(i)
    # return i.islower()
    # return list()
    # a = list(s)
    # for i in a:
    #     b = i.islower
    # return b


# b = list(filter(show_lower, ))
print(show_lower('University'))


def l(s):
    a = []
    for i in s:
        a.append(i)
    return a  # 返回的是一个字符串列表


def f(c):
    return c.islower()


print(list(filter(f, l('dsfafFZSDFG'))))


# print(i)
# return i.islower()


def show_is_lower(s):
    def is_lower(c):
        return c.islower()

    return list(filter(is_lower, s))


print(show_is_lower("University"))
