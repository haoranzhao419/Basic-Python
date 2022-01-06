a = (input("Please enter the students and their grades: \n")).split(";")
Sum = 0
d = dict()
for i in a:
    c = (i.strip()).split(" ")
    # string.strip()可用于去掉字符串左右两端的空格
    d[j] = float(d[1])
    j = d[0]
    g = g + float(d[1])
l = g / len(d)
y = round(l, 2)
# y = "%.2f" % l  # "%.nf" % float表示保留n位小数， 或用round(float, n)保留n位小数，两者转化后都是字符串
print('The average of the grades was: %s' % y)
print("The student that got the best grade was:", max(d, key=d.get))  # 可用max(dict, key=dict.get)得到字典中最大的值对应的键是什么
