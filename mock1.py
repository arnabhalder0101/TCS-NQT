n = int(input())

mat = []

for i in range(n):
    l = list(map(int, input().split()))
    mat.append(l)

index = 0
for j in range(n):
    for k in range(n):
        if (k > index):
            mat[j][k] = 0
    index += 1

print(mat)

