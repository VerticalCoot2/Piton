#Feladat:
# írj egy programot, ami bekér a felhasználótól 5 számot amik nem ismétlődhetnek és megnézni, hogy az az a 5 szám benne van e a [40, 80, 147, 5, 62, 17, 78, 8, 34, 10] listában. Utána írja ki, hogy van e, hányadik helyen, és melyik szám egyezik. Ha egyik sem, akkor írja ki azt.

from os import system as s
s("cls")
list = [40, 80, 147, 5, 62, 17, 78, 8, 34, 10]

userList = []

for i in range(5):
    ugyanaz = False
    while(not ugyanaz):
        szam = int(input(f"Kérem a(z) {i+1} számot! Ne adj meg olyat, amit már meg adtál!\t"))
        
        index = 0
        hasOne = False
        while(index < len(userList) and not hasOne):
            if(userList[index] == szam):
                hasOne = True
            else:
                index += 1

        if(hasOne):
            input("Ezt már írtad...")
        else:
            ugyanaz = True
            userList.append(szam)

print(userList)

answerIndexList = []

for i in range(len(list)):
    index = 0
    includes = False
    while(index < len(userList) and not includes):
        if(list[i] == userList[index]):
            includes = True
        else:
            index += 1

    if(includes):
        answerIndexList.append(i)

if(len(answerIndexList) > 0):
    print("íme az egyező számok:")
    for i in range(len(answerIndexList)):
        print(f"A(z) {answerIndexList[i]+1}.helyen a(z) {list[answerIndexList[i]]}")
else:
    print("Nincs azonos szám.")