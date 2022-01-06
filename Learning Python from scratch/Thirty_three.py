a = []
b = 0
c = 0
try:
    while True:
        d = input('enter a number or Enter to finish:')
        if d == '':
            break
        else:
            e = int(d)
            a.append(e)
            b += 1
            c = c + e

    f = max(a)
    g = min(a)
    a.sort(reverse=True)  # reverse = True 是降序排列， reverse = False 是升序排列

    print('number: ', a)
    print("count = ", b)
    print("sum = ", c)
    print("lowest = ", f)
    print("highest= ", g)

    if len(a) % 2 == 0:
        print((a[int(len(a)/2)]+a[int(len(a)/2)]+1)/2)
    else:
        print(a[int((len(a)-1)/2)])
except ValueError:
    print("please input a number")

