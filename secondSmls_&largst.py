arr = list(set(map(int, input().split())))

arr.sort()

if len(arr) > 1:
    print('Second Smallest ', arr[1], 'Second Largest', arr[len(arr) - 2])
else:
    print(0)
