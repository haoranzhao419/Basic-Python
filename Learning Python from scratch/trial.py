# import math
#
# print("PI=%7.4f" % math.pi)
# # %a.bf，a表示浮点数的打印长度，b表示浮点数小数点后面的精度，按理说a要大于等于b+2，%f时表示原值，默认是小数点后6位数 。
# # %af，表示输出数字的总位数为a位，小数点也占一位，不够时左侧补零。
# print('PI=%f' % math.pi)

# a = ["1", "2", "6", "9", "8"]
# print(a[3])


# a = "zhaohaoran"  # 当步长为正数时正向切片， 当步长为负数时逆向切片， 字符串切片完成后仍为字符串
# b = a[-5: -1: 1]  # 当start比stop数小的时候，步长只能为正数
# c = a[5: 9: 1]
# d = a[:: -1]
# e = a[-1:-5:-1]   # 当start比stop数大的时候，步长只能为负数，且都是start那个能取到，stop那个取不到
# f = a[9: 5: -1]
# print(b)
# print(c)
# print(d)
# print(e, f)


# a = "zhaohaoran"
# b = int(len(a))
# c = b/2
# print(a[0: c])

# def flower(n):
#     b = str(n)
#     c = len(b)
#     d = []
#     total = 0
#     for i in b:
#         d.append(i)
#     print(d)
#     for i in d:
#         d = int(i)
#         s = d ** c
#         total = total + s
#     print(total)
#     if total == n:
#         return True
#     else:
#         return False
#
#
# # flower(153)
# print(flower(153))

# num = 8
# num_p = 0
# num_t = num
# while num_t != 0:
#     num_p = num_p * 10 + num_t % 10
#     num_t = num_t / 10
#
# if num == num_p:
#     print('it is a palin')
# else:
#     print('No')

# def p(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return n * p(n - 1)
#
#
# print(p(3))

# 斐波那契数列编程（递归算法）
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
#
# print(fib(150))


# 汉诺塔
# def hanoi(n, A, B, C):
#     if n == 1:
#         print("Move", n, "from", A, "to", C)
#     else:
#         hanni(n-1, A, C, B)
#         print('Move', n, 'from', A, 'to', C)
#         hanni(n-1, B, A, C)
#
#
# hanni(2, 'left', "middle", "right")  # 函数再调用完后会会回到这一行

# print(6*"x")
# print("x" + 4*" "+ "x")


# a = "SDDF"
# a.lower()
# print(a.lower())

# {'John': 5.4, 'Alice': 8.7, 'Bob': 3.2}
# for key in o:

# a = {"zhao": 1, "hao": 2, "ran": 3}
# print(max(a, key=a.get ))

# mystr = 'abcabcabc'
# print(str.find('bc'))
#
# list1 = [1, 2, 3, 4]
#
# data = 4
#
#
# def add_1(data):
#     if type(data) == list:
#
#         for i in range(len(data)):
#             data[i] += 1
#
#     else:
#
#         data += 1
#
#
# add_1(list1)
#
# add_1(data)
#
# print(list1)
# print(data)

# def fib(n):
#
#     if n == 1 or n == 2:
#
#         return 1
#
#     return fib(n-1) + fib(n-2)
#
# print(fib(5))

#

# list1=[1,2,3,4,5,6]
#
# print(list1[-3:6])
#
# print("abc\"ab")
# print(0x10)
#
# print('abc' in ('abcdefg'))
# print('abc' in ['abcdefg'])
#
# a = [1,2,3]
# b = a
# c = a[ : ]
# print(a is b)
# print(a is c)
#
#
#
# x = 0
#
# for i in range(20):
#
#     x += 1
#
# print(x)


# def triangle_area(a, b, c):
#     if a + b > c > a - b:
#         s = (a + b + c) / 2
#         area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
#     else:
#         return False
#     return area
#
#
# print(triangle_area(13, 12, 5))
# print(triangle_area(1, 2, 3))


# def triangle_area(a, b, c):
#
#     if a + b > c > a - b:
#
#     ​   s = (a + b + c) / 2
#
#     ​    ​area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
#
#     ​else:
#
#     ​    ​return False
#
#     ​return area

# print(bin("I have a big family"))
# print('I have a big family'.encode())
# def encode(s):
# 实现字符串转换成二进制表示
# 字符串 -> ASCII码数值 -> 二进制表示
# str_bin = ' '.join([bin(ord(c)).replace('0b', '') for c in s]) 该代码可转换成裁开的for 循环，如下四行代码：

# tmp = []
# for c in s:
#     tmp.append(bin(ord(c)).replace('0b', ''))
#
# str_bin = ' '.join(tmp)  # join 和 split 操作是相对字符串和列表之间的转化
#
# print(str_bin)

# encode("I have a big family")

