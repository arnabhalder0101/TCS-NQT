# l = [[0, 1, 1, 1], [0, 1, 0, 1], [0, 0, 0, 0], [1, 1, 1, 1]]
l = [[0, 1, 1, 1], [1, 1, 0, 1], [0, 0, 1, 0], [1, 1, 0, 1]]

l_count = []
for i in range(len(l)):
    c = 0
    for j in range(len(l[i])):
        if l[i][j] == 1:
            c += 1
    l_count.append(c)

max_1 = max(l_count)
# print(l_count.index(max_1))
i = 0
while max_1 != l_count[i]:
    i += 1

print("Ans", i)
