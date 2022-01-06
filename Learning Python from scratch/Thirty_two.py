import random  # random库中的主要函数的用法：random()函数生成（0，1）范围内的随机小数， randint（a，b）生成指定范围内的随机整数

a = ['the', "a", "another"]
b = ["cat", "dog", "man", "woman"]
c = ["sang", "ran", "jumped"]
d = ["loudly", "quietly", "well", "badly"]
e = 0
g = input('please input a number between 1 and 10:')
h = int(g)
if g.isdigit() & 1 <= h <= 10:

    while e < h:
        f = random.randint(1, 2)
        if f == 1:
            print(random.choice(a), random.choice(b), random.choice(c), random.choice(d))
        # choice() 方法返回一个列表，元组或字符串的随机项
        else:
            print(random.choice(a), random.choice(b), random.choice(c))
        e = e + 1
else:
    while e < 5:
        f = random.randint(1, 2)
        if f == 1:
            print(random.choice(a), random.choice(b), random.choice(c), random.choice(d))
        # choice() 方法返回一个列表，元组或字符串的随机项
        else:
            print(random.choice(a), random.choice(b), random.choice(c))
        e = e + 1
