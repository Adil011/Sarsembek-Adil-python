s1 = str(input('text: '))
s2 = s1.split()
t = list()
for i in s2:
    t = list(i)
    if t[len(t) - 1] == 'I':
        print(i)