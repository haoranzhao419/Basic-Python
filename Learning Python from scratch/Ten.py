def a_list(alist):
    sum_step = 0
    for i in alist:
        sum_step = sum_step + i
    return sum_step


#  one_list = [123, 45, 4894, 84]
#  调用函数，将返回值赋给my_sum
my_sum = a_list(alist=[123, 45, 4894, 84])
print(my_sum)
