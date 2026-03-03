from os import system as s
from random import randrange as rand
s("cls")

szamok = []
for i in range(20):
    szamok.append(rand(1, 51))
print(szamok)

#legnagyobb:
max = szamok[i]
for i in range(1,len(szamok),1):
    if(szamok[i] > max):
        max = szamok[i]

#legkisebb:
min = szamok[i]
for i in range(1,len(szamok),1):
    if(szamok[i] < min):
        min = szamok[i]

print("A legnagyobb szám:", max)
print("A kisebb szám:", min)

szam = int(input("Milyen számot keressek?"))
index = 0
van = False
while(not van and index < len(szamok)):
    if(szamok[index] == szam):
        van = True
    else:
        index+=1
if(van):
    db = 0
    for i in range(len(szamok)):
        if(szamok[i] == szam):
            db+=1
    print(f"Van {szam} szám, és {db}db van belőle")
else:
    print("Nincs a listában ilyen szám!")        