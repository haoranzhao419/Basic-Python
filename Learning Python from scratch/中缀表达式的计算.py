def calculate(calculate_list):
    array_list = []
    stack_list = []
    for i in calculate_list:
        if i.isnumeric():
            array_list.append(i)
        else:
            if len(stack_list) ==0:
                stack_list.append(i)
            elif i in "*/":
                stack_list.append(i)
            elif i in "+-" and stack_list[len(stack_list) -1] in "*/":
                print(stack_list)
                t = stack_list.pop()
                array_list.append(t)
                stack_list.append(i)
            else:
                stack_list.append(i)
    while stack_list:
        array_list.append(stack_list.pop())
    return array_list


def operate_list(array_list, operator):
    for i in array_list:
        if i == operator:
            operates = array_list.index(operator)
            if operator == "*":
                number = int(array_list[operates-2]) * int(array_list[operates-1])
                array_list.pop(operates)
                array_list[operates-2:operates] = str(number)
                print(array_list)
    if len(array_list) >= 3 & array_list.count("*") >= 1:
        operate_list(array_list, "*")


def operate_list(array_list, operator):
    for i in array_list:
        if i == operator:
            operates = array_list.index(operator)
            if operator == "/":
                number = int(int(array_list[operates-2]) / int(array_list[operates-1]))
                array_list.pop(operates)
                array_list[operates-2:operates] = str(number)
                print(array_list)
    if len(array_list) >= 3 & array_list.count("/") >= 1:
        operate_list(array_list, "/")


def operate_list(array_list, operator):
    for i in array_list:
        if i == operator:
            operates = array_list.index(operator)
            if operator == "-":
                number = int(array_list[operates-2]) - int(array_list[operates-1])
                array_list.pop(operates)
                array_list[operates-2:operates] = str(number)
                print(array_list)
    if len(array_list) >= 3 and array_list.count("-") >= 1:
        operate_list(array_list, "-")


def operate_list(array_list, operator):
    for i in array_list:
        if i == operator:
            operates = array_list.index(operator)
            if operator == "+":
                number = int(array_list[operates-2]) + int(array_list[operates-1])
                array_list.pop(operates)
                array_list[operates-2:operates] = str(number)
                print(array_list)
    if len(array_list) >= 3:
        operate_list(array_list, "+")


