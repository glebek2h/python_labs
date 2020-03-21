import numpy as np
import scipy.linalg as scpl
import time
import pandas as pd
from matplotlib import pyplot as plt


def get_degree_of_2(n):
    degree = 0
    while n >= 2:
        n /= 2
        degree += 1
    return degree


def w(n, m):
    return np.exp((-2 * m * np.pi / n) * 1j)


def w_inv(n, m):
    return np.exp((2 * m * np.pi / n) * 1j)


def fft(x, is_inverse=False):
    t = get_degree_of_2(len(x))
    y = np.array(x[bit_reverse(len(x))], dtype=complex)
    for q in range(t):
        y = mul_A_B(y, q + 1, is_inverse)
    if is_inverse:
        y /= len(y)
    return y


def truefft(x):
    return np.fft.fft(x)


def mul_A_B(y, q, is_inverse):
    L = 2 ** q
    y1 = y.copy()
    for i in range(0, len(y), L):
        y2 = y[i:i + L]
        y3 = y2.copy()
        if not is_inverse:
            for j in range(len(y2) // 2):
                y3[j] = y2[j] + w(len(y2), j) * complex(y2[len(y2) // 2 + j])
            for j in range(len(y2) // 2, len(y2)):
                y3[j] = y2[j - len(y2) // 2] - w(len(y2), j - len(y2) // 2) * complex(y2[j])
        else:
            for j in range(len(y2) // 2):
                y3[j] = y2[j] + w_inv(len(y2), j) * complex(y2[len(y2) // 2 + j])
            for j in range(len(y2) // 2, len(y2)):
                y3[j] = y2[j - len(y2) // 2] - w_inv(len(y2), j - len(y2) // 2) * complex(y2[j])
        y1[i:i + L] = y3
    return y1


def bit_reverse(n):
    reshuffle = []
    bit_length = get_degree_of_2(n)
    for num in range(n):
        size = bit_length - 1
        reversed_num = 0
        while num > 0:
            k = num % 2
            num //= 2
            reversed_num += k << size
            size -= 1
        reshuffle.append(reversed_num)
    return reshuffle


t_y = []
t_z = []
eps_arr = []
delta_arr = []
for k in range(16):
    n = 2 ** k
    x_n = (np.random.rand(n) + np.random.rand(n) * 1j)

    start_time = time.time()
    y_n = fft(x_n)
    t_y.append((time.time() - start_time) * 1000)

    x_n_inv = fft(y_n, True)

    start_time = time.time()
    z_n = truefft(x_n)
    t_z.append((time.time() - start_time) * 1000)

    eps = scpl.norm(x_n - x_n_inv)
    delta = scpl.norm(y_n - z_n)
    delta_arr.append(delta)
    eps_arr.append(eps)
    if n == 8:
        print('x_8:', x_n)
        print('x_8_inv:', x_n_inv)
        print('y_8:', y_n)
        print('z_8:', z_n)
        print('eps_8:', eps)
        print('delta_8:', delta)

plt.figure()
plt.scatter(range(1, 17), t_z, color='green')
plt.scatter(range(1, 17), t_y, color='yellow')
plt.xlabel('k')
plt.ylabel('time(ms)')
plt.legend(['fft', 'truefft'])
plt.show()

print(pd.DataFrame(dict(k=range(1, 17), t_y=t_y, t_z=t_z, eps=eps_arr, delta=delta_arr)))
