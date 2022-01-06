a = input("please enter a sentence:")
b = a.split(" ")
print("The sentence has", len(b), "words")
c = []
for i in b:
    # print(i)
    c.append(len(i))
if len(i) == max(c):
    print(i)

