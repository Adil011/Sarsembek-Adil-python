a = [1,2,3,4,5,6,7,8,9,10]
sum = 0
prdct = 1
for i in range(len(a)):
  if a[i] % 2 != 0:
     prdct *= a[i]
  else:
      sum += a[i]
print(sum)
print(prdct)

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
