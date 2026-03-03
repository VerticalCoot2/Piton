from os import system as s
s("cls")

szam = int(input("SZám: "))

osztok = 2
prim = True
while prim and osztok < szam:
    if(szam%osztok == 0):
        prim = False
    else:
        osztok += 1
if(prim):
    print("Prím")
else:
    print("Nem prím")