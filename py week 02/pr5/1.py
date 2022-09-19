s = str(input())
t = s.split()
r = 0
for words in t:
    if words[0] == 'е' or words[0] == 'Е':
        r += 1
print(r)