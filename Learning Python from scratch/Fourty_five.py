def check_all(f, l):
    a = map(f, l)
    return all(a)


# all()函数用于判断给定的可迭代参数中的所有元素是否都为True，如果是则返回True，否则返回False。空元组、空列表返回值为True元素除了是 0、空、None、False 外都算 True，

print(check_all(lambda x: x < 10, [3, 7, 5]))
