import math
x = int(input())
y = int(input())
a = math.cos(2*y)
b = math.sin(4*y)
c = math.exp(x)
d = math.exp(-x)
e = math.sqrt(c + d)
f = math.pow(e, 3)
g = math.pow(b+a-2, 2)
h = math.sqrt(a+b+e)
z = h / (f * g)
print(z)

input()