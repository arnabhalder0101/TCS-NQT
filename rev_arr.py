arr = list(map(int, input().split()))

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
print(arr)

for i in range(len(arr)//2):
    # k = arr[i]
    # arr[i] = arr[len(arr)-(i+1)]
    # arr[len(arr)-(i+1)] = k
    arr[i], arr[len(arr)-(i+1)] = arr[len(arr)-(i+1)], arr[i]


print(arr)