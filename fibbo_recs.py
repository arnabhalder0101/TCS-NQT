# 0 1 1 2 3 5 8 13 21...

num = 15


def fibbo(n, a=0, b=1):
    if n == 0:
        return
    print(a, end=' ')
    return fibbo(n - 1, a=b, b=a + b)


fibbo(num, 0, 1)


def sunFibo(num):
    
    return sunFibo(num)+sunFibo(num+1)
