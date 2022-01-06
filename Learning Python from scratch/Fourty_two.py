def rectangle(a, b, c):
    print(c*a)
    var = 1
    while var <= (b-2):
        print(a + (c-2) * " " + a)  # 要注意在连接字符串时是用，还是用 +
        var += 1
    print(c*a)


a = input("Please enter a character:")
b = int(input('Please enter the number of lines:'))
c = int(input('Please enter the number of columns:'))
rectangle(a, b, c)
