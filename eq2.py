# // x-x2/2!+x3/3!-...

x = int(input("Enter x: "))
n = int(input("range: "))
sum = x
t = x

for i in range(1, n):
    t = -t * (x) / (i + 1)
    sum += t

print(f"Sum = {sum}")
