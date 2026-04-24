from random import randint
from os import system as s

def main():
    s("cls")
    taskTry()


def task1():
    
    lista = []
    for i in range(4):
        lista.append(input(f"Add meg a(z) {i+1}. listaelemet: "))
    lista = tuple(lista)
    modosit = True

    while(modosit):
        print(type(lista), lista)
        if(input("Szeretne még hozzáfűzni? nem -> nem ; igen -> akármi más input\n?\t") == "nem"):
            modosit = False
        else:
            lista = list(lista)
            lista.append(input("írja be az értéket, amit hozzá akr fűzni a sorhoz: "))
            lista = tuple(lista)
    print(type(lista), lista)

def task2():
    listComp1 = tuple(randint(1,(i+1)*10) for i in range(5))
    print(type(listComp1), listComp1)

    listcomp2 = tuple(randint(10**(i),10**(i+1)) for i in range(5))
    print(type(listcomp2), listcomp2)

def task3():
    t1 = (1,)
    t2  =(3,)
    temp = t1+t2 
    print(type(temp), temp)

def taskTry():
    t = (1,2,3,4,5,6,7,8,9,10)
    print(type(t), t)
    it = task4(t)
    if(it != None):
        print(type(it), it)
    else:
        print("shit")

def task4(a):
    if(isinstance(a, tuple)):
        lista = [i for i in range(len(a), 0, -1)]
        return tuple(lista)

    else:
        return None

if __name__ == '__main__':
    main()