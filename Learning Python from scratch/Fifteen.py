import random
f = open("fi1.txt", mode="a")  # "mode="可加可不加
f.writelines(["hello python\n", "I have a wonderful family\n", "my\n", "name\n", "is\n", "zhao\n", "hao\n", "ran\n"])
f.close()
e = open("fi1.txt", "r")
content = e.readlines()
total = 0
b = []
for i in content:
    a = i.split()
#    print(a)
    for j in a:
        b.append(j)
        total = total + 1
#        print(total)
print(b)
c = random.sample(b, 10)
print(c)
print(total)
e.close()
