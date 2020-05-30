import hashlib
import random

MAX_EVEN = 65536


def mod_mul(a, b, mod):
    res = 0
    a = a % mod
    while b:
        if (b & 1):
            res = (res + a) % mod
        a = (2 * a) % mod
        b >>= 1
    return res


# def mod_pow(base, exp, mod):
#     res = 1
#     base = base % mod
#     if base == 0:
#         return 0
#     while exp > 0:
#         if (exp & 1) == 1:
#             res = mod_mul(res, base, mod)
#         exp = exp >> 1
#         base = mod_mul(base, base, mod)
#     return res

def mod_pow(x, n, m):
    res = 1
    while n:
        if n % 2:
            res = res * x % m
        x = (x ** 2) % m
        n = n // 2
    return res


def euler(p, q):
    return (p - 1) * (q - 1)


# def egcd(a, b):
#     if a == 0:
#         return (b, 0, 1)
#     else:
#         g, y, x = egcd(b % a, a)
#         return (g, x - (b // a) * y, y)

def egcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = egcd(b, a % b)
        return d, y, x - y * (a // b)


def modinv(num, mod):
    g, x, y = egcd(num, mod)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % mod


def gen(q):
    while True:
        R = random.randint(1, MAX_EVEN) * 2
        p = q * R + 1
        if not (mod_pow(2, q * R, p) != 1 or mod_pow(2, R, p) == 1):
            break
    g = 1
    while g == 1:
        x = random.randint(1, p - 1)
        g = mod_pow(x, R, p)
    print('x:', x)
    print('g:', g)
    d = random.randint(1, q - 1)
    e = mod_pow(g, d, p)
    return p, q, g, e, d


def hash_msg(message):
    hash = hashlib.sha256()
    hash.update(message.encode())
    return int(hash.hexdigest(), 16)


def sign(p, q, g, d, message):
    m = hash_msg(message)
    k = random.randint(1, q - 1)
    r = mod_pow(g, k, p)
    inv_k = modinv(k, q)
    s = (inv_k * (m - d * r)) % q
    return r, s


def verify(p, q, g, e, message, r, s):
    if r < 0 or r > p or s < 0 or s > q:
        return False
    m = hash_msg(message)
    return mod_mul(mod_pow(e, r, p), mod_pow(r, s, p), p) == mod_pow(g, m, p)


# q = 97017021638387687521542127312722178904352834655752299660760969612789439451381
# message = 'Я, Владислав Казимиров, люблю МиКОЗИ'

q = 112971461064154869310834029706569828562173472410416149342082034001846987882313
message = 'Я, Глеб Казачинский, люблю МиКОЗИ'

p, q, g, e, d = gen(q)
r, s = sign(p, q, g, d, message)
print(verify(p, q, g, e, message, r, s))
