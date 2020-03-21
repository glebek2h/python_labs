from functools import reduce

import numpy as np


def super_duper_func():
    with open('A.txt') as f:
        A = [list(map(int, row.split())) for row in f.readlines()]
    A = np.array(A)
    fourteen_col = A[:, 14]
    return reduce(lambda x, y: x + y * y if abs(y) > 8 else x, fourteen_col, 0)


print(super_duper_func())
