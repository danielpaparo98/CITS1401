# Finds the greatest common divisor (GCD) using Euclid's algorithm

def Euclid(num1, num2):

    num1, num2 = int(num1), int(num2)
    #Error Handling
    if num2 > num1:
        num1,num2 = num2, num1
    while num2 is not 0:
        divisor = num1 % num2
        num1, num2 = num2, divisor
        
    print("The GCD is: ", num1)

Euclid(5,100)
Euclid(20,12)
Euclid(2.6, 412)
