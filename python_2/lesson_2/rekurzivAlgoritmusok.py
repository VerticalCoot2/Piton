from os import system as s
lefutas = 0
def main():
    lista = [47, 69, 42, 66, 88, 2145, 3, 8, 76, 10]
    s("cls")
    # print("0\n1")
    # fib(0,1)
    # gyoker(0)
    # print(szamol(8))
    # print(fakt(4))
    # print(hatvany(2, 5))
    # print(JOfib(5))
    # print(SUM(17))
    print(ListSUM(lista))

def ListSUM(lista, index = 1):
    lefutas +=1
    print("lefutas", lefutas)
    if(index == len(lista)):
        return 0
    return lista[index] + ListSUM(lista, index+1)
    



    pass

def fib(a,b):
    c = a+b
    print(c)

    if c < 5000000:
        fib(b, c)
def gyoker(szam):
    print(szam)
    gyoker(szam+1)
def szamol(szam):
    if(szam == 1):
        return 1
    else:
        return szamol(szam-1) + 1
def fakt(szam):
    if szam == 1:
        return 1
    else:
        return szam*fakt(szam-1)
    
def hatvany(a, n):
    if(n == 0):
        return 1
    else:
        return a * hatvany(a, n-1)
    
def JOfib(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    
    return JOfib(n-1) + JOfib(n-2)
def SUM(szam):
    if(szam == 1):
        return 1
    return szam + SUM(szam-1)

if __name__ == '__main__':
    main()