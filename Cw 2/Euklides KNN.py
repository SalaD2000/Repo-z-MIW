import math

miasta = ["Warszawa","Gdańsk","Łódź","Poznań","Ełk","Sosnowiec"]

australian = []
 
with open("australian.dat","r") as file:
    australian = [list(map(lambda a: float(a),line.split())) for line in file]                          #Sczytywanie wszystkiego z tego australian.dat
    
#print(australian)

def metryka_euklidesowa(l1, l2):                                                                        #Metryka euklidesowa klasyczek wzór w internetach
    suma = 0
    for i in range(max(len(l1),len(l2))-1):
        suma+=(l1[i]-l2[i])**2
    return math.sqrt(suma)

def Metryka_Euklidesowa_Wektory(ListaA, ListaB, CzyObcinac=0):
    if CzyObcinac:
        v1 = np.array(ListaA[:-1])
        v2 = np.array(ListaB[:-1])
    else:
        v1 = np.array(ListaA)
        v2 = np.array(ListaB)
    Mnozenie = np.dot(v1-v2,v1-v2)

    wynik = mt.sqrt(Mnozenie)
    print(wynik)

#ostatni punkt to klasa klasa_dezyzjna
    
# print(metryka_euklidesowa(australian[0],australian[1]))
# print(metryka_euklidesowa(australian[0],australian[2]))
# print(metryka_euklidesowa(australian[0],australian[3]))
# print(metryka_euklidesowa(australian[0],australian[4]))
# print(metryka_euklidesowa(australian[0],australian[5]))
# print(metryka_euklidesowa(australian[0],australian[6]))
# print(metryka_euklidesowa(australian[0],australian[7]))
# print(metryka_euklidesowa(australian[0],australian[8]))
# print(metryka_euklidesowa(australian[0],australian[9]))

#Metryka:
# |A|-|B|=0 to A i B to ten sam punkt
# |AB|=|BA|

#Praca dowmowa
#Funkcja ma liczyć odległość kazdego z obiektóww do obiektu zerowego
#Pogrupować wszystko wobec klasy decyzyjnej do słownika (klasa klasa_dezyzjna : australijczyk wartości) klasa klasa_dezyzjna to ostatni atrybut


def grupowanie_australijczykow(australijczyk,numer_indexu_decyzyjnego,od_kogo_liczymy_odl):
    grupy = dict()                                                                      #Deklarujemy "grupy" jako słownik
    do_niego_liczymy = australijczyk[od_kogo_liczymy_odl]
    for x in range(1,len(australijczyk)):                                               #Lecimy po całej liście
        klasa_dezyzjna = australijczyk[x][numer_indexu_decyzyjnego]                     #Zczytujemy z pliku australian.dat indeks decyzyjny
        #print(klasa_dezyzjna,"\n")                  
        if klasa_dezyzjna in grupy.keys():                                              #Sprawdzamy czy klasa klasa_dezyzjna jest już jako klucz w słowniku     słownik[kolor]= "biały" = (dict.keys-(['kolor']))
            grupy[klasa_dezyzjna].append(metryka_euklidesowa(do_niego_liczymy, australijczyk[x]))      #Jeśli tak to przypisujemy do danego klucza wawrtosć obliczeń z metryki euklidesowej
        else:
            grupy[klasa_dezyzjna]=[metryka_euklidesowa(do_niego_liczymy, australijczyk[x])]            #Jeśli nie to dodajemy klasę decyzyjną jako klucz i przypisujemy do niej wynik metryki euklideswoej
    return grupy


print("======================================")
grup_austr = grupowanie_australijczykow(australian,14,0)
print(grup_austr)   
print("======================================")
print(metryka_euklidesowa(australian[0],australian[1]))
print(metryka_euklidesowa(australian[0],australian[2]))                                 #Sprawdza pierwsze trzy po zerowym od ktrórego liczymy odległość (Wygląda jaby się zgadzało)
print(metryka_euklidesowa(australian[0],australian[3]))
print("======================================")

# KNN powalona akcja K-najbliższych sąsiadów (K Nearest neighbours)
# Dobra czyli z tego co rozumiem co wikipedia gada to jest tak że wstawiamy jakiś nowy punkt i oraz wpisjemy jaką odległość bierzemy pod uwagę
# I po tym jak sprawdzimy jak zaklasyfikowane są punkty w branej pod uwagę odległości na podstawie tego wyznaczamy klasę
# W branej pod uwagę odległości lub ilości najbliższych sąsiadów


