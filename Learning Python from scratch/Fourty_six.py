a = input("Please enter the students and their grades: \n")
b = a.split(";")
print(b)
g = 0
h = 0
o = dict()
for i in b:
    c = i.strip()
    # string.strip()可用于去掉字符串左右两端的空格
    d = c.split(" ")
    e = float(d[1])
    j = d[0]
    o[j] = e
    g = g + e
    h += 1
l = g / h
y = round(l, 2)
# y = "%.2f" % l  # "%.nf" % float表示保留n位小数， 或用round(float, n)保留n位小数，两者转化后都是字符串
print('The average of the grades was: %s' % y)
print("The student that got the best grade was:", max(o, key=o.get))  # 可用max(dict, key=dict.get)得到字典中最大的值对应的键是什么

