import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2, 100)
y = (1 + np.exp(3 * t)) ** (1. / 3) + t ** (3. / 4)
z = np.log10(4 - t ** 2) / (1 + np.cos(t))
w = z - y

fig, ax = plt.subplots()
ax.plot(t, y, color="green", label="y(t)", linestyle=':', linewidth=2)
ax.plot(t, z, color="pink", label="z(t)", linestyle='--', linewidth=2)
ax.plot(t, w, color="blue", label="w(t)", linestyle='-.', linewidth=2)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()

plt.show()
