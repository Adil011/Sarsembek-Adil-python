#1.1 

import random
N=int(input("Enter n: "))
A=[[random.randrange(10) for i in range(N)] for j in range(N)]
print(A)
summ = 0
count= 0
for i in range(len(A) - 1):
    for j in range(i + 1, len(A[i])):
        if A[i][j] > 0:
            summ += A[i][j]
            count += 1
print("Sum of positive numbs: ", summ)
print("Count of pos. numbs: ", count)

#1.2
import random
N = int(input())
M = int(input())
B = [[random.randrange(10) for i in range(M)] for j in range(N)]
for i in B:
    for j in i:
        print(j, end=" ")
    print()
for i, row in enumerate(B):
    max = min = 0
    for j, elem in enumerate(row):
        if elem > row[max]:
            max = j
        if elem < row[min]:
            min = j
    row[max], row[0] = row[0], row[max]
    row[min], row[-1] = row[-1], row[min]
print(B)

#2.1
N = 3
A = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]

s = 0
for i in range(N):
    s += A[0][i]

b = "YES"
for i in range(N):
    s1 = 0
    s2 = 0
    for j in range(N):
        s1 += A[i][j]
        s2 += A[j][i]
    if s1 != s or s2 != s:
        b = "NO"
        break

print(b)


#2.2
N = 3
M = 4

A = [[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]
print("Current matrix: ")
for i in A:
    for j in i:
        print(j, end=" ")
    print()
print()

for i in range(N):
    tmp = A[i][0]
    A[i][0] = A[i][M-1]
    A[i][M-1] = tmp

for i in range(N):
    for j in range(M):
        print("%2d " % A[i][j], end='')
    print()
    
#3.1

N = 3
A = [[1, 2, 3],[2, 5, 6],[3, 6, 4]]
b = "YES"
for i in range(N):
    for j in range(N):
        if A[i][j] != A[j][i]:
            b = "NO"
            break
print(b)

#3.2
from random import randint
 
a = [[randint(10, 99) for i in range(9)] for j in range(7)]
for row in a:
    print(*map('{:2d}'.format, row))
print()
 
max_elem = a[0][0]
ie = je = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] > max_elem:
            max_elem = a[i][j]
            ie = i 
            je = j 
a[0], a[ie] = a[ie], a[0]
a[0][0], a[0][je] = a[0][je], a[0][0]
for row in a:
    print(*map('{:2d}'.format, row))

#4.1

from random import randint
size = int(input('Array size: '))
matrix = [[randint(1,99) for x in range(size)] for _ in range(size)]

for i in range (size): print(*matrix[i])

maxsum=[0]*size
for i in range (size): maxsum[i]=sum(matrix[i])
print (f'MAX row {maxsum.index(max(maxsum))+1} sum {max(maxsum)}')
print (f'MIN row {maxsum.index(min(maxsum))+1} sum {min(maxsum)}')


#4.2
a = [[1,2,-3],[-1,2,3],[1,-2,3]]
for i in a:
    for j in i:
        print(j, end=" ")
    print()
print()
a = [[1 if x>0 else 0 for x in i] for i in a]
for i in range(len(a)):
    print(*[a[i][x] if x<=i else '' for x in range(len(a[i]))],'')

#5.1

import random
n=int(input("Enter size: "))
m=int(input("Enter size 2: "))
a=[[random.randrange(10) for i in range(n)] for j in range(m)]
print(list(map(sorted, a)))

def qsort(a): 
    if len(a) <= 1:
        return a
    else:
        return qsort( [x for x in a[1:] if x < a[0]]) + [a[0]] + qsort([x for x in a[1:] if x >= a[0]] )
qsort(a)

#6.1

import random
n=int(input("Enter n: "))
m=n
a=[[random.randrange(10) for i in range(n)] for j in range(m)]
for i in a:
    for j in i:
        print(j, end=" ")
    print()
print()

for i in range(n):
    print(a[i],max(a[i]))
for i in range(m):  
    x=[x[i] for x in a]
    print(min(x), end=" ")


#6.2
import random
n=int(input("Enter n: "))
arr=[[random.randrange(10) for i in range(n)] for j in range(n)]
for i in arr:
    print(i)
print()
 
a = sum(arr, [])
max1 = max(a[::n+1])
max2 = max(a[n-1::n-1][:n])
if max1 > max2:
    i1 = j1 = a[::n+1].index(max1)
else:
    i1 = a[n-1::n-1][:n].index(max2)
    j1 = n - 1 - i1
arr[n//2][n//2], arr[i1][j1] = arr[i1][j1], arr[n//2][n//2]
 
for i in arr:
    print(i)

