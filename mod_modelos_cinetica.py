import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math

# SST (total sum of squares) metrica
def sst(y):
    y_mean = np.mean(y)
    resta = np.subtract(y, y_mean)
    cuadrado = resta**2
    sst = np.sum(cuadrado)
    return sst

# SSR (sum squared regression) metrica
def ssr(y, y_txa):
    y_mean = np.mean(y)
    resta = np.subtract(y_txa, y_mean)
    cuadrado = resta**2
    ssr = np.sum(cuadrado)
    return ssr

# SSE (Error de suma de cuadrados) metrica
def sse(y, y_txa):
    resta = np.subtract(y_txa, y)
    cuadrado = resta**2
    sse = np.sum(cuadrado)
    return sse


# R^2 metrica
def r_2(SSR, SST):
    return SSR/SST

# Zero-order
def zero_order(x,k, b):
    return k*x + b

# First-order
def first_order(x,a,b,c):
    y = -a*np.exp(-b*x)+c
    return y

# Higuchi
def higuchi(x, a, b):
    return a*np.sqrt(x) + b

# Tanh
def tanh(x, a, b):
    return a*np.tanh(b*np.sqrt(x))

# Korsmeyer-Peppas
def korsmeyer_peppas(x, a, n):
    return a*x**n

