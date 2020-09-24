#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2

print("I will solve an equation in the format ax + b = c")
print("You will enter the values for a, b and c")
a = input("Enter a:")
b = input("Enter b:")
c = input("Enter c:")

a = float(a)
b = float(b)
c = float(c)

x = (c - b)/a
print("\nThe solution for x is "+ str(x))