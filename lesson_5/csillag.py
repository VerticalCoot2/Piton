from os import system as s

s("cls")
csillagSzam = 0
for i in range(11):
    if(i < 6):
        csillagSzam += 1
    else:
        csillagSzam -= 1
    print("*"*csillagSzam)
    # csillagString = ""
    # for j in range(csillagSzam):
    #     csillagString += "*"
    # print(csillagString)