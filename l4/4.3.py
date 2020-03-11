import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def f(x, y):
    return 3 * x ** 2 * (np.sin(x)) ** 2 - 5 * np.exp(2 * y)


y = np.linspace(-1, 1, 100)
x = y
X, Y = np.meshgrid(x, y)

Z = f(X, Y)

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=1, fontsize=10)
ax.set_title('Contour')

ax = Axes3D(fig)
ax.plot_surface(X, Y, Z)
plt.show()
