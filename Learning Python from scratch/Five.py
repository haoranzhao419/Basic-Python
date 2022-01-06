import math


def main():
    try:
        a, b, c = eval(input("Please put three numbers:"))
        delta = b * b - 4 * a * c
        if delta > 0:
            root1 = (-b + math.sqrt(delta)) / 2 * a
            root2 = (-b - math.sqrt(delta)) / 2 * a
            print("Two different real roots are:", root1, root2)
    except ValueError as excObj:
        if str(excObj) == "math domain error":
            print("No Real Roots.")
        else:
            print("You didn't give me the right number of coefficients")
    except NameError:
        print("\nYou didn't enter three numbers.")
    except TypeError:
        print("\nYour input were not all numbers.")
    except SyntaxError:
        print("\nYour input was not in the correct form. Missing comma")
    except:
        print("\nSomething went wrong, sorry!")


main()
