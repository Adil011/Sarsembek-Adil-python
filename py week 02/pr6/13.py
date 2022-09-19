a = [1,3,3,3,4,4,5,5,6,9,9]
b = []
b.append(a[0])
for i in range(1,len(a)):
    if a[i] in b:
        print("dublicate:", a[i], i)
    else:
        b.append(a[i])

a = [10,20,14,25,17,11,12,13]
print(a)
for i in range(8):
    if a[i] < 15:
        a[i] = a[i] * 2
print(a)
