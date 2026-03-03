from os import system as s
s("cls")
#Írjatok egy programot, ami bekér a felhasználótól 10 dolgot, amit beleír egy listába
# lista = []
# for i in range(10):
#     lista.append(input(f"Kérem a(z) {i+1}. dolgot: "))
# s("cls")
# print("A listád:\n", *lista)


#Ha a dolog "alma" akkor "narancs"-ot adjunk hozzá
# lista = []
# for i in range(10):
#     dolog = input(f"Kérem a(z) {i+1}. dolgot: ")
#     if(dolog != "alma"):
#         lista.append(dolog)
#     else:
#         lista.append("narancs")
# s("cls")
# print("A listád:\n", *lista)



#Írjatok egy olyan programot, ami bekér a felhasználótól egy szót, és azzal a szóval, és az éppen aktuális sorszámmal feltöti a listát, annyiszor, ahányszor a felhasználo mondja(egy szám bekéréssel)
# lista = []
# szo = input("Gimme szó: ")
# szam = int(input("Gimme hányszor: "))
# for i in range(szam):
#     lista.append(f"{szo}{(i+1)}")
# print(*lista)


#Írjatok egy olyan programot, folyamatosan bekér elemeket a listába, amíg a felhasználó üres ("") karaktert nem ad meg. Írja ki utána az egész listát.
lista = []
i = 0
uresKarakter = False
while(not uresKarakter):
    dolog = input(f"Mi leygen a lista {i+1}. eleme? ")
    if(dolog != ""):
        lista.append(dolog)
        i+=1
    else:
        uresKarakter = True
print("A lista:\n", *lista)