a_dict = dict()


def to_dict(a_string):
    a_list = a_string.split("|")
    # print(a_list)
    for i in a_list:
        # print(i)
        a = i.split(":")
        # print(a)
        # for j in a:
        a_dict[a[0]] = int(a[1])
    return a_dict


print(to_dict("k:1|k1:2|k2:3|k3:4"))










