from os import system as s

s("cls")

nev = input("Kérlek írj be egy nevet: ")
kor = int(input("Kérlek add meg, hány éves: "))

print(f"A név: {nev}")
print(f"A kora: {kor}")

print(f"Ő itt {nev}, és {kor} éves.")

print(f"Két év múlva ennyi ifős lesz: {kor + 2}")