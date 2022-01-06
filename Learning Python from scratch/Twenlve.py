def flower(n):
    total = 0
    if n >= 100:
        a = str(n)
        a_list = []
        for i in a:
            a_list.append(i)
        # print(a_list)
        length = len(a_list)
        # print(length)
        for i in a_list:
            b = int(i)
            c = b ** length
            total = total + c
        if total == n:
            return True
        else:
            return False

    else:
        print("you put a wrong number")


def second(largenum):
    e = []
    for i in range(100, largenum + 1):
        flower(i)
        if flower(i):
            e.append(i)
    print(e)


second(100000)