# List1 = [1, 2, 3, 4]
# # print(List1[2])
# List2 = [5, 6, 7, 8]
# List1.append(List2)
# print(List1)
# # print(List2)
# List2.append(List1)
# print(List2)
# print(List1)
# print(List1[4])
#
# def get_Money(self):
#     return self.__money
#
#
# def set_Money(self, value):
#     if isinstance(value, int):
#         self.__money = value
#     else:
#         print("error: 不是整型数字")
#
#
# def get_Money(self):
#     return self.__money
#
#
# def set_Money(self, value):
#     if isinstance(value, int):
#         self.__money = value
#     else:
#         print("error: 不是整型数字")
#
#
# money = property(get_Money, set_Money)
#
# @property
# def money(self):
#     return self.__money
#
#
# @money.setter
# def money(self, value):
#     if isinstance(value, int):
#         self.__money = value
#     else:
#         print("error:不是整型数字")

# def remainder_n(a, b):
#     interger = a//b
#     print(type(a//b))
#     c = b * interger
#     re = a - c
#     return re
#
#
# print(remainder_n(6, 5))
# print(6//5)
# print(6 % 5)


# def draw_rectangle(a, b, c):
#         print(c*a)
#         for i in range(b-2):
#             print(a+(c-2)*" "+a)
#             i += 1
#         print(c*a)
#
#
# while True:
#     a = input("Please enter a character('q' to quit): ")
#     if a == 'q':
#         quit()
#     else:
#         b = int(input("Please enter the number of lines: "))
#         c = int(input("Please enter the number of columns: "))
#         draw_rectangle(a, b, c)


# a = ['a', 'b', 'c', 'd']
# b = a
# c = a[:]
# print(a[0:3])
# print(a is b)
# print(a is c)
#
# a = "123"
# b = a
# c = a[:]
# print(a[0:2])
# print(a is b)
# print(a is c)

# str1 = "this is string example....wow!!!"
# str2 = "exam"
# print(str1.find(str2))  # 字符串中的find和index用法有相似之处，都课返回子字符串在父字符串中第一次出现的位置。
# print(str1.index(str2))

# eyes = ("brown", "hazel", "amber", "green", "blue", "gray")
# print(eyes[2:-1])
# print(eyes[2:5])

# list1 = [1, 2, 3, 4]
# data = 4
#
#
# def add_1(data):
#     if type(data) == list:
#         for i in range(len(data)):
#             data[i] += 1
#     else:
#         data += 1
#
#
# add_1(list1)
#
# add_1(data)

#
# def draw_rectangle(char, lines, columns):
#     print(columns*char)
#     for i in range(0, lines-2):
#         print(char+(columns-2)*" "+char)
#     print(columns*char)
#
#
# while True:
#     char = input('Please enter a character:')
#     if char == 'q':
#         quit()
#     else:
#         lines = int(input('Please enter the number of lines:'))
#         columns = int(input('Please enter the number of columns:'))
#     draw_rectangle(char, lines, columns)


# def are_consecutive(a_list):
#     i = 0
#     while i < (len(a_list)-1):
#         if abs(a_list[i]-a_list[i+1]) == 1:
#             i += 1
#         else:
#             return False
#     return True
#
#
# print(are_consecutive([5, 5, 7, 8]))

# mystr = 'abcabcabc'
# print(mystr.find("bc"))

# hair = "black", "brown", "blonde", "red"
# eyes = ("brown", "hazel", "amber", "green", "blue", "gray")
# colors = (hair, eyes)
# print(colors)
# print(eyes[3:5])
#
# list1 = [1, 2, 3, 4]
# data = 4
#
#
# def add_1(data):
#     if type(data) == list:
#         for i in range(len(data)):
#             data[i] += 1
#     else:
#         data += 1
#
#
# add_1(list1)
# print(list1)
# add_1(data)
# print(data)
#
# print([1, 2, 3]*3)
# print(set('apple'))
# print(set([1, 2, 3, (2, 3), 2]))

# def triangle_area(a, b, c):
#     if a+b > c & abs(a-b) < c:
#         p = (a+b+c)/2
#         area = (p*(p-a)*(p-b)*(p-c))*0.5  # 注意乘号一定要写
#         return area
#     else:
#         return False
#
#
# print(triangle_area(3, 4, 5))

# a = input('Please enter the students and their grades:')
# b = a.split(";")
# D = dict()
# H = 0
# for i in b:
#     c = i.strip()
#     d = c.split()
#     H = H + float(d[1])
#     D[d[0]] = float(d[1])
#
# result = H/len(D)
# y = '%.2f' % result
# x = round(result, 2)
# print((type(x)))
# print("The average of the grades was:"+str(x))
# print('The average of the grades was:', str(x))
# print('The student that got the best grade was:' + max(D, key=D.get))

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def getage(self):
#         return self.age
#
#     def getname(self):
#         return self. name
#
#     def setage(self, age):
#         self.age = age
#
#     def setname(self, name):
#         self.name = name
#
#     def save_the_file(self, filename):
#         with open(filename, "wt") as myfile:
#             myfile.write(self.name+ " " + str(self.age))
#             myfile.close()

