x = int(input())
n = int(input())
t = x
s = x

N = 3
while n > 0:
    t = (-t) * (x * x) / (N * (N - 1))
    s += t

    N += 2
    n -= 1

print(s)
