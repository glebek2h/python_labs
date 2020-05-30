import numpy as np
import time
from scipy.sparse.linalg import bicg
from scipy.linalg import solve_banded
from scipy.sparse import dia_matrix

A = dia_matrix((np.array([[13, 14, 15, 28, 33, 44], [15, 16, 18, 22, 32, 42], [17, 18, 19, 44, 71, 81]]), [0, -1, 1]),
               shape=(6, 6)).toarray()
b = [1, 2, 3, 4, 5, 6]
start_time_1 = time.time()
print(bicg(A, b))
end_time_1 = (time.time() - start_time_1) * 1000

ud = np.insert(np.diag(A, 1), 0, 0)
d = np.diag(A)
ld = np.insert(np.diag(A, -1), len(d) - 1, 0)
ab = [ud, d, ld]

start_time_2 = time.time()
print(solve_banded((1, 1), ab, b))
end_time_2 = (time.time() - start_time_2) * 1000

print('bicg:', end_time_1, 'solve_banded:', end_time_2)
