s = str(input())
t = s.split()
r = 0
while True:
    if t[r][len(t[r]) - 1] == '.':
        break
    else:
        r += 1
print(r)