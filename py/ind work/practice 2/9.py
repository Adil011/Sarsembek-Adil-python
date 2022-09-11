import math
x = 0.8
y = 0.1
z = 4
b = 1 - x + math.atan(x-7*y)
c = 4 * x * z - math.pow(math.log10(x), 2)
g = b / c
a = pow(g, (1/5))
print(a)

input()
