from os import system as s
s("cls")

#csináljatok egy olyan programot, amely bekér egy számot, és megmondja, hogy páros, vagy páratlan
szam = float(input("Adj egy szmámot, és megmondom, hogy páros vagy páratlan!\n\t"))
if(szam == 0):
    print("\n\tA szám nulla.")
elif not (szam%2 == 0):
    print("\n\tA szám páratlan.")
else:
    print("\n\tA szám páros.")
