s1 = str(input('text: '))
i = []
count = 0
for char in s1:
    count += 1
    if char == '"':
                i.append(count)
s1 = s1[i[0]:i[1] - 1]
print(s1)