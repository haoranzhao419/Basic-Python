while True:
    year_number = input("please enter a year number('q' to quit): ")
    if year_number == "q":
        break  # quit() break是结束这一层循环
    else:
        try:
            year_number = int(year_number)
        except:
            print("你需要输入一个合法的年份")
            continue  # continue是结束这一轮循环
        if year_number % 100 != 0:
            if year_number % 4 == 0:
                print(year_number, "is leap year")
            else:
                print(year_number, "is not a leap year")
        else:
            if year_number % 400 == 0:
                print(year_number, "is leap year")
            else:
                print(year_number, "is not a leap year")
