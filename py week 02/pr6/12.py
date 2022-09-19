n = int(input())
a = [ int(input()) for i in range(n)]
mn = 9999999999
for i in range(len(a)):
    if a[i] % 2 == 1 and a[i] < mn:
        mn = a[i]
print(mn)

a = [1,2,3,4,5,6,7,8,9,10]
b = [10,9,8,7,6,5,4,3,2,1]
print(a)
print(b)
a,b = b,a
print(a)
print(b)
