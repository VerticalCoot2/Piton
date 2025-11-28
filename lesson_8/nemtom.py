from os import system as s
s("cls")

nevek = ["Dóri","Huba","Boti","Tomi","Áron","Teó","Kolos","Imi","Tibi"]
vane = False

# for i in range (len(nevek)):
#     if(nevek[i] == "Kadosa"):
#         vane = True
#         break
keresendo = input("Keresendő név: ")
index = 0
while index < len(nevek) and vane != True:
    if(nevek[index] == keresendo):
        vane = True
    else:
        index += 1
if(vane):
    print(f"{keresendo} jelen van")
else:
    print(f"{keresendo} hiányzik!")