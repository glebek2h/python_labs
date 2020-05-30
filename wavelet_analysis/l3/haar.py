import numpy as np
import pywt
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from numpy import linalg as LA


def save_img(C, name):
    plt.imshow(C, cmap='Greys_r')
    plt.savefig('compressed_img/{0}.png'.format(name), bbox_inches='tight')


def for_rows(C_, n):
    for i in range(n):
        s, m = [], []
        for k in range(0, n - 1, 2):
            s.append((C_[i][k] + C_[i][k + 1]) / 2)
            m.append((C_[i][k] - C_[i][k + 1]) / 2)
        C_[i, :n] = s + m


def for_columns(C_, n):
    for j in range(n):
        s, m = [], []
        for k in range(0, n - 1, 2):
            s.append((C_[k][j] + C_[k + 1][j]) / 2)
            m.append((C_[k][j] - C_[k + 1][j]) / 2)
        C_[:n, j] = s + m


def dwt(C):
    if len(C) != len(C[0]):
        raise ValueError('Wrong matrix dimensions')
    n = len(C)
    C_ = np.array(C.copy(), dtype=float)
    while n != 1:
        for_rows(C_, n)
        for_columns(C_, n)
        n = n // 2
    return C_


def for_rows_i(C, n, iteration):
    for i in range(n):
        s = []
        for k in range(0, n - iteration, 1):
            s.append(C[i][k] + C[i][k + iteration])
            s.append(C[i][k] - C[i][k + iteration])
        C[i, :n] = s


def for_columns_i(C, n, iteration):
    for j in range(n):
        s = []
        for k in range(0, n - iteration, 1):
            s.append(C[k][j] + C[k + iteration][j])
            s.append(C[k][j] - C[k + iteration][j])
        C[:n, j] = s


def dwt_i(C_):
    if len(C_) != len(C_[0]):
        raise ValueError('Wrong matrix dimensions')
    n = len(C_)
    C = np.array(C_.copy(), dtype=float)
    c = 2
    iteration = 1
    while c != n * 2:
        for_columns_i(C, c, iteration)
        for_rows_i(C, c, iteration)
        c *= 2
        iteration *= 2
    return C


