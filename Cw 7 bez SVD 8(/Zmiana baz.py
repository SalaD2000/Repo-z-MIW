import numpy as np
import math as math



a = np.array([[1.,1.,1.,1.,1.,1.,1.,1.],                    #Macierz z tablicy
              [1.,1.,1.,1.,-1.,-1.,-1.,-1],
              [1.,1.,-1.,-1.,0.,0.,0.,0.],
              [0.,0.,0.,0.,1.,1.,-1.,-1.],
              [1.,-1.,0.,0.,0.,0.,0.,0.],
              [0.,0.,1.,-1.,0.,0.,0.,0.],
              [0.,0.,0.,0.,1.,-1.,0.,0.],
              [0.,0.,0.,0.,0.,0.,1.,-1.]])

b = np.dot(a,a.T)                                           #Przemnożenie macierzy podstawowej przez jej transpozycje
c = []
temp = 0
for row in a:
    c.append(np.dot(np.array(row),np.array(row).T))
print("B \n",b)
print("C \n",c)
print("c==np.diag(b) \n",c==np.diag(b))

d = []

for i in range(len(a[0])):                              #Przechodzimy przez wszystkie wiersze a
    print("a[i] \n", a[i])  
    d.append(a[i]/math.sqrt(c[i]))                      #Dzielimy prez pierwiaste z c[i] i dodajemy do lsity d 
    print("c[i] \n", c[i])

d = np.array(d)                                         #Przekształcamy d w maicierz
print("D \n",d)

print("Transpozycja ortonormalnej \n",d.T)              #d transponowane
print("Odrwrotna ortonormalna \n",np.linalg.inv(d))     #inerted d
print("d*d^-1 jest diagonalna\n",np.dot(d,np.linalg.inv(d)))           #d razy odwrotność d


#Internety trochę nie ogarnia jak t ze wzorami leciało
ones = np.diag([1.,1.,1.,1.,1.,1.,1.,1.])
va=np.array([8.,6.,2.,3.,4.,6.,6.,5.])
vb=np.dot(d,va) 
print("Zamiana baz ale nie wiem o co codzi \n", vb)