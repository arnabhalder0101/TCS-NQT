n = int(input("Enter: "))
for i in range(n+1):
    ran = i+1
    for j in range(ran):
        print(' * ', end="")
    print()


# reverse

for i in range(n):
    ran = n-i
    for j in range(ran):
        print(' * ', end='')
    print()
