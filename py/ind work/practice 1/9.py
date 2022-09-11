import math
a=float(input("Enter real num which contain 2 digits before and 2 digits after the coma: "))
b=a//1
c=a%1
b1=b/100 
c1=c*100 
num = c1+b1
print(num)