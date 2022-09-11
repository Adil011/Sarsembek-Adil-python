import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
 
D = b ** 2 - 4 * a * c
print("D = " % D)
 
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("x1 = ", x1)
    print("x1 = ", x2)
    input()
elif D == 0:
    x = -b / (2 * a)
    print("x = " % x)
    input()
else:
    print("No solution")
    input()