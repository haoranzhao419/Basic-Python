
val = input("请输入带有温度表示符号的温度值：")
if val[-1] in ["C", "c"]:
    temp = 1.8 * int(val[0:-1]) + 32
    print("转换后的温度为： %.2fF" % temp)
elif val[-1] in ["F", 'f']:
    c = (int(val[0:-1]) - 32) / 1.8
    print("转换后的温度为： %.2fC" % c)
else:
    print("error occurs")
