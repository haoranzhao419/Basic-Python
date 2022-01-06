a = input('Please enter a string:')
b = dict()
for i in a:
    c = a.count(i)
    b[i] = c  # 可以通过dict[key] = value向字典中逐一添加键值对
print(b)