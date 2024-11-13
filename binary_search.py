arr = [1, 3, 6, 2, 6, 7, 99, 44]

arr.sort()
print(arr)

ele = int(input("Enter search element"))
beg = 0
end = len(arr)-1
mid = (beg+end) // 2

found = False

while not found:
    if ele in arr:
        if ele == arr[mid]:
            found = True
            print('Element found at ', mid+1)
            break
        elif ele < arr[mid]:
            end = arr.index(arr[mid])+1
            mid = (beg+end)//2
        elif ele > arr[mid]:
            beg = arr.index(arr[mid])+1
            mid = (beg+end)//2
    else:
        print("Not present")
        break


