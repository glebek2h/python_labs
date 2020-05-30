import numpy as np
from scipy.integrate import quad
from scipy.optimize import fminbound
from scipy.special import gamma


def integrand(x, a):
    return gamma(a * x) * np.exp(-a * x)


def f(a):
    return quad(integrand, 1, 2, args=(a,))[0]


print(fminbound(f, 0, 1))
