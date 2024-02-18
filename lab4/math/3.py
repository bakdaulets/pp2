import math
n = int(input("Input number of sides:"))
l = int(input("Input length of side:"))
cot = 1/math.tanh(180/n)
print("The area of the polygon is:", int((n * l**2 * cot)/4))