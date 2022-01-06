print("\\大家好\\")
print("\"大家好\"")
a = "Hello world"
print(a[1: 6])
c = "welcome to london"
d = "come"
print(c.replace("london", d))
for j in c:
    print(j)

months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = input("请输入月份数（1-12）：")
a = int(n)
b = months[(a-1)*3:(a-1)*3+3]
print(b)
