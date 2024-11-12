n = int(input("Enter: "))

for i in range(n):
    ran = n - i
    for j in range(ran):
        print('   ', end='')

    ran1 = i + 1
    for k in range(ran1):
        print(' * ', end='')

    # print(' * '*(n+1), end='')

    if i > 0:
        ran2 = i
        for l in range(ran2):
            print(' * ', end='')

    print()
