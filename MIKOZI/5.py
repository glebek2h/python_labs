import random
import hashlib


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


def gen(q):
    while True:
        R = random.randint(0, 4 * (q + 1))
        R += R % 2
        p = R * q + 1
        if not (fast_p(2, q * R, p) != 1 or fast_p(2, R, p) == 1):
            print('R :', R)
            print('p :', p)
            break
    g = 1
    while g == 1:
        x = random.randint(1, p - 1)
        g = fast_p(x, R, p)
    print('x:', x)
    print('g:', g)
    d = random.randint(1, q - 1)
    e = fast_p(g, d, p)
    return p, q, g, e, d


def hash(m):
    hash_ = hashlib.sha256()
    hash_.update(m.encode())
    return int(hash_.hexdigest(), 16)


def sign(p, q, g, d, M):
    m = hash(M)
    k = random.randint(1, q - 1)
    r = fast_p(g, k, p)
    gcd, x, y = gcdex(k, q)
    k_ex = x % q
    s = (k_ex * (m - d * r)) % q
    return r, s


def verify(p, q, g, e, M, r, s):
    if s < 0 or s > q or r > p or r < 0:
        return False
    m = hash(M)
    return (fast_p(e, r, p) * fast_p(r, s, p)) % p == fast_p(g, m, p)


q = 112971461064154869310834029706569828562173472410416149342082034001846987882313
M = 'Я, Глеб Казачинский, люблю МиКОЗИ'

p, q, g, e, d = gen(q)

r, s = sign(p, q, g, d, M)

print(verify(p, q, g, e, M, r, s))
