# // x-x2/2!+x3/3!-...
print('Enter: ')

x = int(input())
n = int(input())
t = x
s = x
N = 2
while n > 0:
    t = -t * x / N
    s += t
    n -= 1
    N += 1
print(s)
