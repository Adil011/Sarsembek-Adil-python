s1 = str(input('text: '))
s2 = s1.split()
t = list()
for i in s2:
    t = list(i)
    t[0] = t[0].upper()
    print("".join(t))