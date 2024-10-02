s1 = input()
s2 = input()

str12 = s1 + s2
l = []

for i in range(len(str12)):
    l.append(str12[i])

s = list(set(l))
# print("".join(s))
out = ''
print(s)
for i in range(len(s)):
    c = 0
    for j in range(len(str12)):
        if s[i] == str12[j]:
            c += 1

    if c == 1:
        out += s[i]


print(out)