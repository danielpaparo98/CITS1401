import math

def material():
    radius = float(input("Please insert the radius in meters "))
    cost = float(input("What is the cost per cubic meter "))

    area = 4* math.pi * radius * radius

    print("The cost of area:", area, "is: ", area * cost)

material()