a = [1,2,3,4,5,6,7,8,9,10]
sum = 0
prdct = 1
for i in range(len(a)):
    prdct *= a[i]
    sum += a[i]
print(sum)
print(prdct)

a = [1,0,3,0,5,0,7,0,9,0]
sum = 0
for i in a:
    sum += i
mean = sum / len(a)
for i in range(len(a)):
    if a[i] == 0:
        a[i] = mean
print(a)