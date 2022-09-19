a = [1,3,3,3,4,4,5,5,6,9,9]
b = []
b.append(a[0])
for i in range(1,len(a)):
    if a[i] in b:
        print("dublicate:", a[i], i)
    else:
        b.append(a[i])

a = [1,2,3,4,5,6,7,8,9,10]
b = []
for i in range(len(a)):
    if a[i] % 2 == 1:
        b.append(a[i])

if len(b) == 0:
    print("no such numbers")
else:
    b.sort()
    print(b[::-1])