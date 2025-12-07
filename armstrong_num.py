n = int(input("Enter number: "))
length = len(str(n))

s = 0
num = n
for i in range(length):
    s += (num % 10) ** length
    num //= 10

if n == s:
    print(f'{n} is a armstrong number!')
else:
    print('no')