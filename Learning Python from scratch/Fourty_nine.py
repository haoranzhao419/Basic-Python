import os
import pickle
import sys


def export_students(filename, information):
    f1 = None  # f1为局部变量
    try:
        f1 = open(filename, "wb")
        pickle.dump(information, f1, True)
        return True
    except (EnvironmentError, pickle.PicklingError) as err:
        print("{0}: export error:{1}".format(
            os.path.basename(sys.argv[0]), err
        ))
        return False
    finally:
        if f1 is not None:
            f1.close()


list_students = [['John', '5.4'], ['Alice', '8.7'], ['Bob', '3.2']]
print(export_students("students.b", list_students))


def import_students(filename):
    f = None
    try:
        f = open(filename, "rb")
        a = pickle.load(f)
        return a
    except (EnvironmentError, pickle.UnpicklingError) as err:
        print("{0}: import error: {1}". format(
            os.path.basename(sys.argv[0], err)
        ))
        return False
    finally:
        if f is not None:
            f.close()


print(import_students("students.b"))