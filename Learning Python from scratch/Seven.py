#  计算哪年哪月
odic = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
tdic = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
first = int(input("Please input the year you choose:"))
if (first % 4 == 0 and first % 100 != 0) or first % 400 == 0:  # 四年一闰，百年不闰，400年再闰
    print("今年是闰年")
    second = int(input("Please input the month you choose:"))
    print(tdic[second])

else:
    print("今年不是闰年")
    third = int(input("Please input the month you choose:"))
    print(odic[third])
