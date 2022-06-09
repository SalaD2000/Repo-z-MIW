import math as m
import numpy as np
from itertools import product


def qr_decomp(A):
    m, n = A.shape
    rank = np.linalg.matrix_rank(A)
    print(rank)

    if rank < n:
        raise SingularException(f"Matrix rank {rank} is smaller than the number of columns {n}")

    Q = np.zeros((m,n))

    for i, column in enumerate(A.T):                                #Wstawianie kolumn do Q
        Q[:,i] = column
        print(Q[:,i])

        for prev in Q.T[:i]:                                        #Odejmowanie projekcji od danej kolumny
            Q[:,i] -= (prev @ column) / (prev @ prev) * prev

    Q /= np.linalg.norm(Q, axis=0)                                  #Normalizacja czyli podzielenie kolumny przez swoją długość czyli u/||u||
    R = Q.T @ A

    return Q, R

Macierz = np.array([[1,0],
                    [1,1],
                    [0,1]])

Q, R = qr_decomp(Macierz)

print(Q)
print(R)
