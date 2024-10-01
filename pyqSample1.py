n = int(input())
li = []

for i in range(n):
    li.append(int(input()))
    
s = 0

while len(li) > 1:
    li.sort(reverse=True)
    l_sum = sum(li[-2:])
    li.pop(len(li) - 1)
    li.pop(len(li) - 1)
    li.append(l_sum)
    s += l_sum

print(s)
