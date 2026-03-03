from os import system as s
s("cls")

szo1 = input("szo1: ")
szo2 = input("szo2: ")

if(len(szo1) == len(szo2)):
    szo1 = sorted(szo1)
    szo2 = sorted(szo2)
    index = 0
    kulonbozik = False
    while kulonbozik and index < len(szo1):
        if(szo1[i] == szo2[i]):
            index += 1
        else:
            kulonbozik = True
    if(kulonbozik):
        print("Nem anagrammák.")
    else:
        print("A két szó anagramma.")
        
else:
    print("Nem anagrammák.")