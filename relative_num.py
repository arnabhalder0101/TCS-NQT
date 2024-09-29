n = int(input())

n1 = n


def fact(n):
    res = 1
    num = n
    for i in range(n):
        res *= num
        num -= 1
    return res


s = 0
for i in range(len(str(n))):
    num = n1 % 10
    n1 = n1 // 10
    s += fact(num)

if s == n:
    print(1)
else:
    print(0)
