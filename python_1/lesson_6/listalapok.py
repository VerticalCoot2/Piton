from os import system as s
s("cls")

lista = ["egy", "kettő", "három", "négy", "öt", "hat", "hét", "nyolc", "kilenc", "tíz"]

print(lista)
print(*lista)

# for i in range (10):
#     print(lista[i])

# for i in range (9, -1, -1):
#     print(lista[i])

lista.append("tizenegy")
print(*lista)