def set_d_to_0(C, d, i):
    C_ = C.copy()
    n = C_.shape[0]
    c = 0
    while n is not 1 and c < i:
        if d == 'g':
            C_[:n // 2, n // 2:n] = 0
        if d == 'v':
            C_[n // 2:n, :n // 2] = 0
        if d == 'd':
            C_[n // 2:n, n // 2:n] = 0
        n = n // 2
        c += 1
    return C_


C = np.int32(
    rgb2gray(plt.imread(
        r'/Users/fpm.kazachin/PycharmProjects/wavelet_analysis/l3/256x256.jpg')) * 255)  # матрица из интенсивностей серого цвета

save_img(C, 'source_black')
n = C.shape[0]
# tests:
# C = np.array([[0, 2, 1, 2],
#               [1, 1, 2, 0],
#               [0, 1, 2, 1],
#               [0, 2, 1, 2]])
# print('C = \n', C)
# C_ = dwt(C)
# print('C_ = \n', C_)
# print('dwt_i(C_) = \n', dwt_i(C_))


C_ = dwt(C)
save_img(C_, 'С_')
C_new = dwt_i(C_)
print('|dwt_i(C_) - C| =', LA.norm(C - C_new))

C_true = pywt.wavedec2(C, 'haar')
C_new_true = pywt.waverec2(C_true, 'haar')
print('|C_new_true - C| =', LA.norm(C_new_true - C))

# task 1
# a)
C_with_d_1_g_0 = set_d_to_0(C_, 'g', 1)
C_new = dwt_i(C_with_d_1_g_0)
save_img(C_with_d_1_g_0, 'task_1_a_C_')
save_img(C_new, 'task_1_a')

# a) true
C_true_array, coeff_slices = pywt.coeffs_to_array(C_true)
print('M:', LA.norm(C_true_array - C_))
C_true_array = set_d_to_0(C_true_array, 'g', 1)
C_new_true = pywt.waverec2(pywt.array_to_coeffs(C_true_array, coeff_slices, output_format='wavedec2'), 'haar')
print('||dwt_i(C_) - dwt_i_true(C_true)|| a:', LA.norm(C_new_true - C_new))
save_img(C_new_true, 'task_1_a_true')

# b)
C_with_d_1_v_0 = set_d_to_0(C_, 'v', 1)
C_new = dwt_i(C_with_d_1_v_0)
save_img(C_with_d_1_v_0, 'task_1_b_C_')
save_img(C_new, 'task_1_b')

# b) true
C_true_array, coeff_slices = pywt.coeffs_to_array(C_true)
C_true_array = set_d_to_0(C_true_array, 'v', 1)
C_new_true = pywt.waverec2(pywt.array_to_coeffs(C_true_array, coeff_slices, output_format='wavedec2'), 'haar')
print('||dwt_i(C_) - dwt_i_true(C_true)|| b:', LA.norm(C_new_true - C_new))
save_img(C_new_true, 'task_1_b_true')

# c)
C_with_d_1_d_0 = set_d_to_0(C_, 'd', 1)
C_new = dwt_i(C_with_d_1_d_0)
save_img(C_with_d_1_d_0, 'task_1_c_C_')
save_img(C_new, 'task_1_c')

# c) true
C_true_array, coeff_slices = pywt.coeffs_to_array(C_true)
C_true_array = set_d_to_0(C_true_array, 'd', 1)
C_new_true = pywt.waverec2(pywt.array_to_coeffs(C_true_array, coeff_slices, output_format='wavedec2'), 'haar')
print('||dwt_i(C_) - dwt_i_true(C_true)|| c:', LA.norm(C_new_true - C_new))
save_img(C_new_true, 'task_1_c_true')

# task 2
C_copy = C_.copy()
C_ = set_d_to_0(C_, 'g', 1)
C_ = set_d_to_0(C_, 'v', 1)
C_ = set_d_to_0(C_, 'd', 1)
C_new = dwt_i(C_)
save_img(C_, 'task_2_C_')
save_img(C_new, 'task_2')

# task 2 true
C_true_array, coeff_slices = pywt.coeffs_to_array(C_true)
C_true_array = set_d_to_0(C_true_array, 'g', 1)
C_true_array = set_d_to_0(C_true_array, 'v', 1)
C_true_array = set_d_to_0(C_true_array, 'd', 1)
C_new_true = pywt.waverec2(pywt.array_to_coeffs(C_true_array, coeff_slices, output_format='wavedec2'), 'haar')
print('||dwt_i(C_) - dwt_i_true(C_true)|| task_2:', LA.norm(C_new_true - C_new))
save_img(C_new_true, 'task_2_true')

# task 3
C_ = set_d_to_0(C_, 'g', 2)
C_ = set_d_to_0(C_, 'v', 2)
C_ = set_d_to_0(C_, 'd', 2)
C_new = dwt_i(C_)
save_img(C_, 'task_3_C_')
save_img(C_new, 'task_3')

# task 3 true
C_true_array, coeff_slices = pywt.coeffs_to_array(C_true)
C_true_array = set_d_to_0(C_true_array, 'g', 1)
C_true_array = set_d_to_0(C_true_array, 'v', 1)
C_true_array = set_d_to_0(C_true_array, 'd', 1)
C_true_array = set_d_to_0(C_true_array, 'g', 2)
C_true_array = set_d_to_0(C_true_array, 'v', 2)
C_true_array = set_d_to_0(C_true_array, 'd', 2)
C_new_true = pywt.waverec2(pywt.array_to_coeffs(C_true_array, coeff_slices, output_format='wavedec2'), 'haar')
print('||dwt_i(C_) - dwt_i_true(C_true)|| task_3:', LA.norm(C_new_true - C_new))
save_img(C_new_true, 'task_3_true')

# task 4
for j in range(7, 13):
    C_copy[170][j] = 0

for j in range(0, 12):
    C_copy[197][j] = 0

for j in range(0, 14):
    C_copy[230][j] = 0

for j in range(49, 60):
    C_copy[167][j] = 0

for j in range(100, 116):
    C_copy[252][j] = 0

C_new = dwt_i(C_copy)
save_img(C_new, 'task_4')
