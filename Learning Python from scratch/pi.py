from random import random
from math import sqrt
from math import pow
import time

time.perf_counter()
n = input("输入的数为:")
a = eval(n)
count = 0
for i in range(1, a):
    x, y = random(), random()
    sum = sqrt(pow(x, 2) + pow(y, 2))
    if sum <= 1:
        count = count + 1
pi = 4 * (count / a)
print("Pi的值是 %s" % pi)
print("程序运行时间是%-5.5ss" % time.perf_counter())
