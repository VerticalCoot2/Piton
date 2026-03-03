from os import system as s
s("cls")
# Mikulásnak szüksége van a seg(gítség)edre!
# írj egy programot, ami a nevek listából csinál egy mátrixot, amibe randomizálnod kell 1-100 ig egy "jóság" százalékot, ez alapján
# meg be kell rakni a jó, illetve a rossz listára. Ennek a feladatnak legyen "menüje"(számok segítségével ki lehessen választani,
# hogy éppen melyik listát mutassa meg) legyen egy olyan menüpont, ahol új embert lehet felvenni a listára. ott a felhasználónak
# kell megadnia az ember nevét, és jóság százalékát. ezek után sorolja be a program.legyen még egy kiíratás, ami a határon(40%<x<60%) állnak.


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