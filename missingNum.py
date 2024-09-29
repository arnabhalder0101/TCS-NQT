n = int(input())
arr = list(map(int, input().split()))
missing = 0
for i in range(n):

    if (i+1) not in arr:
        missing = i+1
        break

print(missing)

