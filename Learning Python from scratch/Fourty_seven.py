def are_consecutive(a_list):
    s = 1
    while s < len(a_list):
        if abs(a_list[s] - a_list[s-1]) == 1:
            s += 1
        else:
            return False
    return True


print(are_consecutive([9, 8, 8, 6]))
