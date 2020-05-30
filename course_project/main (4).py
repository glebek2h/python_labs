import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pylab
from mpl_toolkits.mplot3d import Axes3D


def draw(x, y, v, z_0, min_E_index):
    X, Y = np.meshgrid(x, y)
    Z = v[:(len(x) * len(y)), min_E_index].reshape((len(x), len(x)))
    fig, ax = plt.subplots()
    cs = ax.contour(X, Y, Z)
    ax.clabel(cs, inline=1, fontsize=10)
    plt.ylabel(f"v_[:, {min_E_index}]")
    fig.colorbar(cs)
    fig = pylab.figure()
    cs = Axes3D(fig)
    cs.plot_surface(X, Y, Z)
    cs.set_xlabel("x")
    cs.set_ylabel("y")
    cs.set_zlabel(f"v_[:, {min_E_index}]")
    cs.set_title(f"z_0={z_0}")
    pylab.show()


def k_(i, j, N, M):
    if j == 0 or i == N or j == M:
        return -1  # сработало одно из 1-ых 3-ёх граничных условий
    if i == 0:
        return j - 1  # сработало 4-ое граничное условие
        # M - 2 - кол-во столбцов в заполняемой матрице
    return (i - 1) * (M - 2) + j - 1  # не соответсвует ни одному из граничных условий


def a_1(t):
    return - 1 / (t ** 2)


def a_2(t, h, i, j, z_0, eps=11.4, eps2=3.8):
    return - (- 2 / (t ** 2) - 2 / (h ** 2) + 2 / np.sqrt((i * h) ** 2 + (z_0 - j * t) ** 2) + 2 / np.sqrt(
        (i * h) ** 2 + (z_0 + j * t) ** 2) * ((eps - eps2)/(eps + eps2)))


def a_3(t):
    return - 1 / (t ** 2)


def a_4(h, i):
    return - (1 / (h ** 2) + 1 / (i * h * 2 * h))


def a_5(h, i):
    return - (1 / (h ** 2) - 1 / (i * h * 2 * h))


def solve(x0, xn, N, y0, ym, M, E, e, eps_0, z_0, m_, h_, g1=0, g2=0, g3=0, g4=0):
    # x0 - начальная координата области решения по оси х;
    # xn - конечная координата области решения по оси х;
    # y0 - начальная координата области решения по оси y;
    # ym - конечная координата области решения по оси y;
    # N  - число точек координатной сетки вдоль оси х;
    # M  - число точек координатной сетки вдоль оси y;
    # f  - функция в правой части уравнения

    x = np.arange(x0 + (xn - x0) / N, xn, (xn - x0) / N)
    h = x[1] - x[0]
    y = np.arange(y0 + (ym - y0) / M, ym, (ym - y0) / M)
    t = y[1] - y[0]

    a = np.zeros(((N - 1) * (M - 1), (N - 1) * (M - 1)), dtype=float)

    for i in range(1, N):
        for j in range(1, M):
            k_row = k_(i, j, N, M)
            k_1 = k_(i, j + 1, N, M)
            k_2 = k_row
            k_3 = k_(i, j - 1, N, M)
            k_4 = k_(i + 1, j, N, M)
            k_5 = k_(i - 1, j, N, M)
            if k_1 != -1:
                a[k_row][k_1] = a_1(t)
            if k_2 != -1:
                a[k_row][k_2] += a_2(t, h, i, j, z_0)  # Здесь и далее пишем '+=', т.к может совпасть индекс столбцов
            if k_3 != -1:
                a[k_row][k_3] += a_3(t)
            if k_4 != -1:
                a[k_row][k_4] += a_4(h, i)
            if k_5 != -1:
                a[k_row][k_5] += a_5(h, i)

    E, v = np.linalg.eig(a)
    min_E_index = np.argmin(E)

    draw(x, y, v, z_0, min_E_index)

    first = E[min_E_index]
    print('first', first)

    E[min_E_index] = 99
    min_E_index = np.argmin(E)

    second = E[min_E_index]
    print('second', second)

    E[min_E_index] = 99
    min_E_index = np.argmin(E)

    third = E[min_E_index]
    print('third', third)

    # E_copy[min_E_index_2] = 0
    # min_E_index_3 = np.argmin(E_copy)
    #
    # E_copy[min_E_index_3] = 0
    # min_E_index_4 = np.argmin(E_copy)
    #
    # E_copy[min_E_index_4] = 0
    # min_E_index_5 = np.argmin(E_copy)
    return [first, second, third]


x0, xn, N, y0, ym, M, E, e, eps_0, z_0, m_, h_, = 0, 20, 50, 0, 20, 50, 1000, 1.6 ** (-19), 8.85418781762039 ** (
    -12), 10, 1 / 2, 1

E_arr = np.zeros((9, 3))
i = 0
for z_0 in np.arange(1, 10):
    E_arr[i] = (solve(x0, xn, N, y0, ym, M, E, e, eps_0, z_0, m_, h_))
    i += 1

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(np.arange(1, 10), E_arr[:, 0], s=10, c='b', marker="s", label='first')
ax1.scatter(np.arange(1, 10), E_arr[:, 1], s=10, c='r', marker="o", label='second')
ax1.scatter(np.arange(1, 10), E_arr[:, 2], s=10, c='y', marker="o", label='third')
plt.legend(loc='center right')
plt.xlabel('z_0')
plt.ylabel('E')
plt.show()

# E = (solve(x0, xn, N, y0, ym, M, E, e, eps_0, 8, m_, h_))
# z = np.zeros(6)
# for i in range(1, 7):
#     z[i - 1] = - 1 / (i ** 2)
#
# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# ax1.scatter(range(6), np.abs(E - z), s=10, c='b', marker="s")
# plt.ylabel('E - E_true')
# plt.title(f'z_0={8}')
# plt.show()