# h = int(input('Please input a height:'))
# n = int(input('Please enter the nth time it fall on the ground:'))
# initial_height = h
# total_height = 0
# nth_h = 0
# a_list = []
# if n == 1:
#     total_height = h
#     nth_h = h / 2
#     a_list.append(nth_h)
# elif n >= 2:
#     u = 1
#     while u <= n:
#         h = h / 2
#         total_height = total_height + 2*h
#         a_list.append(h)
#         u = u + 1
#     total_height = total_height + initial_height

# for i in a_list:
#     total_height = total_height + i
# total_height = total_height * 2

# print(sum(a_list)*2)
# print(min(a_list))
# print(total_height)

# string = input('Please enter a string with a specific format:')
# a_list = string.split("|")
# Dict = dict()
# for i in a_list:
#     a = i.split(":")
#     Dict[a[0]] = int(a[1])
# print(Dict)
#
# a_str = "k:1|k1:2|k2:3|k3:4"
# d = {k: int(v) for t in a_str.split("|") for k, v in (t.split(":"),)}
# print(d)

# f = open("second.txt", "wt")
# text = f.write("AFDGdgdDSFAfdsa")
# f.close()
# with open("second.txt", "rt") as f1:
#     content = f1.read()
#     f1.close()
# a_list = []
# for i in content:
#     if 65 <= ord(i) < 90:
#         i = chr(ord(i)+33)
#         a_list.append(i)
#     elif 97 <= ord(i) < 122:
#         i = chr(ord(i)-31)
#         a_list.append(i)
#     elif ord(i) == 122:k:1|k1:2|k2:3|k3:4
#         i = chr(ord(i)-57)
#         a_list.append(i)
#     elif ord(i) == 90:
#         i = chr(ord(i)+7)
#         a_list.append(i)
#
# another_string = "".join(a_list)
# with open("final.txt", "wt") as f2:
#     f2.write(another_string)
#     f2.close()

# a = "zhaohaoran"
# print(a[::-1])
# print(a[:-1])

# def the_answer(s1, s2):
# c1 = [0] * 26
# c2 = [0] * 26
# for i in range(len(s1)):
#     pos = ord(s1[i]) - ord("a")  # 将A-Z这26个字母变成0-25
#     c1[pos] = c1[pos] + 1
# for i in range(len(s2)):
#     pos = ord(s2[i]) - ord('a')
#     c2[pos] = c2[pos] + 1
# j = 0
# stillOK = True
# while j < 26 and stillOK:
#     if c1[j] == c2[j]:
#         j = j + 1
#     else:
#         stillOK = False
#     return stillOK

# if c1 == c2:
#     return True
# else:
#     return False
# a_dict = dict()
# a_dict1 = dict()
# for i in list(s1):
#     a_dict[i] = list(s1).count(i)
# for j in list(s2):
#     a_dict1[j] = list(s2).count(j)
# print(a_dict1)
#     print(a_dict)
#     if a_dict == a_dict1:
#         return True
#     else:
#         return False
#
#
# print(the_answer("aaaggeh", "gagaahe"))
# a_list = []
# for i in a_list:
#     i.startwith

# def Fibonacci(a_number):
#     if a_number < 3:
#         return 1
#     else:
#         return Fibonacci(a_number - 1) + Fibonacci(a_number - 2)


# print(Fibonacci(5))

# a = list(map(lambda x: x ** 2, [1, 2, 3, 4]))
# print(a)
# print([x ** 2 for x in [1, 2, 3, 4]])
# b = list(filter(lambda x: x < 0, [1, -1, 5, 6, -9]))
# print(b)
# print([x for x in [1, -1, -5, 6, 9] if x > 0])

import functools as func
import operator
import os

# print(func.reduce(operator.mul, [1, 2, 3, 4]))
# func.reduce(operator.add, map(os.path.getsize, filter(lambda x: x.endswith(".py"), "demo")))


# def factorial(x):
#     if x <= 1:
#         return 1
#     return x * factorial(x - 1)
#
#
# def foactorial_1(x):
#     a_list = []
#     for i in range(1, x+1):
#         a_list.append(i)
#         i += 1
#     return func.reduce(operator.mul, a_list)
#
#
# print(foactorial_1(5))

# print(9 // 5)

# def factorial(x):
#     a_list = []
#     for i in range(1, x+1):
#         a_list.append(i)
#         i += 1
#     return func.reduce(operator.mul, a_list)
#
#
# print(factorial(4))

def max_3(x, y, z):
    return max(max(x, y), z)


