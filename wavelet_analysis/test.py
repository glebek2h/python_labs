# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 16:01:02 2020

@author: Lenovo
"""
import numpy as np
import scipy.linalg as scpl


def explicit_view_F(n):
    w_n = w(n, 1)
    F = np.zeros((n, n), complex)
    for i in range(n):
        for j in range(n):
            F[i][j] = (w_n ** i) ** j
    return F


def w(n, m):
    return np.exp(-2j * np.pi * m / n)


def fft2(x):
    if len(x) <= 1:
        return x
    z0 = fft2(x[::2])
    z1 = fft2(x[1::2])
    r = range(len(x) // 2)
    w_mul_z1 = [w(len(x), k) * z1[k] for k in r]
    return [z0[k] + w_mul_z1[k] for k in r] + [z0[k] - w_mul_z1[k] for k in r]


def cooley_Tukey_factorization(n):
    t = np.log2(n)
    t = int(t)
    A = np.eye(n)
    B = np.eye(n)
    F = explicit_view_F(n)
    for q in range(0, t):
        L = 2 ** (q + 1)
        ptl = PTL(L)
        omega = np.zeros((L // 2, L // 2), complex)
        for i in range(L // 2):
            omega[i][i] = w(L, i)
        first_line_Bl = np.hstack((np.eye(int(L / 2)), omega))
        second_line_Bl = np.hstack((np.eye(int(L / 2)), -omega))
        Bl = np.vstack((first_line_Bl, second_line_Bl))
        p = len(Bl)
        g = n // p
        Aq = np.zeros((n, n), complex)
        RTL = np.zeros((n, n), complex)
        for k in range(0, g):
            for i in range(0, p):
                for j in range(0, p):
                    Aq[k * p + i][k * p + j] = Bl[i][j]
                    RTL[k * p + i][k * p + j] = ptl[i][j]
        A = np.matmul(Aq, A)
        B = np.matmul(B, RTL)
    print(scpl.norm(F - np.matmul(A, B)))


def PTL(L):
    ptl = np.zeros((L, L), int)
    i = 0
    for j in range(0, L, 2):
        ptl[i][j] = 1
        i += 1
    for j in range(1, L, 2):
        ptl[i][j] = 1
        i += 1
    return ptl


cooley_Tukey_factorization(4)
