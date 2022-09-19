n = int(input())
D = [ int(input()) for i in range(n)]
sum = 0
for i in range(1,n,2):
    sum += D[i]
print(D)
print(sum)

a = [10,20,14,25,17,11,12,13]
print(a)
for i in range(8):
    if a[i] < 15:
        a[i] = a[i] * 2
print(a)