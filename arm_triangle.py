n = 5

for i in range(n):
    ran1 = n - (i + 1)
    for j in range(ran1):
        print(" * ", end='')

    ran2 = i + 1
    for k in range(ran2):
        print(f' {k + 1} ', end='')

    ran3 = i
    for l in range(ran3):
        print(f' {i - l} ', end='')

    ran4 = n - (i + 1)
    for m in range(ran4):
        print(' * ', end='')

    print()

# *  *  *  *  1  *  *  *  *
# *  *  *  1  2  1  *  *  *
# *  *  1  2  3  2  1  *  *
# *  1  2  3  4  3  2  1  *
# 1  2  3  4  5  4  3  2  1
