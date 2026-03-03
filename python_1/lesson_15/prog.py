from os import system as s
from math import pi
from random import randrange

def main():
    s("cls")
    # feladat1()
    # feladat2()
    # feladat3()
    feladat4()
    
def feladat1():
    print("I wandered lonely as a cloud\nThat floats on high o'er vales and hills,\nWhen all at once I saw a crowd,\nA host, of golden daffodils;\n\tBeside the lake, beneath the trees,\n\tzFluttering and dancing in the breeze.")

def feladat2():
    #A bekért adatokkal számold ki egy kúp felszínét. (alapterület * magasság )/3 (csak a rádiuszt és a magasságot kérhetitek be.)
    # r = int(input("r = "))
    # m = int(input("m = "))
    # print("A kúp területe: ", (r**2*pi * m)/3)

    print("A kúp területe: ", (int(input("r = "))**2*pi * int(input("m = ")))/3)

def feladat3():
    #csinálj egy listát, ami bekér random 10db és 20db között tört számot, írja ki a listát, és utána egy enter lenyomás után írja át int(egész szám) re a számokat.
    lista = []
    for i in range (randrange(10,21)):
        lista.append(float(input(f"add meg a(z) {i+1}.dik törtszámot: ")))
    print(*lista)
    input("Átszámolás egészre")
    for i in range (len(lista)):
        lista[i] = int(lista[i])
    
    print(*lista)

def feladat4():
    #generálj 20 random számot egy listába. írd ki. egy enter lenyomás után válogasd külön a páros, és a páratlan számokat két másik listába. az ereteti listát töröéd ki, és írd ki mind a 3 listát * nélkül
    lista = []

    for i in range (20):
        lista.append(randrange(1,101))

    print(lista)
    input("buffer")
    
    paros = []
    paratlan = []
    for i in range(20):
        if(lista[i]%2 == 0):
            paros.append(lista[i])
        else:
            paratlan.append(lista[i])
    lista = []
    print(f"{lista}\n{paros}\n{paratlan}")
    















if __name__ == "__main__":
    main()