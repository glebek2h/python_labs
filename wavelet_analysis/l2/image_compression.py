import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray


def fft(x):
    return np.fft.fft(x)


def ifft(x):
    return np.fft.ifft(x)


def Z(m):
    count_zeros = 0
    count_matrix_numbers = len(m[:, 0]) * len(m[0, :])
    for i in range(len(m[:, 0])):
        for j in range(len(m[0, :])):
            if m[i][j] == 0:
                count_zeros += 1
    return count_zeros / count_matrix_numbers * 100


def get_Y_eps(Y, eps):
    n = len(Y[:, 0])
    m = len(Y[0, :])
    Y_eps = Y.copy()
    for i in range(n):
        for j in range(m):
            if abs(Y_eps[i][j]) <= eps:
                Y_eps[i][j] = 0
    return Y_eps


def PSNR(X, X_eps, n, m):
    s = 0
    for i in range(n):
        for j in range(m):
            s += (X[i][j] - X_eps[i][j]) ** 2
    rms = np.sqrt(s / (m * n))
    M_gray = 255
    return 20 * np.log10(M_gray / rms)


X = np.int32(
    rgb2gray(plt.imread(
        r'/Users/fpm.kazachin/PycharmProjects/wavelet_analysis/l2/ tulip_fields.jpg')) * 255)  # матрица из интенсивностей серого цвета

imgplot_1 = plt.imshow(X, cmap='Greys_r')
plt.savefig('compressed_img/source_black.png', bbox_inches='tight')

n = len(X[:, 0])
m = len(X[0, :])

Y = np.zeros((n, m), dtype=complex)
for i in range(m):  # применили fft к столбцам Х
    Y[:, i] = fft(X[:, i])

for i in range(n):  # применили fft к строкам Х
    Y[i, :] = fft(X[i, :])

eps_0 = Y[52][60]
eps_3 = Y[201][700]
eps_17 = Y[21][60]
eps_29 = Y[25][100]
eps_39 = Y[31][60]
eps_58 = Y[21][100]
eps_72 = Y[26][60]
eps_80 = Y[25][55]
eps_90 = Y[24][22]
eps_99 = Y[32][10]
eps_arr = [eps_0, eps_3, eps_17, eps_29, eps_39, eps_58, eps_72, eps_80, eps_90, eps_99]

Z_arr = []
PSNR_arr = []
for k in range(len(eps_arr)):
    Y_eps = get_Y_eps(Y, eps_arr[k])

    X_eps = np.zeros((n, m), dtype=complex)
    for i in range(m):  # применили ifft к столбцам Y
        X_eps[:, i] = ifft(Y_eps[:, i])

    for i in range(n):  # применили ifft к строкам Y
        X_eps[i, :] = ifft(Y_eps[i, :])

    imgplot_2 = plt.imshow(np.abs(X_eps), cmap='Greys_r')
    plt.savefig('compressed_img/eps_{0}.png'.format(round(Z(Y_eps))), bbox_inches='tight')

    PSNR_arr.append(np.abs(PSNR(X, X_eps, n, m)))
    Z_arr.append(Z(Y_eps))

    if k == 7:
        print('eps_80: ', eps_arr[k], 'Z(eps_80):', Z_arr[k])
    if k == 8:
        print('eps_90: ', eps_arr[k], 'Z(eps_90):', Z_arr[k])
    if k == 9:
        print('eps_99: ', eps_arr[k], 'Z(eps_99):', Z_arr[k])

plt.figure()
plt.plot(Z_arr, PSNR_arr)
plt.xlabel('Z')
plt.ylabel('PSNR')
plt.show()
