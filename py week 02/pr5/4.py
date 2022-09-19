s= str(input())
r = 0
while s.find('a') != -1:
    s = s.replace('a', 'o', 1)
    r += 1
print(s)
print(r)
print(len(s))