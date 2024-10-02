n = int(input())
arr = list(map(int, input().split()))

for i in range(len(arr)):
    if 0 == arr[i]:
        arr.pop(i)
        arr.insert(len(arr), 0)

print(arr)