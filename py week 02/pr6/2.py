n = int(input())
a = [ int(input()) for i in range(n)]
min = a[0]
min_index = 0
for i in range(len(a)):
    if a[i] < min:
        min = a[i]
        min_index = i
print(min_index)

a = [-1,2,-3,4,-5,6,-7,8,-9,10]
scnd = []
thrd = []
for i in range (len(a)):
    if a[i] > 0:
        scnd.append(a[i])
    else:
        thrd.append(a[i])
print(scnd)
print(thrd)