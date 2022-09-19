s = str(input())
r = 0
while s.find(':') != -1:
    s = s.replace(':', '%', 1)
    r += 1
print(s)
print(r)