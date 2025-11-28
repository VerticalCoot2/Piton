from os import system as s
s("cls")

lista = ["egy", "kettő", "három", "négy", "öt", "hat", "hét", "nyolc", "kilenc", "tíz"]
print(lista)

# for i in range(len(lista)):
#     lista[i] = "SZÁÁZ"
# print(lista)

# for i in range(1, len(lista), 2):
#     lista[i] = "SZÁÁZ"
# print(lista)

# for i in range(len(lista)):
#     if(i%2 != 0):
#         lista[i] = "SZÁÁZ"
# print(lista)
# lista.remove("SZÁÁZ")
# print(lista)

lista.pop(0)
print(lista)