a = "ArnabHalder".lower()
print(a[::-1])

d = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
print(d)

for char in a:
    # print(d[char])
    # x = d.get(char)
    # print(x)
    d[char] += 1
print(d)

for j in d:
    if d[j] != 0:
        print(j, ' : ', d.get(j))
