import math

l = input()
r = int(math.sqrt(len(l)))
c = int(math.sqrt(len(l)))

s = 0
index = 0
u_l = []

# print(r, c)

for i in range(r):
    li = []
    for j in range(c):
        li.append(l[index])
        index = index + 1

    u_l.append(li)

for i in range(r):
    for j in range(c):
        print(u_l[j][i], end="")
    print(end="")