def KNN(australijczyk,numer_indexu_decyzyjnego,nowy_punkt):
    grupy = dict()                                                                                      #Ponownie tworzymy słownik do grup
    for x in range(0,len(australijczyk)):                                                               #Pętla która leci przez całego australiana
        klasa_dezyzjna = australijczyk[x][numer_indexu_decyzyjnego]                                     #Zczytanie klasy decyzyjnej z australian.dat
        if klasa_dezyzjna in grupy.keys():                                                              #Sprawdzamy czy klasa decyzyjna jest juz jako klucz w słowniku
            grupy[klasa_dezyzjna].append(metryka_euklidesowa(nowy_punkt, australijczyk[x]))             #Jeśli tak to dodajemy do danego klucza wynik
        else:
            grupy[klasa_dezyzjna]=[metryka_euklidesowa(nowy_punkt, australijczyk[x])]                   #Jeśli nie to dodajemy klasę decyzyjną jako klucz i dodajemy wpis do tego klucza
    return grupy

GrupyKNN = KNN(australian, 14, [1,1,1,1,1,1,1,1,1,1,1,1,1,1])
print(GrupyKNN[0])
print(GrupyKNN[1])
print("=========================================")
GrupyKNN[0].sort()
GrupyKNN[1].sort()
print(sum(GrupyKNN[0][:5])) #Suma 5 Najbliższych punktów z klasą 0
print(sum(GrupyKNN[1][:5])) #Suma 5 Najbliższych punktów z klasą 1
print("=========================================")

def LISTA_KNN(australijczyk,numer_indexu_decyzyjnego,nowy_punkt):                                       #Wprowadzenie odległośći do nowego punktu do listy
    lista = []
    for x in range(0,len(australijczyk)):                                                               #Przechodzimy prez całe australian.dat
        klasa_dezyzjna = australijczyk[x][numer_indexu_decyzyjnego]                                     #Sprawdzamy klasę decyzyjną anego punktu
        lista.append((klasa_dezyzjna,metryka_euklidesowa(nowy_punkt, australijczyk[x])))                #Dodawanie do listy
    return lista

def Suma_Odl(australijczyk,k):                                                                          #Sumowanie odległości od danych klas
    grupy = dict()                                                                                      #Deklaracja słownika
    for element in australijczyk:                                                                       #Lecimy przez każdy element ze wcześniej stworzonej listy
        klasa_dezyzjna = element[0]                                                                     #W danej liscie klasa decyzyjna jest na pierwszym miejscu
        if klasa_dezyzjna in grupy.keys():
            grupy[klasa_dezyzjna].append(element[1])                                                    #Jeżeli klucz już jest w słowniku dodaj odległość danego punktu 
        else:
            grupy[klasa_dezyzjna]=[element[1]]                                                          #Jeżeli nie to dodajemy klasę jako punkt i wspujemy do niej odległość
    for klucz in grupy.keys():                                                                          #Lecimy przez klucze w słowniku
        grupy[klucz].sort()                                                                             #I je sortujemy od najmniejszej do największej
    for klucz in grupy.keys():                                                                          #Pętla w której dodajemy do siebie odległośi k najbliższych sąsiadów o danym kluczu
        suma = 0
        for ele in grupy[klucz][:k]:
            suma+= ele
        grupy[klucz]=suma
    return grupy
            
grupy = Suma_Odl(LISTA_KNN(australian, 14, [1,1,1,1,1,1,1,1,1,1,1,1,1,1]),5)
print(grupy[0]) #Suma 5 Najliższych punktów klasy 0
print(grupy[1]) #Suma 5 najbliższych punktów klasy 1

Sprawdzam0 = sum(GrupyKNN[0][:5]) #Suma 5 Najbliższych punktów z klasą 0
Sprawdzam1 = sum(GrupyKNN[1][:5]) #Suma 5 Najbliższych punktów z klasą 1

print(bool(grupy[0]==Sprawdzam0))
print(bool(grupy[1]==Sprawdzam1))
#print(grupy[2])



