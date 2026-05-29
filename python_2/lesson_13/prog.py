from os import system as s
 
def main():
    s("cls")
    path = 'D:/LSC/Piton/python_2/lesson_13/Lesson_13_csv_files/secret_santa.csv'
    data = matrixRead(path, "r")
    
    wannaSearch = True if (input("Keresi valakinek az E-mail címét? ('i' => igen,akármi más => nem)") == "i")  else False
    
    
    while(wannaSearch):
        name = input("Kit keres?(nevet írjon be): ")
        index = 0
        meagvan = False
        while(not meagvan and index < len(data)):
            if(data[index][0] == name):
                meagvan = True
            else:
                index += 1
        if(meagvan):
            print(f"Van ilyen ember. az E-mail címe: {data[index][1]}\n")
        else:
            print("Nincs ilyen nevű ember.\n")
        wannaSearch = True if (input("Keresi még valakinek az E-mail címét? ('i' => igen,akármi más => nem): ") == "i")  else False
    
    
    hozzaAdas = True if (input("Szeretne hozzáadni új embert? ('i' => igen,akármi más => nem)") == "i") else False
    while(hozzaAdas):
        nev = input("Név: ")
        email = input("e-mail: ")
        NewPerson(path, nev, email)
        hozzaAdas = True if (input("Szeretne hozzáadni még egy új embert? ('i' => igen,akármi más => nem)") == "i") else False
    
    for i in range(len(data)):
        print(f"{data[i][0]}\t{data[i][1]}")
            

def matrixRead(fp, t): #fn => File path t => open type(r, a, w)
    f = open(fp, t, encoding="utf-8")
    lines = f.readlines()
    f.close()
    m = []

    for i in range(1, len(lines)):
        list = []
        line = lines[i].split(", ")
        for j in range(len(line)):
            list.append(line[j].replace('"', "").strip())
        m.append(list)
    
    return m

def NewPerson(path, name, email):
    f = open(path, "a", encoding="utf-8")
    f.write(f'\n"{name}", "{email}"')
    f.close()
    







if __name__ == "__main__":
    main()