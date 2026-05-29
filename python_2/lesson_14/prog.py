from os import system as s

m = []
def main():
    s("cls")
    beolvas()
    kiir()

def beolvas():
    be = open("D:\LSC\Piton\python_2\lesson_14\Lesson_14_csv_files\olympics.csv", "r", encoding="utf-8")
    data = be.readlines()
    be.close()
    for i in range(2, len(data)):
        tempList =[]
        
        #Algeria (ALG),12,5,2,8,15,3,0,0,0,0,15,5,2,8,15
        
        line = data[i].split(",")
        
        tempList.append(line[0])

        tempList.append([line[j] for j in range(1,4)])
        tempList.append([line[j] for j in range(5,8)])
        tempList.append([line[j] for j in range(9,12)])

        tempList.append(line[4])  #Ssum
        tempList.append(line[8])  #Wsum
        tempList.append(line[12]) #Gsum
        
        tempList.append(line[13]) #SumSum

        m.append(tempList)

def kiir():
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=", " if j!=len(m[i])-1 else "\n")
        

if __name__ == '__main__':
    main()