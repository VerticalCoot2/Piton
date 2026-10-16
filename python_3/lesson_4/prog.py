from os import system as s
from random import randrange

def main():
    s("cls")
    feladat3()
    

def feladat1():
    pass
    #kérjetek be két számot, és írjátok ki a nagyobbat, vagy ha egyenlők, akkor azt
    a = int(input("kérek egy számot"))
    b = int(input("kérek egy másikszámot"))

    c = a if (a > b) else b if(a < b) else "they are equal"
    print(c)

def feladat2():
    pass
    #töltsetek fel egy listát 10 számmal(-10 000, 10 000), majd a maximumkiválasztás tételével nézzétek meg, hogy melyik alegnagyobb, írjátok ki, majd minimumkiválasztással nézzétek meg hogy melik a legkisssebb, vonlyátok ki a legnagyobból. majd kérjen be egy számot a felhasználótól. És bináris kereséssel nézzétek meg, hogy szerepel e az a szám a listába.

    a = [randrange(-10000, 10000) for i in range(10)]
    max = a[0]
    for i in range(1,len(a), 1):
        max = i if (i < max) else max
    print(max)

    min = a[0]
    for i in range(1,len(a), 1):
            min = i if (i > min) else min

    print(max-min)

    num = int(input("Gimme a number"))
    index = 0
    foundIt = False
    while (not foundIt and index < len(a)):
        if(a[index] == num):
            foundIt = True
        else:
            index += 1
    print("Szerepel" if foundIt else "nemszerepel")


def feladat3():
    pass
    #kérjetek be egy szöveget a felhasználótól. Számollyátok ki, hoggy hánj szóbó ál. Majd soronként írjátok ki melyik szó hány karakterből áll, majd írjátok ki a szavakat megfordítva, de a mondatban elfoglalt helyüket nem változtatva.
    # pl.: (A holló sajtja nagy => A ólloh ajtjas ygan)

    text = input("írj egy szöveget:\n")
    szavak = text.split(' ')
    print(f"Szavak száma: {len(szavak)}\n")
    
    for i in range(len(szavak)):
        print(f"{szavak[i]} : {len(szavak[i])}db.")

    for i in range(len(szavak)):
        print(reverse(szavak[i]), end =" ")

def reverse(szo):
    text = ""
    for i in range(len(szo)-1, -1, -1):
        text += szo[i]
    return text


def feladat4():
    pass
    #írjatok egy másodfokú egenlet megoldó képletet. képlet a táblán?

    # x^2+10x+50 = 0
    
    # a = x^2
    # b = 10x
    # c = 50



if __name__ =='__main__':
    main()