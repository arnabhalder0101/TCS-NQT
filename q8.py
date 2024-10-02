s1 = input().lower()
s2 = input().lower()

l = []
for i in range(len(s1)):
    if s1[i] == s2:
        l.append(i)


print({l[0], l[len(l) - 1]})
