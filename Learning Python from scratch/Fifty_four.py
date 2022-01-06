# name = ["张三", "李四", "王五", "李六"]  # 保存名字列表
# sign = ["白羊座", "双鱼座", "狮子座", "处女座"]  #保存星座列表
# dict1 = {i : j for i, j in zip(name, sign)}    # 字典推导式


a = input('please enter a string:')
b = []
c = []
first_list = a.split("|")
for i in first_list:
    second_list = i.split(":")
    b.append(second_list[0])
    c.append(int(second_list[1]))

dict1 = {i: j for i, j in zip(b, c)}
print(dict1)

# 字典推导式
d = {k: int(v) for t in str1.split("|") for k, v in (t.split(":"),)}