import turtle  # import用来引用外部库。


def drawSnake(rad, angle, len, neckrad):
    a = ["blue", "red", "yellow", "green", "black"]  # 运用数组
    for i in range(len):
        turtle.pencolor(a[i])
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.pencolor("pink")
    turtle.circle(rad, angle / 2)
    turtle.fd(rad)
    turtle.circle(neckrad + 1, 180)
    turtle.fd(rad * 2 / 3)
    turtle.done()


def main():
    turtle.setup(1300, 800, 0, 0)  # 四个数字中前两个表示该图形界面的宽度和高度，后两个表示窗口在屏幕中左上角的坐标位置。
    pythonsize = 20  # 表示小乌龟运行轨迹的宽度。
    turtle.pensize(pythonsize)
    turtle.seth(-30)  # 小乌龟启动运行时运动的方向,包含一个输入参数，是角度值
    drawSnake(40, 60, 5, 10)   # 再调用drawSnake函数。


main()  # 该程序先调用的是main函数


