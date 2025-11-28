from os import system as s
s("cls")

lista = [7,3,1,9,8,56,4,5]

#Maximumkiválasztás tétel
# max = lista[0]
# for i in range(1, len(lista), 1):
#     if(lista[i] > max):
#         max = lista[i]
# print(max)

#Minimumkiválasztás tétel
# min = lista[0]
# for i in range(1, len(lista), 1):
#     if(lista[i] < min):
#         min = lista[i]
# print(min)

#Összegzés tétel
# sum = 0
# for i in range(len(lista)):
#     sum += lista[i]
# print(sum)

#Megszámlálás
# db=0 # Hány 5-nél nagyobb szám van a listában
# for i in range(len(lista)):
#     if(lista[i] > 5):
#         db+=1
# print(db)

#Eldöntés tétel
# van = False #Van-é 9-es a listában
# for i in range(len(lista)):
#     if(lista[i] ==  9):
#         van = True
#         # break <-ilyet sosem használunk ilyen esetekben!
#     print(i)
# print(van)

#Lineáris keresés tétel
van=False #vab e 9 a listában?
i = 0
while(not van and i < len(lista)):
    if(lista[i] == 9):
        van = True
    else:
        i += 1
    print(i)
print(van, lista[i])

