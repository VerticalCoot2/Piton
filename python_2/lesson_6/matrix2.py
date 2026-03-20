from os import system as s
from random import randint
import math

def main():
    s("cls")
    # f1()
    # f2()
    # f3()
    # f4()
    f5()

def f1(): #lisztkomprehensön
    a = []
    for i in range(4,10):
        a.append(i)
    print(*a)

    b = [x for x in range(4,10)]
    print(*a)

def f2():
    # a = []
    # for i in range(0, 100, 2):
    #     a.append(i)

    # a = [x for x in range(0, 100, 2)]

    # a = []
    # for i in range(100):
    #     if(i % 2 == 0):
    #         a.append(i)
    
    a = [x for x in range(100) if x%2 == 0]
    
    
    print(*a)
    
def f3(): #Mátrix generál listkomprehension
    m1 = [[i for i in range(10)] for j in range(10)]
    matrix(m1)
    print()
    m2 = [[j for i in range(10)] for j in range(10)]
    matrix(m2)

def f4():
    m = [[i ** 4 + j for i in range(10)] for j in range(30)]
    matrix(m)

def f5():
    #WeatherCalculator
    month = [[randint(-5,32) for i in range(0, 24)] for j in range(30) ]
    matrix(month)


    daysAvgTemp = []
    for i in range(len(month)):
        avg = 0
        for j in range(len(month[i])):
            avg += month[i][j]
        daysAvgTemp.append(round(avg/len(month[i]),2))

    daysHighestTemp = [max(month[x]) for x in range(len(month))]

    allTimeHigh = max(daysHighestTemp)

    print(f"\nDays avarage temp.:\t{daysAvgTemp}\n\nDays highest temp.:\t{daysHighestTemp}\n\nAll time highest temp.:\t{allTimeHigh}")


def matrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=" ")
        print()


if __name__ == '__main__':
    main()