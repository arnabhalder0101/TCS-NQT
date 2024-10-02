s1 = input()
s2 = input()

s22 = set(i for i in s2)
s11 = set(i for i in s1)

out = ''

for i in range(len(s1)):
    if s1[i] not in s2:
        out += s1[i]

for j in range(len(s2)):
    if s2[j] not in s1:
        out += s2[j]

out = list(set(i for i in out))
out.sort()
print("".join(out))
