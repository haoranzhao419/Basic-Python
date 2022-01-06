file1 = open("first.txt", "wt")
text = file1.write("abcFDGSgfdsgGUIHG")  # text的type是int类型的print（text）的结果是输入的字符数
file1.close()

with open("first.txt", "r+") as myfile:
    content = myfile.read()
    print(content)  # 这里已经将程序关闭
a_list = []
for i in content:
    if 64 < ord(i) < 90:
        i = chr(ord(i)+33)
        a_list.append(i)
    elif ord(i) == 90:
        i = chr(ord(i)+7)
        a_list.append(i)
    elif 96 < ord(i) < 122:
        i = chr(ord(i)-31)
        a_list.append(i)
    elif ord(i) == 122:
        i = chr(ord(i)-57)
        a_list.append(i)

print(a_list)
c = ''.join(a_list)  # join是将列表转化为字符串！！！
print(c)
file = open("new.txt", "w+")
file.write(str(c))
file.close()
# 空字符串不能修改
# A = 65, B = 66, a = 97 ,a-B=31  b = 98   b-A = 33, Z = 90
# print(ord("A"))
# print(chr(ord('A')+40))
# if
# with open("tmp.txt", "rt") as myfile:
# print(myfile.read())

# for mychar in content:
#     if(mychar.isupper()):
#         mychar = mychar.lower()
#     elif (mychar.islower()):
#         mychar = mychar.upper()
#     temp = ord(mychar)
#     if temp in range(ord('A'), ord('Z')+1):
#         temp += 1
#         chr(temp)
#     else:
#         pass
# f.close()
