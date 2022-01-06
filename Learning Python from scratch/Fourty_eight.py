f = open("tmp.b", "wb")
a = f.write("zhr is handsome".encode("UTF-8"))
# print(type(a)) [['John', '5.4'], ['Alice', '8.7'], ['Bob', '3.2']]
# "tmp.txt".encode()
print(a)
f.close()
#
# infile = file("in.mp3", "rb")
# outfile = file("out.txt", "wb")
# # struct.unpack()方法可用来解析各种二进制文件，二进制文件是不保留存储方式的数据格式，因此读二进制文件是应该知道二进制文件的储存格式
#
# def main():
#     while 1:
#         c = infile.read(1)
#         if not c:
#             break
#         outfile.write(hex(ord(c)))
#     outfile.close()
#     infile.close()
#
#
# if __name__ == '__main__':
#     main()
# f = open("tmp.txt", "at")
# f.write("\nI love my family")
# f.close()
#
# with open("tmp.txt", "rt") as myfile:
#     print(myfile.read())


# from base64 import b64decode, b64encod


