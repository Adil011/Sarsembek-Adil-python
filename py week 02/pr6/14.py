a = [1,-200,3,4,5,600,7,8,9]
max = a[0]
max_index = 0
min = a[0]
min_index = 0
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
        max_index = i
    if a[i] < min:
        min = a[i]
        min_index = i
a[min_index] = max
a[max_index] = min
print(a)

n = int(input())
a = [ int(input()) for i in range(n)]
sum = 0
for i in a:
    sum += i
mean = sum / len(a)
for i in range(len(a)):
    if a[i] > mean:
        a[i] = 1
print(a)
