# 1st 5 armstrong num --
nn = 100
c = 0


def isArm(n):
    s = 0
    num = n
    while num != 0:
        s += (num % 10) ** len(str(n))
        num = num // 10

    if n == s:
        return True
    else:
        return False


#
print("1st 20 Armstrong number: ")
while c != 5*3:
    if isArm(nn):
        print(nn)
        c += 1

    nn += 1

# print(isArm(153))

print("-- end --")
