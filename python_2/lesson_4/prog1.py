from os import system as s
from random import randrange
import random

def main():
    s("cls")
    Task4()
    
def Task1():
    #with break
    for i in range(50):
        print(i)
        if i == 25:
            break

    print('\n\n')
    #without break
    index = 1
    target = 50 
    feltetel = False
    while ((index <= target) and not feltetel):
        print(index)
        if(index == 25):
            feltetel = True
        else:
            index += 1

def Task2():
    lista = []
    for i in range(20):
        lista.append(randrange(1,101))
    print(f"og list: {lista}")
    print("Páros számok a listában:", end=" ")

    for i in printEven(lista):
        print(i, end = " ")

def Task3():
    lista = []
    for i in range(20):
        lista.append(randrange(1,101))
    print(f"maximum of the list: {MaxSearch(lista)}")

def MaxSearch(lista):
    max = lista[0]
    for i in range(1, len(lista)):
        max = lista[i] if (max < lista[i]) else max
    return max

def GoodMaxSearch(lista):
    maxIndex = 0
    for i in range(1, len(lista)):
        maxIndex = i if (lista[maxIndex] < lista[i]) else maxIndex
    return maxIndex

def printEven(lista):
    for i in lista:
        if( i%2 == 0):
            yield i

def Task4():
    items = ["Laptop", "Asztalka", "Unity", "McDonaldsos kesztyű", "Alma"]
    prices = [7.54, 5.55, 2.18, 157.99, 4.99] # €

    basket = []
    itemPrice = []
    buyItems(items, prices, basket, itemPrice)

    maximum = GoodMaxSearch(itemPrice)
    print(f"A legdrágább tétel: {basket[maximum]}, ami enniybe kerül: {itemPrice[maximum]}€")

def buyItems(items, prices, basket, itemPrice):

    desiredItemCount = int(input("Hány tételt szeretnél?"))
    
    for i in range(desiredItemCount):

        rand = random.randint(0, len(items)-1)

        basket.append(items[rand])
        itemPrice.append(prices[rand])

        print(f"{basket[i]}\t.-{itemPrice[i]}")

if __name__ == '__main__':
    main()