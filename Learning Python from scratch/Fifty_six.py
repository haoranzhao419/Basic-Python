from exception import First_error


def draw_rectangle(a, b, c):
    print(c * a)
    for i in range(b - 2):
        print(a + (c - 2) * " " + a)
        i += 1
    print(c * a)


while True:
    a = input("Please enter a character('q' to quit): ")
    if a == 'q':
        quit()
    else:
        b = int(input("Please enter the number of lines: "))
        c = int(input("Please enter the number of columns: "))
        draw_rectangle(a, b, c)