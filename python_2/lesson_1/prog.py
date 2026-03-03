from os import system as s
from random import randrange
def main():
    s("cls")
    lista = generalas(50,500)
    print(lista)
    print (f"A három szám összege{f1(1,2,3)}")
    print(f"Lista hossza: {f2(lista)}")
    # print(f"Az 5 szám átlaga: {f3(
    #     int(input("add meg a számot: ")),
    #     int(input("add meg a számot: ")),
    #     int(input("add meg a számot: ")),
    #     int(input("add meg a számot: ")),
    #     int(input("add meg a számot: ")))}")
    print(f"A lista átlaga: {f4(lista)}")
    lista2 = [3, 5]
    print(f"A lista átlaga: {f4(lista2)}")
    hulyeseg()
    

def generalas(min, max):
    listaa = []
    for i in range(20):
        listaa.append(randrange(min, max+1))
    return listaa

def f1(sz1, sz2, sz3):
    return sz1 + sz2 + sz3

def f2(l):
    return len(l)

def f3(a,b,c,d,e):
    return (a+b+c+d+e)/5

def f4(a): #    a = lista
    sz = 0
    for i in range(len(a)):
        sz+=a[i]
    return sz/len(a)

def hulyeseg():
    for i in range(20):
        print(i)
    hulyeseg()




if __name__ == '__main__':
    main()