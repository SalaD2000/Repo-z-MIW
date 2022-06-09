print("{0}- type: {1}\n{2}- type:\n".format("Sprawdzam",type("Sprawdzam"),"2",type("2"),2,type(2)))

#Wpisuję print a następnie wpisuję tekst. {0} {1} to placeholdery które później zostają wpisane w .format()
#type po prostu wypisuje klasę danej zmiennej

Napisy = ['Jestem','Damian','jestem','pacanem']
Napis1 = "_".join(Napisy)
print(Napis1)

#Łączenie napisów

Napis1_Split = Napis1.split("_")
print(Napis1_Split)
print(type(Napis1_Split))

#Splitowanie napisów

Zdanie = "Metody Inżynierii Wiedzy to taki przedmiot co się go boję"
print(Zdanie)
print(Zdanie.lower())
print(Zdanie.upper())

#Zmniejszanie wszystkich znaków
#Zwiększanie wszystkich znaków

ZmianaZnakow =Zdanie.replace("ż", "z").replace("ę", "e")
print(ZmianaZnakow,len(ZmianaZnakow))

#Za pomocą replace wymieniamy wybrane znaki na inne wybrane znaki

set = set(ZmianaZnakow)
print(set,len(set))

#Set nie zawiera w sobie żadnyh duplikatów
#Wyswietlajac len(set(ZmianaZnakow)) możemy dowiedzieć się ile jest tam różnych liter

Tuple = ("pierwszy",1)
print(Tuple)
print(type(Tuple))

#Zmienna typu tuple. Może mieć w sobie wiele różnych typów

Slownik = {"pierwszy" : 1,'drugi' : 2}
print(Slownik)
print(type(Slownik))

#Tutaj zmienna typu 'dict'

Znaki = ['b','a','c']
Cyfry = [2,1,3]
print(Znaki+Cyfry)

#Wyświetlanie zawartości 2 tablic

Znaki.append(Cyfry)
print(Znaki.index('a'))

#Dodanie do tablicy Znaki tablicy Cyfry i pokazanie w którym miejscu znajduje się 2

Cyfry2 = [0,1,2]
Cyfry3 = [4,5,6]
Cyfry2.append(3)
Cyfry2.extend(Cyfry3)
print(Cyfry2)

#Dodawanie na koniec listy

dict = {'d':2,'c':1,'b':4,'a':3}
print(dict)
dict_sort = {k:v for k,v in sorted(dict.items())}
print(dict_sort)

#Sortowanie słownika po literach

dict_sort = {k:v for k,v in sorted(dict.items(), key=lambda item: item[1])}
print(dict_sort)

#Sortwoanie słownika po cyfrach

Rozne = [' ','',0,1,'0','1',[],[',']]
for x in Rozne:
    print(bool(x))

#Hmmm... jakie bolle zwracają te znaki coż za loteria :O
    
for x in range(0,21,1):
    print(x, end=" ")
print("")
    
#Wyświetlenie od 0 do 20 ze spacją pomiędzy

to_split = " ".join(Napisy)
print(to_split)

def Haslo(Okon):
    if len(Okon)>=10 :
        spec = False
        duza = False
        mala = False
        for ch in Okon:
            if ch=="!":
                spec=True #Czy jest znak specjalny
            else:
                if ch not in ["0","1","2","3","4","5","6","7","8","9"]: #Czy jest tam cyfra
                    if ch==ch.upper():
                        duza = True     #Czy jes wielka litera
                    if ch==ch.lower():
                        mala = True     #Czy są tam małe litery
        if( spec & duza & mala):
            return True                 #Jeżeli wszystko sie zgadza zwróć prawdę
    return False                        #Każdy inny przypadek to fałsz

print(Haslo("0123456789aA!"))   

#Określanie czy dane hasło spełnia warunki

Tablcia = [1,2,3,4,5,99,6,7,8,9]

def index_99(Tablcia):
    x=0
    while(x<=len(Tablcia)):
       if(Tablcia[x]==99):
           return x
       x+=1
    return -1

#Wyszukiwanie indeksu wybranej liczby w tablicy

print(index_99(Tablcia))

with open("tekst.txt","r") as file:
    print(file.read().split("\n"))

    #Sczytywanie pliku
    
Kanapka = ['Kanapka','z','masłem','to','coś','niesamowitego']

with open("tekst.txt",'w') as file:
    for x in Kanapka:
        file.write(x+'\n')
        print(x)

    #Wpisywanie do pliku