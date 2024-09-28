# 5+5+5+5 = 20
# 20+20+20 = 60
# 60+60 = 120
# 120

n = int(input())
ans = n
i = n - 1
while i > 0:
    sum_ = 0
    j = i
    while j > 0:
        sum_ += ans
        j -= 1
    ans = sum_
    i -= 1

print(ans)