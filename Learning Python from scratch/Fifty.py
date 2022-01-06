import pickle

# t1 = ("This is a string", 42, [1, 2, 3], None)
# print(t1)
# p1 = pickle.dumps(t1)
# print(p1)
a1 = "apple"
b1 = {1: "One", 2: "Two", 3: "Three"}
c1 = ["fee", "fie", "foe", "fum"]
f1 = open("temp.pkl", "wb")
pickle.dump(a1, f1, True)
pickle.dump(b1, f1, True)
pickle.dump(c1, f1, True)
f1.close()
f2 = open("temp.pkl", "rb")
a2 = pickle.load(f2)
print(a2)
b2 = pickle.load(f2)
print(b2)
c2 = pickle.load(f2)
print(c2)
f2.close()
"""检索所支持的格式"""
print(pickle.format_version)
print(pickle.compatible_formats)

a = [1, 2, 3]
b = a
a.append(4)
c = pickle.dumps((a, b))
d, e = pickle.loads(c)
print(d)
print(e)
d.append(5)  # 只对d进行append(5)后，d与e都发生了变化
print(d)
print(e)

l = [1, 2, 3]
l.append(l)
print(l)  # output为：[1, 2, 3, [...]]  [...]用于表示该列表中的内容与之前的内容相重复
l[3]
l[3][3]
p = pickle.dumps(l)
l2 = pickle.loads(p)
print(l2)
print(l2[3])
print(l2[3][3])

a1 = [1, 2]
b1 = [3, 4]
a1.append(b1)
print(a1)
b1.append(a1)
print(b1)
print(a1)
print(a1[2])
print(b1[2])
print(a1[2] is b1)
print(b1[2] is a1)
f = open("temp1.pkl", "w")
pickle.dump((a1, b1), f)
f.close()
f = open("temp1.pkl", "r")
c, d = pickle.load(f)
f.close()
print(c)