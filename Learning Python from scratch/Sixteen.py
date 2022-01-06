import easygui as g
import sys
while 1:
    g.msgbox("嗨！欢迎进入第一个GUI制作的小游戏")
    msg = "你希望学到什么知识呢？"
    title = "互动小游戏"
    choices = ["琴棋书画", "四书五经", "程序编写", "逆向分析"]
    choice = g.choicebox(msg, title, choices)
    # 选择choices中的一个
    g.msgbox("你的选择是：" + str(choice), "结果")  # str（choice）的输出结果是choices中的一个
    msg = "你希望重新开始小游戏吗？"
    title = "请选择"
    #  ccbox()函数有continue 和 cancel 两个按钮，提供用户选择
    if g.ccbox(msg, title):
        pass
    else:
        sys.exit(0)
