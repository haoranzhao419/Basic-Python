Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]
b = []
for a in Nine[0]:
    if a == ' ':
        print(a)
        b.append(a)
    else:
        print("9")
print(b)
# a = (input('Please enter the radius of the circle:'))
# try:  # 用try except finally
#     e = int(a)
#     pi = 3.1416
#     b = 2 * pi * e
#     c = pi * e ** 2
#     print('perimeter =', b)
#     print('Area =', c)
# except ValueError:
#     print('You have not inserted a valid number!')


# a = int(input('please enter the first number:'))
# b = int(input('Please enter the second number:'))
# if a % b == 0:
#     print(a, 'is a multiple of ', b)
# else:
#     print(a, 'is not a multiple of ', b)


# def list_max(int_list):
#     a = max(int_list)
#     return a
#
#
# print(list_max([1, 2, 8, 3, 10, 5]))
