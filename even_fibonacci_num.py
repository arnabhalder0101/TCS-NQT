#!/bin/python3

import sys
# https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem?isFullScreen=true

def fibo(n, n1, n2):
    li_fib = [n1, n2]

    for i in range(n - 2):

        nn = n1 + n2

        if nn > n:
            break

        li_fib.append(nn)
        n1 = n2
        n2 = nn

    s = sum(i for i in li_fib if i % 2 == 0)

    return s


t = int(input().strip())

list_ = []

for a0 in range(t):
    n = int(input().strip())
    list_.append(fibo(n, 1, 2))

for i in range(t):
    print(list_[i])
