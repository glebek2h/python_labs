import numpy as np
from matplotlib import pylab
from mpl_toolkits.mplot3d import Axes3D
from numpy import linalg as LA
from prettytable import PrettyTable


def draw(X, Y, Z):
    fig = pylab.figure()
    cs = Axes3D(fig, azim=-80)
    cs.plot_surface(X, Y, Z)
    pylab.show()


def u_true(x, t):
    return (x + 10 * t) ** 2


def solve(N, M, x, t, sigma, gamma):
    y = np.zeros((N, M))
    for i in range(N):
        y[i][0] = x[i] ** 2
    for j in range(M):
        y[0][j] = 100 * (t[j] ** 2)
    for i in range(0, N - 1):
        for j in range(0, M - 1):
            y[i + 1][j + 1] = (1 / (sigma * gamma)) * (
                    y[i][j + 1] * (1 + sigma * gamma) - y[i][j] * (1 - (1 - sigma) * gamma) - y[i + 1][j] * (
                    1 - sigma) * gamma)
    return y


# sigma = 0.45
# gamma = 10

th = ['sigma', 'gamma', '|| U_true - U ||']
table = PrettyTable(th)

for sigma in np.arange(0.4, 0.6, 0.01):
    for gamma in np.arange(1, 11, 0.1):
        h = 0.1
        tau = h * gamma / 10

        N, M = int(1 / h), int(1 / tau)
        x, t = np.zeros(N), np.zeros(M)

        for i in range(N):
            x[i] = i * h
        for j in range(M):
            t[j] = j * tau

        U_true = np.zeros((N, M))
        for i in range(N):
            for j in range(M):
                U_true[i][j] = u_true(x[i], t[j])

        U = solve(N, M, x, t, sigma, gamma)

        print(f'|| U_true - U || = {LA.norm(U_true - U)}')

        X, Y = np.meshgrid(t, x)
        draw(X, Y, U_true)
        draw(X, Y, U)
        table.add_row([sigma, gamma, LA.norm(U_true - U)])

print(table)
