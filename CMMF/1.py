import numpy as np


def f_func(x):
    return (np.sin(x)) ** 2


def k_func(x):
    return (np.cos(x)) ** 2 + 1


def q_func(x):
    return 1


N, h, ae_0, g_0, ae_1, g_1 = 10, 1 / 10, 1, 0, 1, 1
x, k, q, f, C, F, A, B = [], [], [], [], [], [], [], []

for i in range(0, N + 1):
    x.append(i * h)
    k.append(k_func(x[i]))
    q.append(q_func(x[i]))
    f.append(f_func(x[i]))
    C.append(2 * k[i] + h * h * q[i])
    F.append(f[i] * h * h)

R = h * ae_0 + h * h * q[0] / 2 - h * h * (-2 * np.sin(x[0]) * np.cos(x[0])) * ae_0 / (2 * k[0]) + k[0]
O_1 = k[0] / R
W1 = (h * g_0 + h * h * f[0] / 2 - h * h * (-2 * np.sin(x[0]) * np.cos(x[0])) * g_0 / (2 * k[0])) / R
Q = h * ae_1 + h * h * q[N] / 2 + h * h * (-2 * np.sin(x[0]) * np.cos(x[0])) * ae_1 / (2 * k[N]) + k[N]
O_2 = k[N] / Q
W2 = (h * g_1 + h * h * f[N] / 2 + h * h * (-2 * np.sin(x[0]) * np.cos(x[0])) * g_1 / (2 * k[N])) / Q

A.append(0)
B.append(O_1)
for i in range(1, N):
    A.append(k[i] - (k[i + 1] - k[i - 1]) / 4)
    B.append(k[i] + (k[i + 1] - k[i - 1]) / 4)

A.append(O_2)
B.append(0)
C[0], F[0], C[N], F[N] = 1, W1, 1, W2

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
