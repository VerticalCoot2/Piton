from os import system as s
from random import randrange as rand

while True:
    s("cls")
    randSzam = rand(0,1001)
    tipp = ""
    print("Sorsolunk 0 és 1000 között egy számot. Találd ki!\n")
    while not(randSzam == tipp):
        tipp = int(input("Kérem a számot: "))
        if tipp > randSzam:
            print("\tA szám kisebb!")
        elif tipp < randSzam:
            print("\tA szám nagyobb!")
        else:
            print("\nGratulálok, eltaláltad a számot!\n")
    input()