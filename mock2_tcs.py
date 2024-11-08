n = int(input())

arr = []
for i in range(n):
    l = list(map(int, input().split()))
    arr.append(l)

for i in range(n):
    for j in range(n):
        if j >= i + 1:
            arr[i][j] = 0

print(arr)

