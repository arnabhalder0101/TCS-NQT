n = int(input(f"enter n "))
k = int(input(f"enter k "))
l = []

for m in range(n):
    l.append(int(input(f"enter value {m} ")))

l1 = []


def possibleCombos(list1):
    length = len(list1)-1
    for i in range(length):
        runTime = len(list1)
        for j in range(1, runTime):
            if list1[i] + list1[j] >= k:
                l1.append([list1[i], list1[j]])
        list1.remove(list1[0])
        length = len(list1)-1


possibleCombos(l)
print(l1)
