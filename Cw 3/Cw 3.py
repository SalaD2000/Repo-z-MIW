import random as rand
import numpy as np
import math
import matplotlib.pyplot as plt
#import eval

def sqrt(value, epsilon):                                               #Funkcja pierwiastkująca
    a, b = value, 1
    while abs(a-b) > epsilon:
        a, b = (a+b)/2, value/((a+b)/2)
    return a

# print(sqrt(4, 0.00000000000000000001))

def montecarlo_integration(foo, xp, xk, sample):                        #Wprowadzamy funkcje, x początkowe, x końcowe oraz ilośc losowanych punktów
    minimum, maximum = foo(xp), foo(xk)
    for i in np.arange(xp+0.1, xk+0.1, 0.1):                            #Przesuwamy się po wykresie o 0.1 i mierzymy miniumum oraz maksimum
        if foo(i) < minimum:
            minimum = foo(i)
        if foo(i) > maximum:
            maximum = foo(i)
    #minimum, maximum = minimum-10, maximum+10
    points = 0
    for j in range(sample):                                             #Wprowadzmy losowe punkty w wybranym obrębie
        x = rand.uniform(xp, xk)
        y = rand.uniform(minimum, maximum)
        if y <= foo(x):                                                 #Sumujemy ilość punktów pod funkcją
            points += 1
    print(points, xk, xp, minimum, maximum)
    return (xk-xp)*(maximum-minimum)*(points/sample)                    #Zwracamy już obliczenia ze wzoru

def foo(x):
    return x

print(montecarlo_integration(foo, 0, 2, 100000))

def Prostokaty(function, a, b, i):
    dx = (b - a) / i                                #Szerokości wydzielonych prostokątów
    integr = 0
    for x in range(i):                              #Sumowanie wyników 
        x = x * dx + a                              #Przeskakiwanie o szerokość Prostokąta
        integr += dx * function                     #Dodawanie do siebie wyników
    return integr

def funkcjaaa(x):
    return x**2

Prostokaty = Prostokaty(2, 0, 5, 20)

def mean_average(list1):                                                            #Srednia
    return sum(list1) / len(list1)

def variance(list1):                                                                #Wariancja
    return sum([pow((x-mean_average(list1)), 2) for x in list1]) / len(list1)       

def standard_deviation(list1):                                                      #Odchylenie standardowe
    return pow(variance(list1), 1/2)



#Poniżej to samo w wersji wektorowej

def VECTOR(vector):
    vector_array = np.array(vector)
    skalar = np.dot(vector_array, np.ones(vector))
    return skalar / len(vector)

def VARIANCE_VECTOR(vector):
    a = np.full((1,len(vector)), VECTOR(vector))
    b = vector - a
    c = pow(b,2)
    d = sum(c)
    e = d / len(vector)
    return e

def STANDARD_VECTOR(vector):
    f = VARIANCE(vector)
    g = pow(f,1/2)
    return g


#Rysowanie średniej prostej

x =  np.array([                                                         #Tworzenie tablic
    [2],
    [5],
    [7],
    [8],
])

y =  np.array([                                                         
    [1],
    [2],
    [3],
    [3],
])

def funkcja(IKSY, IGREKI):      
    n = len(IKSY)                                                           #Długość X
    X = np.ones((n, 1))                                                     #tablica ługości n wypełniona 1
    X = np.hstack((X, IKSY))                                                #Łączenie tablic
    print("X \n", X)
    B = np.linalg.inv(np.transpose(X) @ X) @ np.transpose(X) @ IGREKI       #(X.T * X^-1) * X.T * vector
    print("B\n", B)

    b1 = B[1][0]
    b0 = B[0][0]
    plt.figure(figsize=(12,8))
    plt.scatter(x, y, alpha=1)
    plt.plot(x, [b0 + b1 * n for n in x])
    plt.title('Średnia Gładka')
    plt.show()                                                              #Rysowanie wykresu

funkcja(x, y)