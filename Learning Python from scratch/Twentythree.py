def fib():    # 斐波那契数列编程
    a, b = 1, 1
    yield a
    yield b
    while True:
        yield a + b
        a = a +b
        b = a-b


for fn in fib():
    print(fn)
    if fn > 100000000000000:
        break








