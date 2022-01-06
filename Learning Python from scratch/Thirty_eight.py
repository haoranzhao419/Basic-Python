a = input('Please enter a string:')
b = []
c = set(a)  # 字符串能直接转化为列表用list(string)或直接转化为集合用set(string)
for i in a:
    d = a.count(i)
    b.append((i, d))
print(b)
d = set(b)
print(d)
e = dict(b)
print(e)






