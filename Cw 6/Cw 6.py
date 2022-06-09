import numpy as np
import math as math #xd

def Kowariancja(macierz):
    return np.dot(macierz.T,macierz)

def Odwrotnosc(macierz):
    return np.linalg.inv(macierz)

def L_Odwrotnosc(macierz):
    kow = Kowariancja(macierz)
    odwrotnosc = Odwrotnosc(kow)
    return np.dot(odwrotnosc,macierz.T)

