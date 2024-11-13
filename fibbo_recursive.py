n = int(input("Enter Number : "))


def Fibbo(n):
    if n <= 1:
        return n
    else:
        return Fibbo(n - 1) + Fibbo(n - 2)


for i in range(n):
    print(Fibbo(i), end=' ')
