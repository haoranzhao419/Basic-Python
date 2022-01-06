a = set()
for x in range(10):
    for y in range(x):
        a.add(x + y)

print(a)


def even_number(max):
    n = 0
    while n < max:
        yield n
        n += 2


for i in even_number(max=10):       # i就是even_number（max）函数的返回值（yield值）
    print(i)

agen = (x*x for x in range(10))
print(agen)
for n in agen:
    print(n)
