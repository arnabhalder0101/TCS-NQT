s = input("enter string: ").lower()
l = []
for i in range(len(s)):
    l.append(s[i])
u_l = list(set(l))

d = {u_l[i]: 0 for i in range(len(u_l))}

print(u_l)
print(d)

for j in range(len(u_l)):
    for k in range(len(s)):
        if u_l[j] == s[k]:
            d[u_l[j]] += 1

print(d)
