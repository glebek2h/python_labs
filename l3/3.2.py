import numpy as np
import scipy.special as sc


N = 10
z = 10
print sum([((5 / 6) + 2 * k) * sc.gamma(1 + k)/np.math.factorial(k) * sc.jv(1/(2 + k), z) * sc.jv(1/(3 + k), z) for k in range(0, N)])
