# 斐波那契数列编程（递归算法）
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(fib(150))

