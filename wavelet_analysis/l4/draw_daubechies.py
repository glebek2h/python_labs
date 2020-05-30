import numpy as np
from matplotlib import pyplot as plt
import pywt as pywt


def phi_0(x, left, right):
    if x < left or x > right:
        return 0
    return 1


def draw_scaling_function_and_wavelet(h):
    left, right = 0, 12
    x = np.arange(left, right, 1 / 4)
    N = len(x)

    fi, fi_obj = get_scaling_function(h[::-1], x, N, left, right)

    psi = get_wavelet_function(h, x, fi_obj)

    wavelet = pywt.Wavelet('db6')
    phi_true, psi_true, x_true = wavelet.wavefun(level=5)

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    ax1.plot(x, fi)
    ax1.set_title('phi')
    ax2.plot(x_true, phi_true, 'tab:orange')
    ax2.set_title('phi_true')
    ax3.plot(x, psi, 'tab:green')
    ax3.set_title('psi')
    ax4.plot(x_true, psi_true, 'tab:red')
    ax4.set_title('psi_true')

    for ax in fig.get_axes():
        ax.label_outer()

    plt.show()


def get_scaling_function(h, x, N, left, right):
    fi_1, fi_1_object = np.zeros(len(x), dtype=float), {}

    for xi in range(len(x)):
        for k in range(len(h)):
            fi_1[xi] += np.sqrt(2) * h[k] * phi_0(2 * x[xi] - k, left, right)
        fi_1_object[x[xi]] = fi_1[xi]

    fi_2 = np.zeros(len(x), dtype=float)

    fi_2_object = {}
    for m in range(1, N):
        fi_2_object = {}
        for x_i, i in zip(x, range(len(x))):
            for k in range(len(h)):
                if 2 * x_i - k in x:
                    fi_2[i] += np.sqrt(2) * h[k] * fi_1_object[2 * x_i - k]
            fi_2_object[x_i] = fi_2[i]
        fi_1_object = fi_2_object

    return fi_2, fi_2_object


def get_wavelet_function(h, x, fi_obj):
    q = np.zeros(len(h))
    for k in range(len(h)):
        q[k] = ((-1) ** k) * h[k]

    psi = np.zeros(len(x))
    for x_i, i in zip(x, range(len(x))):
        for k in range(len(h)):
            if 2 * x_i - k in x:
                psi[i] += np.sqrt(2) * q[k] * fi_obj[2 * x_i - k]
    return psi
