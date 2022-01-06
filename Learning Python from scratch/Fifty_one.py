h = int(input("please put a number of height: "))
n = int(input("please put how many time it fall down: "))
ini_number = 1
total_height = 0
a_list = []
if n == 1:
    total_height = h
else:
    while ini_number <= n:
        a_list.append(h)
        ini_number += 1
        total_height = (total_height + 2 * h)
        h = h / 2
if n > 1:
    real_total_height = total_height - max(a_list)
else:
    real_total_height = h
    h = h / 2
print(h)
print(real_total_height)

tour = []
height = []
h = int(input("请输入最初的高度："))
n = int(input("请输入反弹的次数："))
for i in range(n):
    if i == 0:
        tour.append(h)
    else:
        tour.append(2 * h)
    h = h / 2
    height.append(h)
print("经过的高度为：tour = {0}".format(sum(tour)))  # 这里的{0}和{1}分别对应的是后面format中对应的第一和第二个
print("第{0}次反弹高度：height = {1}".format(n, height[-1]))
