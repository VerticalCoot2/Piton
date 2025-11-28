from os import system as s
from random import randrange
while(True):
    s("cls")
    
    szam = randrange(1,1001)
    print(szam)
    guess = 0
    print("\n\t Gondoltam egy számra 1 és 1000 között. Tippelgess, és találd ki!")
    while (guess != szam):
        guess = int(input())
        if(guess < szam):
            print("nagyobb")
        elif(guess > szam):
            print("kisebb")
    input("Gratulálok, eltaláltad. Megy mégegyszer?\n\nPersze!")