s = input().replace(" ", '').lower()

d = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
d_v = {chr(i): 0 for i in range()}

for i in range(len(s)):
    if s[i] in list(d.keys()):
        d[s[i]] += 1


print(d)
