# x-x3/3!+x5/5!-....

n = int(input("enter range: "))
x = int(input("Enter X: "))
sum = x
t = x
for i in range(1, n):
    t = (-t)*(x*x)/((2*i)*(2*i+1))
    sum += t

print(f"Sum: {sum} for x = {x} within range of {n}")

