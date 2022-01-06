def gougu():
    for i in range(1, 100):
        for j in range(1, 100):
            for k in range(1, 100):
                if i ** 2 + j ** 2 == k * k:
                    yield "(%d, %d, %d)" % (i, j, k)


l = list()  # l = []与l = list()都是表示创建一个空列表的意思
for i in gougu():
    l.append(i)
print(l)

