name = input()

n1 = name.split()
# print(n1)
new = ''
for i in range(len(n1)-1):
    new += n1[i][0]
    new += ". "

new += n1[len(n1)-1]
print(new)