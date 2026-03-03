from os import system as s
from random import randrange as r


def q1():
    valasz = False
    while(not valasz):
        if(int(input("1+1?")) == 2):
            valasz = True
    input("Mehetsz tovább!")
def q2():
    print("2")
    input()
def q3():
    print("3")
    input()
def q4():
    print("4")
    input()
def q5():
    print("5")
    input()
def q6():
    print("6")
    input()
def q7():
    print("7")
    input()
def q8():
    print("8")
    input()
def q9():
    print("9")
    input()
def q10():
    print("10")
    input()
def q11():
    print("11")
    input()
def q12():
    print("12")
    input()
def q13():
    print("131")
    input()
def q14():
    print("14")
    input()
def q15():
    print("15")
    input()
def q16():
    print("16")
    input()
def q17():
    print("17")
    input()

funcList = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17]


def main():
    s("cls")
    usedindexes = [0]
    while len(usedindexes) != 7:
        num = r(0,len(funcList))
        if num not in usedindexes:
            usedindexes.append(num)

    print(usedindexes)
    for i in range(len(usedindexes)):
        print(f"\n{i+1}. szoba:\n")
        funcList[usedindexes[i]]()
        
    
    




if __name__ == '__main__':
    main()