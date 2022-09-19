s = str(input())
r = 0
while s.find('a') != -1:
    s = s.replace('a', '', 1)
    r += 1
print(s)
print(r)