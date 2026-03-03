from os import system as s

s("cls")
csillagString = ""
csillagSzam = 0
for i in range(11):
    print("*"*((i < 6)? i : 6))