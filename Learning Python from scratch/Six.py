import time


#  计算1+2！+3！+...+n!的值并输出程序运行时间
t1 = time.time()
number = input("Please input a number:")
n = eval(number)
count = 1
total = 0
for var in range(1, n + 1):
    count = count*var
    total = total + count

print(total)
t2 = time.time()
print(t2-t1)

