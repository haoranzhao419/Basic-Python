def Tower_of_Hanoi(disks, resource, auxiliary, target):
    if disks == 1:
        print("Move disk 1 from peg {} to peg {}.".format(resource, target))
        return

    Tower_of_Hanoi(disks - 1, resource, target, auxiliary)
    print('Move disk {} from peg {} to peg {}.'.format(disks, resource, target))
    Tower_of_Hanoi(disks - 1, auxiliary, resource, target)


disks = int(input("the number of the disks: "))
print(Tower_of_Hanoi(disks, "a", "b", "c"))

# Tower_of_Hanoi(disks - 1, resource, target, auxiliary)
# print('Move disk {} from peg {} to peg{}.'. format(disks, resource, target))
# Tower_of_Hanoi(disks - 1, auxiliary, resource, target)