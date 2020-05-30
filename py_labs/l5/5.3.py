import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# y''' + y'' -10y' + 9y = 0
# u = y
# u' = y' = v
# v' = y'' = w
# w' = y''' = -y'' + 10y' - 9y = -w + 10v - 9u
#
# u(0) = 0
# v(0) = 0
# w(0) = 1

def rhs(s, v):
    return [v[1], v[2], -v[2] + 10 * v[1] - 9 * v[0]]


res = solve_ivp(rhs, (0, 2), [0, 0, 1])

y = res.y[0]
print(y)

# time points
t = np.arange(0.0, 2.0, 0.2)

plt.plot(t[:len(y)], y)
plt.show()