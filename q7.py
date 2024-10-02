n = int(input())
n_str = str(n)
n_list = [int(n_str[i]) for i in range(len(n_str))]

max_ele = max(n_list)
min_ele = min(n_list)
print([max_ele, min_ele])
