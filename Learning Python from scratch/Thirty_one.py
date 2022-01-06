a_list = list()
while True:
    a = input('please enter a number:')
    if a == '':
        break
    else:
        b = int(a)
        a_list.append(b)

print(a_list)
a_list.sort()
print(a_list)
if len(a_list) % 2 == 0:
    i = int(len(a_list)/2)
    j = i - 1
    print((a_list[i]+a_list[j])/2)
else:
    print(a_list[int(len(a_list)//2)])