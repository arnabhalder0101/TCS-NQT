import math

n = int(input())
i = 1
while n > 0:
    prime = True
    if i == 1 or i == 2:
        prime = True

    else:
        for num in range(2, int(math.sqrt(i)) + 1):
            if i % num == 0:
                prime = False
                break

    if prime:
        print(i, end=" ")

    i += 1
    n -= 1
