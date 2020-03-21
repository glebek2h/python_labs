import numpy as np
from scipy.linalg import expm

A = np.diagflat(np.arange(1, 15, 2, dtype=int), 0) + np.diag(np.full(6, 7, dtype=int), -1)
A[:, 4] = np.full(7, 9)
A[4][3] = 9

R = np.vstack((np.hstack((A, np.eye(7))), np.hstack((np.exp(A), expm(A)))))
np.savetxt('C.txt', R)
