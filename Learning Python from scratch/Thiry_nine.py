a = input('Please enter a string: ')
b = set()
for i in a:
    c = a.count(i)
    b.add((i, c))
# 这里实际上是先产生了一个这样的集合{('p', 1), ('r', 2), ('o', 1), ('g', 1), ('r', 2), ('a', 1), ('m', 1)}， 由于集合的互异性所以去掉一个重复的。
print(b)

