# Author: Daniel Paparo

#Main question 5
def square(x):
        #returns the square of x
        return x * x

def fibs(x):
        #prints the first x Fibonacci numbers
        #each number is the sum of the previous two
        a,b = 0,1
        for i in range(x):
                print("fib(", i, ") = ", a)
                a,b = b,a+b
                

#Extra question 1
#print(square(20))
#print(fibs(100))

#Extra question 2
def answers():
    print("8 = ",8)
    print("8 * 2 = ", 8*2)
    print("8 ** 2 = ", 8 ** 2)
    print("8 / 6 = ", 8 / 6)
    print("8 // 6 = ", 8 // 6)
    print("8 // 6 = ", 8 // 6)
    print("8 / 0 = dont do that...")

#Extra question 3a
def three_a():
    print("This program illustrates a chaotic function")
    x = float(input("Enter a number between 0 and 1: "))
    for i in range(1,10):
        x = 2.0 * x * (1 - x)
        print(x)

#Extra question 3b
def three_b():
    print("This program illustrates a chaotic function")
    x = float(input("Enter a number between 0 and 1: "))
    for i in range(1,20):
        x = 3.9 * x * (1 - x)
        print(x)

#Extra question 3c
def three_c():
    print("This program illustrates a chaotic function")
    x = float(input("Enter a number between 0 and 1: "))
    y = int(input("How many do you want to print: "))
    for i in range(1,y):
        x = 3.9 * x * (1 - x)
        print(x)

#Extra question 3d
def three_d():
    print("This program illustrates a chaotic function")
    x = float(input("Enter a number between 0 and 1: "))
    y = int(input("How many do you want to print: "))
    for i in range(1,y):
        x = 3.9 * x * (1 - x)
    print(x)
    
#Extra question 3e
def three_e():
    print("This program illustrates a chaotic function")
    x = float(input("What is your first number: "))
    y = float(input("What is your second number: "))
    for i in range(1,10):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print(x," & ", y)