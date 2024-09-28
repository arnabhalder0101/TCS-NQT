v = 'aeiou'
s = input()

for i in range(len(v)):
    out = ''
    for j in range(len(s)):
        if v[i] != s[j]:
            out += s[j]
    s = out


print(s)