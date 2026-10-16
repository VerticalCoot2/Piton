from os import system as s

def main():
    #írjatok egy olyan egyszerű progit, ami bekér egy szöveget, és nagybetűvel kiírja

    szotar = {"cat": "Katze",
              "dog": "hund",
              "horse": "pferd",
              "Military vehichle": "Panzerkampfwagen"}

    print(szotar['cat'])

    szotar["cat"] = "nev"

    print(szotar)

def kulcskerese(szotar):
    for key in szotar.keys():
        print(key, "->", szotar[key])
    print("Rombikozidodekaéder")
    print("Fekete bikapata kopog a patika pepita kövezetén.")
    print("jobb egy lúdnyak tíz tyúknyaknál")
    print("Cirkuszi csibecombcsont")


if(__name__ == "__main__"):
    main()