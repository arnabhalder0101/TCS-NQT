a = list(map(int, input().split()))
add_ = []


def is_even_combo(li):
    s = 0
    for i in range(len(li)):
        s += li[i]
    if s % 2 == 0:
        return True
    else:
        return False


for i in range(len(a)):
    for j in range(i + 1, len(a)):
        li = [a[i], a[j]]
        if is_even_combo(li) and (li not in add_):
            add_.append(li)

print(add_)
print(len(add_))
