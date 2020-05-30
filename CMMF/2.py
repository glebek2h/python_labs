import numpy as np


def f_func(x):
    return (np.sin(x)) ** 2


def k_func(x):
    return 1 / ((np.cos(x)) ** 2 + 1)


def q_func(x):
    return 1


def integr(predicate, a, b):
    count = 5000
    integral, step = 0, (b - a) / count
    for i in range(1, count + 1):
        integral += step * predicate(a + (i - 1) * step)
    return integral


N, h, ae_0, g_0, ae_1, g_1 = 10, 1 / 10, 1, 0, 1, 1
x, a, d, fi, C, F, A, B = [], [], [], [], [], [], [], []

for i in range(0, N + 1):
    x.append(i * h)
    a.append(1 / ((1 / h) * integr(lambda x1: k_func(x1), x[i - 1], x[i])))
    d.append((1 / h) * integr(lambda x1: q_func(x1), x[i] - h / 2, x[i] + h / 2))
    fi.append((1 / h) * integr(lambda x1: f_func(x1), x[i] - h / 2, x[i] + h / 2))
    A.append(a[i])

d[0] = (2 / h) * integr(lambda x1: q_func(x1), 0, h / 2)
fi[0] = (2 / h) * integr(lambda x1: f_func(x1), 0, h / 2)
d[N] = (2 / h) * integr(lambda x1: q_func(x1), 1 - h / 2, 1)
fi[N] = (2 / h) * integr(lambda x1: f_func(x1), 1 - h / 2, 1)

R = h * ae_0 + h * h * d[0] / 2 + a[1]
O_1 = a[1] / R
W1 = (h * g_0 + h * h * fi[0] / 2) / R
Q = h * ae_1 + h * h * d[N] / 2 + a[N]
O_2 = a[N] / Q
W2 = (h * g_1 + h * h * fi[N] / 2) / Q

C.append(1)
B.append(O_1)
F.append(W1)
for i in range(1, N):
    C.append(a[i + 1] + a[i] + d[i] * h * h)
    B.append(a[i + 1])
    F.append(fi[i] * h * h)

A[0] = 0
A[N] = O_2
C.append(1)
B.append(0)
F.append(W2)

alfa, beta, y = np.zeros(N + 1), np.zeros(N + 1), np.zeros(N + 1)
alfa[1], beta[1] = O_1, W1

for i in range(1, N):
    alfa[i + 1] = B[i] / (C[i] - alfa[i] * A[i])
    beta[i + 1] = (F[i] + beta[i] * A[i]) / (C[i] - alfa[i] * A[i])

y[N] = (W2 + O_2 * beta[N]) / (1 - alfa[N] * O_2)

for i in range(N - 1, -1, -1):
    y[i] = alfa[i + 1] * y[i + 1] + beta[i + 1]

for i in range(0, N + 1):
    print("u(", x[i], ") = ", y[i])
