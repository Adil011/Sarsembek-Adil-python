a = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(a)):
    print(a[i],-a[i])

a = [1,1,3,4,5,3,3,9,9,9]
b = []
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
print(b)