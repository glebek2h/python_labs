import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 10 * np.pi, 0.01)

fig, ax = plt.subplots()
plt.plot(t * np.sin(t), t * np.cos(t), label="Archimedean spiral", lw=3)
plt.axis('equal')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()

plt.show()
