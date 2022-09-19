s = str(input('Enter a string: '))
r = 0
while s.find('t') != -1:
    s = s.replace('t', '', 1)
    r += 1
print(r)