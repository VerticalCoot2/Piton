from os import system as s
from random import randrange

def main():
    lista = []
    for i in range(50):
        lista.append(k(0,500))
    print(*lista)
    print(f"Átlag: {atlag(lista)}")

def k(a,b):
    return randrange(a,b+1)

def atlag(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    return sum/len(a)

if __name__ == '__main__':
    main()