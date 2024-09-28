s1 = input()
s2 = input()
count = 0
for i in range(len(s2)):
    for j in range(len(s1)):
        if s2[i] == s1[j]:
            count += 1

print(count)