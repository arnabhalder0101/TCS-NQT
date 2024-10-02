arr = [1, 20, 33, 4, 52, 61, 744, 48, 19, 10]
target = int(input())
arr.sort()
beg = 0
end = len(arr) - 1
found = False
while not found:
    if target in arr:
        index = (beg + end) // 2
        if arr[index] == target:
            found = True
            print("Array: ", arr)
            print(f'Target {target} element found at {index + 1} position')
            break
        elif target > arr[index]:
            beg = index + 1
        elif target < arr[index]:
            end = index - 1
    else:
        print("Not Present")
        found = False
        break

    print(beg, end)
