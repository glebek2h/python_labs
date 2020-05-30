def gcdex(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcdex(b, a % b)
        return d, y, x - y * (a // b)


def fast_p(x, n, m):
    res = 1
    while n:
        if n % 2:
            res = res * x % m
        x = (x ** 2) % m
        n = n // 2
    return res


p = 148250911826341
q = 202614773351219
e = 12776470783322290155855389671
X1 = 26926695734432769312536758139
Y2 = 7060854756795018940042464563

n = p * q
fi = (p - 1) * (q - 1)

gcd, x, y = gcdex(e, fi)

d = 0
if gcd == 1:
    d = x % fi
    print('d: ', d)

Y1 = fast_p(X1, e, n)
print('Y1: ', Y1)

X1_ = fast_p(Y1, d, n)
print('X1_: ', X1_)
print('X1 - X1_ :', X1 - X1_)


X2 = fast_p(Y2, d, n)
print('X2: ', X2)
