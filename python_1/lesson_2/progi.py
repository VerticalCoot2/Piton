from os import system as s


s("cls")

szoveg = input("Kérlek írj egy szöveget:\n")

if szoveg.isupper():
    print(szoveg.lower())
else:
    print(szoveg.upper())


# karakter = input("Melyik karaktert akarod összeszámolni?\t")

# print(f"a szövegben ennyi '{karakter}' betű van: {szoveg.count(karakter)}")






# print(szoveg.__len__())
# print(szoveg.split(" ")[0])

# if szoveg.count("a") == 3:
#     print("3 a van benne")

# elif szoveg.count("a") == 4:
#     print("4 a van benne")

# else:
#     print("nem 3, vagy 4 a van benne")