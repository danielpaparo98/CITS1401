# Author: Daniel Paparo

# Question 1
# Not analysing a projects requirements will result in the program not meeting the specifications.
# Not designing the program means that the program wont follow best practices and wont make sense...

# Question 2
x = 'hello\'s'
print(x)

#Question 3
q3 = 'Hello \"Daniel\'s\"'
print(q3)

#Question 4
print("One line \nTwo Line!")

#Question 5
print("This is on ", end="")
print("the same line")

#Question 6
q6x = 'One string'
q6y = 'Two string'

print(q6x, q6y)

#Question 7
q7x, q7y = "Thing 1", "Thing 2"
print(q7x, q7y)
q7x, q7y = q7y, q7x
print(q7x, q7y)

#Question 8
def my_factorial():
    users_int = int(input("What number would you like to factorial-ize?"))
    fact = users_int

    for i in range(users_int -1):
        users_int -= 1
        fact *= (users_int)

    print(fact)

#Uncomment this to use
#my_factorial()

#Question 9
import math

print(math.sqrt(2.124))
print(math.factorial(23))

#Question 10
def myfutval():
    print("This program calculates the future value of a 10-year investment.")
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annual interest rate: "))
    years = int(input("Enter the number of years you want:"))
    for i in range(years):
        principal *= (1 + apr)
    print ("The value in 10 years is:", principal)

#Uncomment this to use
#myfutval()

#Question 11
def odd_integers(N):
    for i in range(N):
        if N % 2 != 0:
            if N % 5 != 0:
                print(N)
        N -= 1

#Uncomment this to use
#odd_integers(23)
#odd_integers(21243)
#odd_integers(22315233)

#Question 12
def odd_integers_errors(N):
    if isinstance(N, int):
        for i in range(N):
            if N % 2 != 0:
                if N % 5 != 0:
                    print(N)
            N -= 1
    else:
        print("Please only input values of integer type")

#Uncomment this to use
#odd_integers_errors(20)
#odd_integers_errors("daniel")
#odd_integers_errors(2.4)
