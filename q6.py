i = int(input("T: "))
while i > 0:
    n = int(input("N: "))

    # n_str = str(n)
    #
    # sum_n = sum(int(n_str[i]) for i in range(len(n_str)))
    # # print(sum_n)
    #
    # if n % sum_n == 0:
    #     print("Good Number")
    # else:
    #     print("Bad Number")

    s = 0
    num = n
    while (num != 0):
        s += num % 10
        num = num // 10
    # print(s)
    if n % s == 0:
        print("good number")
    else:
        print("bad number")

    i -= 1
