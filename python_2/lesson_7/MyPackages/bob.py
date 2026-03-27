from random import randint
def BobSummarise(x,y):
    return x+y

def Negyzetreemeles(a, n):
    return a**n

def Talald_Meg_a_Primeket(lista):
    primList = []
    for i in range(len(lista)):
        
        prim = True
        index = 2
        while (index < lista[i] and prim):
            
            if(lista[i]%index != 0):
                index += 1
            else:
                prim = False
        if(prim):
            primList.append(lista[i])

    if(len(primList) > 0):
        return primList
    else:
        return False
    
def MatrixKreacio():
    sor = int(input("Hány sor legyen? "))
    oszlop = int(input("Hány oszlop legyen? "))
    r = input("melyik két szám között sorsoljak? megadási mód: x-y (x<y) ").split('-')

    matrix = []
    for i in range(sor):
        lista = []
        for j in range(oszlop):
            lista.append(randint(int(r[0]), int(r[1])))
        matrix.append(lista)
    return matrix