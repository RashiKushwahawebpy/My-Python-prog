# WAP using function to perform many task
from factoriallib import *
#main program
while True:
    print("you can perform following operation")
    print("1 - Factorial calculation")
    print("2 - Addition")
    print("3 - x to power y calculation")
    print("4 - Exit")
    k = int(input(" enter your choice 1 to 4: "))
    if (k == 1):
        n = int(input("enter a number for factorial calculation: "))
        y = fact (n)
        print("factorial =", y)
    elif (k == 2):
        a = int(input("enter first no.: "))
        b = int(input("enter second no.:"))
        c = add_nums(a, b)
        print("sum =", c)
    elif (k == 3):
        a = int(input("enter first no.: "))
        b = int(input("enter second no.: "))
        c = powercal(a, b)
        print (a,"to power ",b, "is" ,c)
    elif (k == 4):
        break
    else:
        print("wrong choice")
# main close