#! python3
#
# Find the hypotenuse
# Your program will ask the user to enter in the 2 short sides of a right triangle.
# You will calculate the length of the hypotenuse and display the result.
# You will need to use the math module to use the command that finds the square root.
#
# Inputs:
# side, side
#
# Outputs:
# hypotenuse
#
# Test output
# input sides of 5 and 7 should give hypotenuse of 8.60232526704
import math

print("")
print("You will enter in 2 sides of a right triangle and I will calculate the hypotenuse")
a = input("Enter the length of one side:")
b = input("Now enter the length of another:")
a = float(a)
b = float(b)
c= math.sqrt(a**2 + b**2)
print("The hypotenuse is " + str(c))