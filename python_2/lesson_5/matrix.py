from os import system as s
from random import randrange

def main():
    s("cls")
    f5()

def f1():
    m = [[1,2,3, 84, 78, 31, 7],
         [4],
         [7,8,9, 3, 0, 1]]    
    # print(m)
    f2(m)
def f2(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=" ")
        print()

def f3():
    m = []
    for i in range(5):
        m.append([])
        for j in range(5):
            m[i].append(j)
    print(m)

def f4():
    mRows = int(input("Hány sora legyen?\n"))
    mLength = int(input("Milyen hosszúak legyenek a sorok?\n"))
    m = []
    for i in range (mRows):
        m.append([])
        for j in range(mLength):
            m[i].append(randrange(0,101))
    f2(m)

def f5():
    baratok = ["Tamás", "Teó", "Áron", "Dóri", "Boti"]
    kaloriak = [[], [], [], [], []]

    for i in range (len(baratok)):
        for j in range(10):
            kaloriak[i].append(randrange(50,401))

    for i in range(len(baratok)):
        print(f"[{baratok[i]}]: ", end= "\t")
        for j in range(len(kaloriak[i])):
            print(f"{kaloriak[i][j]}kcal", end= " ")
        print()

    print("\nÖsszkalóriák:\n")    
    
    for i in range(len(baratok)):
        sum = 0
        for j in range(len(kaloriak[i])):
            sum += kaloriak[i][j]
        print(f"[{baratok[i]}]: {sum}kcal")


if __name__ == '__main__':
    main()