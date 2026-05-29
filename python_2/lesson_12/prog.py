from os import system as s

def main():
    s("cls")
    f = open('D:/LSC/Piton/python_2/lesson_12/tekszt.txt', "r", encoding="utf-8") # r -> read; a -> append; w -> write
    tekszt = f.read()
    print(tekszt)


    # f = open('D:/LSC/Piton/python_2/lesson_12/tekszt.txt', "a", encoding="utf-8") # r -> read; a -> append; w -> write
    # f.write("\nDe kapott egy jó állás ajánlatot a Cloud9-nál, mert ők is szarok.")
    # f.close()

    # f = open('D:/LSC/Piton/python_2/lesson_12/tekszt.txt', "w", encoding="utf-8") # r -> read; a -> append; w -> write
    # f.write("Teó a legjobb Siege player, de sakkozni, ha megölik sem tud.")
    # f.close()

    # f = open('D:/LSC/Piton/python_2/lesson_12/tekszt.txt', "r", encoding="utf-8") # r -> read; a -> append; w -> write
    # lista = f.read()
    # f.close()
    # lista = [int(i) for i in range(len(lista))]
    # print(type(lista), lista)

    f = open('D:/LSC/Piton/python_2/lesson_12/matrix.csv', "w", encoding="utf-8") # r -> read; a -> append; w -> write
    szam = 1
    for i in range(10):
        for j in range(10):
            if(j<9):
                f.write(f"{szam};")
            else:
                f.write(f"{szam}")
            szam += 1
        f.write("\n")
    f.close()


if __name__ == "__main__":
    main()

import random
a = [random.randint(1,5) for _ in range(10)]
print(a)
print(sorted(list(set(a)),reverse=True)[1])
M = -1
for elem in a:
    if elem > M:
        M = elem

M2 = -1
for elem in a:
    if elem > M2 and elem != M:
        M2 = elem
print(M2)