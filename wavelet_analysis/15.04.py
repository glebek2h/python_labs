import pywt
import numpy as np
import matplotlib.pyplot as plt

# wav = pywt.Wavelet('haar')
wav = pywt.Wavelet('db2')
print(wav.dec_lo)
print(wav.dec_hi)

data = np.arange(8)
print(pywt.wavedec(data, 'haar'))

dim = 32
img = np.zeros((dim, dim))
img[5, :] = 1
img[:, 10] = 1
img[:, 15] = 1
n = 15
for i in range(n):
    img[i, n + i] = 1

dwt = pywt.wavedec2(img, 'haar')
print(dwt)
co_matrix, _ = pywt.coeffs_to_array(dwt)
print(co_matrix)

kwargs = dict(cmap=plt.cm.gray, interpolation='nearest')
plt.imshow(img, **kwargs)

plt.imshow(co_matrix, **kwargs)
plt.show()


