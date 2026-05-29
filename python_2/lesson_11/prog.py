from os import system as s

def main():
    s("cls")
    list1 = []
    for i in range(int(input("Hány diák pontjait nézzuk?\t"))):
        list1.append(int(input(f"írj be a(z) {i+1}. számú diák pontját (0-100): ")))
    tupleList = []

    for i in range(len(list1)):
        grade = 5 if list1[i] >= 85 else 4 if list1[i] >= 70 else 3 if list1[i] >= 55 else 2 if list1[i] >= 40 else 1    
        tupleList.append(tuple((list1[i], grade)))
    tupleList = tuple(tupleList)
    # print(type(tupleList), tupleList)

    #task1
    minMax = task1(tupleList)
    print(f"\nA legkisebb érték {minMax[0]} pont\nA legnagyobb érték {minMax[1]} pont")

    #task2
    avarages = task2(tupleList)
    print(f"\nAz átlag pontszám {avarages[0]} pont\nA jegyek átlaga: {avarages[1]}")

    #task3
    nl = task3(tupleList)
    print("Osztályzat darabszámok:\n")
    for i in range(len(nl)):
        print(f"{nl[i][0]} osztályzatból {nl[i][1]}db van.")

    #task4
    lessMost = task4(nl)
    print(f"\nA legtöbb jegy {lessMost[1]}-ból/ből van\nA legkevesebb jegy {lessMost[0]}-ból/ből van")

def task1(tl):
    min = tl[0][0]
    max = tl[0][0]
    for i in range(1, len(tl)):
        max = tl[i][0] if (tl[i][0] > max) else max
        min = tl[i][0] if (tl[i][0] < min) else min
    return tuple((min, max))

def task2(tl):
    avgP = 0 #avg point
    avgG = 0 #avg grade
    for i in range(len(tl)):
        avgP += tl[i][0]
        avgG += tl[i][1]
    return tuple((avgP/len(tl), avgG/(len(tl))))

def task3(tl):
    numList = [[i, 0] for i in range(1,6)]
    for i in range(len(tl)):
        numList[tl[i][1]-1][1] += 1
    return(tuple(numList))

def task4(nl):
    legtobb = nl[0][0]
    legkevesebb = nl[0][0]
    for i in range(1,len(nl)):
        
        if(nl[i-1][1] < nl[i][1]):
            legtobb = nl[i][0]

        if((nl[i-1][1] > nl[i][1]) and not 0):
            legkevesebb = nl[i][1]
    return(tuple((legkevesebb, legtobb)))

if __name__ == '__main__':
    main()