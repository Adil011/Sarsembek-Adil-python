a = [ int(input()) for i in range(10)]
sum = 0
for i in range(len(a)):
    if a[i] > 5:
        sum += a[i]