# abcdefghijklmnopqrstuvwxyz abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijkkl
x = 3.6
y = x
print(y is x)
z = 3.5
print(z is x)
print(id(x), id(y), id(z))
print(type(5.6))
print("zhaohaoran", "gaowenhao")  # 用逗号连接两个字符串的时候会出现中间会多加一个空格的情况
print("zhaohaoran"+"gaowenhao")  # 用+连接两个字符串时直接将两个字符串连接起来，中间没有间隔。