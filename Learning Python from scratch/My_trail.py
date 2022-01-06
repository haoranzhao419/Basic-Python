# a = input('Please enter a string:')
# set_a = set(a)
# b = list()
# c = set()
# d = dict()
# for i in set_a:
#     num = a.count(i)
#     b.append((i, num))
#     c.add((i, num))
#     d[i] = num
# print(b)
# print(c)
# print(d)


# for i in list(input("Please enter a number: ")):
# print(i)
# a = int(input('Please enter the number of seconds:'))
# b = 3600*24
# print(a//b)
# c = a - b*(a//b)
# print(c//3600)
# d = c - 3600*(c//3600)
# print(d//60)
# e = d - 60*(d//60)
# print(e)

# a = input('Please enter a string: ')
# for i in range(len(a)):
#     if a[i] == a[(len(a)-1)-i]:
#         continue
#     else:
#         print("%s is not a palindrome" % a)
#         quit()
# print('%s is a palindrome' % a)


# a = input("Please enter a sentence: ")
# print(len(a.split()))
# D = dict()
# for i in a.split():  # string.split()当括号中什么都不写的时候表示要以空格作为分隔符
#     D[i] = len(i)
# print(max(D, key=D.get))

# print("abcdefg", "hijklmn")  # ","是将字符串进行连接，连接的字符串之间是有空格的；"+"也是连接两个字符串的，直接连接没有空格

a = "dsafga"
print(list(a))