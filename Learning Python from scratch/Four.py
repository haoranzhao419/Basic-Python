a = "zhaohaoran123456"
print(a[-1: -7: -1])

b = "Mike and Tom"
print(b.split(" "))
print(b.replace("Mike", "Jerry"))
print(b.swapcase())
print(b.upper())
print(b.lower())

C = ["zhao", "hao", "ran"]
print(" ".join(C))

d = "Mike and Tom"
print(d.center(20))

e = ["my", "name", "is"]
f = ["zhao", "hao", "ran"]
e.insert(0, "li")
print(e)
e.extend(f)
print("Extended List: ", e)
print(len(e))

bands = {"marxes": ["moe", "curly"], "kk": [True, "moon"]}
print(bands["kk"][1])
position = {(100, 100): "zhongguancun", (123, 23): "Pizza"}
print(position[(100, 100)])

people = {}
people["name"] = "Tom"
people["ID number"] = 20
bar = {"first name": "yu", "last name": "li", "manager": "jin"}
people.update(bar)
people.update(one=["hao"], two="ran")
print(people)

aset = set("zhaohaoran")
print(aset)
aset.update("22")
print(aset)
aset.add(5)
print(aset)
print(aset.pop())
aset.remove("z")
print(aset)
print(aset | set("liyan"))
print(aset)
print(aset & set("asopfha"))
print(aset - set("jadsifob"))

print("p", 2, 3, end="\n", sep=",")

first = ["li", "yan", "jin", "shan"]
print(first * 3)
print(first[3])

mylist = [1, 2, 3, 4, 5]
print(mylist[1: 4])
print(mylist[2: 5])
print(mylist[0: 5: 2])
print(mylist[-3: -6: -1])

t = "Mike and Tom"
print("/".join(t))
print(t.split(","))

oneset = set([1, 2, 3, 4, 5, ])
seset = set([2, 4, 6, 8, 10])
print(oneset & seset)  # 交集
print(oneset | seset)  # 并集
print(seset - oneset)
print(oneset - seset)
print(oneset ^ seset)
oneset.update((12,))
print(oneset)
oneset.update("12")
print(oneset)
oneset.remove(1)
print(oneset)

mydict = {1: "Mon", "line1": 3332}
print(mydict.items())
print(mydict.keys())
print(mydict.values())
print(2 in mydict)
print(mydict.pop(1))
print(mydict)
mydict[2] = "Tuesday"
print(mydict)

selist = [1, 2, 3, 4, 5, 6, 7]
print(selist[0:-1])
print(selist[0:6])





