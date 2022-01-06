a = int(input('Please enter the number of seconds:'))
b = a % 86400
c = a / 86400
g = int(c)
d = b / 3600
h = int(d)
i = b % 3600
j = int(i/60)
k = i % 60
print(g)
print(h)
print(j)
print(k)