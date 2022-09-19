s = str(input())
for letters in s:
    if ord(letters) > 64 and ord(letters) < 91:
        s = s.replace(letters, chr(ord(letters)+32))
print(s)