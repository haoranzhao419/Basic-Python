import turtle


def tree(branchlen, cu, a):
    if branchlen > 5:
        a.pensize(cu)
        a.forward(branchlen)
        a.left(25)
        tree(branchlen - 20, cu-2, a)
        a.left(25)
        tree(branchlen - 20, cu - 2, a)
        a.right(75)
        tree(branchlen - 20, cu-2, a)
        a.right(25)
        tree(branchlen - 20, cu - 2, a)
        a.left(50)
        a.backward(branchlen)


# turtle.done()


def main():
    t = turtle.Turtle()  # 生成海龟
    # myWin = turtle.Screen()
    t.left(90)  # 海龟位置调整
    t.up()
    t.backward(100)
    t.down()
    t.color("green")  # 调整结束
    tree(75, 10, t)  # 画树， 树干长度75 ,为什么非得是t
    # myWin.exitonclick()


main()
turtle.done()