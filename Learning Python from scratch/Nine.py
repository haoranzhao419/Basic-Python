one = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8",
       "nine": "9", "zero": "0"}
first = input("an English string:")
a = first.split("-")  # split分离出来的是一个列表，这里的split('-')中的-是表示以'-'为分隔标志，在分隔后的列表中并不显现出来'-'
b = []
for i in a:
    print(one[i])
    b.append(one[i])

print(b)
print("".join(b))
