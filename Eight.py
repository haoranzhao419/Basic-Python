first = input("please put a string:")
n = int(input("please put a number:"))
a = first[-1:-1 - n:-1]
d = a[::-1]
c = len(first)
b = first[0:c - n]
print(d + b)
