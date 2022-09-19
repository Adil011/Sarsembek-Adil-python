s1 = str(input('text: '))
s2 = s1.split()
for i in s2:
    if i[len(i) - 1] == 'i':
        if i[0] == 'a':
            print(i)