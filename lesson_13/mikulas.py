from os import system as s
from random import randrange
s("cls")
# Mikulásnak szüksége van a seg(gítség)edre!
# írj egy programot, ami a nevek listából csinál egy mátrixot, amibe randomizálnod kell 1-100 ig egy "jóság" százalékot, ez alapján
# meg be kell rakni a jó, illetve a rossz listára. Ennek a feladatnak legyen "menüje"(számok segítségével ki lehessen választani,
# hogy éppen melyik listát mutassa meg) legyen egy olyan menüpont, ahol új embert lehet felvenni a listára. ott a felhasználónak
# kell megadnia az ember nevét, és jóság százalékát. ezek után sorolja be a program.legyen még egy kiíratás, ami a határon(40%<x<60%) állnak.
# kell még két menüpont: az egyik a legjobb, a másik a legrosszabb gyereket mutatja meg a listában. A kiírás után újra írja ki a menüt.
# AZ utolsó menüpont írja ki az egész listát.

regies_nevek = [
    "Andrássy Gyula", "Apponyi Albert", "Batthyány Lajos", "Báthory Erzsébet", "Bezerédj Amália",
    "Bornemisza Péter", "Brunszvik Teréz", "Chernel István", "Csáky Krisztina", "Csemegi Károly",
    "Dessewffy Arisztid", "Dőry Etelka", "Eötvös József", "Erdődy Pál", "Esterházy Miklós",
    "Fáy András", "Festetics György", "Forgách Zsuzsanna", "Ghyczy Kálmán", "Grassalkovich Antal",
    "Hadik András", "Hunyadi Mátyás", "Illésházy István", "Justh Gyula", "Kállay Béni",
    "Károlyi Mihály", "Kemény Zsigmond", "Kornis Gáspár", "Kováts Mihály", "Lipthay Sándor",
    "Madarász László", "Mészöly Géza", "Nádasdy Ferenc", "Orczy Emma", "Pálffy János",
    "Patay István", "Perényi Zsigmond", "Podmaniczky Frigyes", "Prónay Sándor", "Puky Endre",
    "Ráday Gedeon", "Reviczky Gyula", "Rhédey Klaudia", "Semsey Andor", "Szapáry Gyula",
    "Széchenyi István", "Szinyei Merse", "Teleki Blanka", "Thököly Imre", "Tisza Kálmán",
    "Vay Ádám", "Wesselényi Miklós", "Zichy Mihály", "Zrínyi Ilona", "Almássy László",
    "Ambrózy Béla", "Bajzáth József", "Balassa Bálint", "Barcsay Jenő", "Barkóczy Ferenc",
    "Bánffy Miklós", "Beniczky Lajos", "Bethlen Gábor", "Bónis Sámuel", "Bottlik János",
    "Cházár András", "Czobor Imre", "Darvas József", "Degenfeld József", "Döbrentei Gábor",
    "Draskovich János", "Egressy Gábor", "Fekete János", "Haller János", "Héderváry Károly",
    "Jankovich Béla", "Jósika Miklós", "Kende Zsigmond", "Klobusiczky Péter", "Koháry István",
    "Lónyay Menyhért", "Majláth György", "Máriássy Béla", "Nákó Sándor", "Nyáry Pál",
    "Odescalchi Artúr", "Országh Kristóf", "Pallavicini Ede", "Pejacsevich Péter", "Péchy Manó",
    "Pongrácz István", "Pulszky Ferenc", "Radvánszky Béla", "Révay Péter", "Rónay Jácint",
    "Serényi Béla", "Sigray Jakab", "Somssich Pál", "Szilágyi Dezső", "Sztáray Gábor",
    "Török Bálint", "Ujházy László", "Vécsey Károly", "Wenckheim Béla", "Zay Károly"
]

#menu:
# listagenerálás - 1
# jó gyerekek listája - 2
# rossz gyerekek listája - 3
# gyerek hozzáadás - 4
# határ gyerekek listája - 5
# legjobb gyerek megmutatása - 6
# legrosszabb gyerek megmutatása - 7
# teljes lista kiírás - 8

joLista = []
rosszLista = []
sorok = len(regies_nevek)
oszlopok = 2

# List comprehension módszer (EZ A JAVASOLT)
matrix = [[] * oszlopok for _ in range(sorok)]

# print(matrix)
while(True):
    print("\nlistagenerálás - 1\njó gyerekek listája - 2\nrossz gyerekek listája - 3\ngyerek hozzáadás - 4\nhatár gyerekek listája - 5\nlegjobb gyerek megmutatása - 6\nlegrosszabb gyerek megmutatása - 7\nteljes lista kiírás - 8")
    choice = input("\n\tChoose....")
    if(choice == "1"):
        for i in range(len(matrix)):
            matrix[i][0] = regies_nevek[i]
            matrix[i][1] = randrange(0,100)
            if(matrix[i][1] < 50):
                rosszLista.append(matrix[i][0])
            else:
                joLista.append(matrix[i][0])

    elif(choice == "2"):#jólistaKiírás
        for i in range(len(joLista)):
            print(joLista[i])

    elif(choice == "3"):#rosszlistaKiírás
        for i in range(len(rosszLista)):
            print(rosszLista[i])

    elif(choice == "4"):
        acceptable = False
        name = ""
        goodness = ""
        while(not acceptable):
            name = input("Childs name (more than 8 characters): ")
            goodness = int(input("Childs goodness in % (between 0 and 100)"))
            if(goodness >= 0 and goodness <= 100 and len(name)>=8):
                acceptable = True
       
        matrix.append([name, goodness])
        if(goodness < 50):
            rosszLista.append(name)
        else:
            joLista.append(name)
        print("The child has been added to the list")


    elif(choice == "5"):
        for i in range(len(matrix)):
            if(matrix[i][1] > 40 and matrix [i][1] < 60):
                print(f"{matrix[i][0]}, {matrix[i][1]}%")

    elif(choice == "6"):
        best = matrix[0][1]
        for i in range(1, len(matrix), 1):
            if(best < matrix[i][1]):
                best = matrix[i][1]

    elif(choice == "7"):
        worst = matrix[0][1]
        for i in range(1, len(matrix), 1):
            if(worst > matrix[i][1]):
                worst = matrix[i][1]

    elif(choice == "8"):
        for i in range(len(matrix)):
            print(f"{matrix[i][0]}, {matrix[i][1]}%")

    else:
        print("OutOfChoiceException.... Try again!")


        # print(matrix)

