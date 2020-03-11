import numpy as np
import random


def super_func(c, b=None):
    if np.linalg.det(c):
        if b is None:
            b = np.array([random.random() for i in range(10)])
        x = np.linalg.solve(c, b)
        return [x, sum(x)]


M = np.array([[2., 5.], [1., -10.]])
B = np.array([1., 3.])
print super_func(M, B)
