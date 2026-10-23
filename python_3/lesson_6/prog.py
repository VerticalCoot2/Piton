from os import system as s

def main():
    s("cls")
    feladat2()

def feladat2():
    while(1):
        s("cls")
        print("Bejelentkezés menü\n\t1 - Regisztráció\n\t2 - Bejelentkezés")
        
        match (int(input("\n\t"))):
            case 1:
                s("cls")
                Register()

            case 2:
                s("cls")
                Login()

            case _:
                input("Nem sikerült, próbáld újra: [PRESS ENTER]")

def Register():
    email = ""
    rightFormat = False
    while (not rightFormat):
        text = input("email => format: name@domain.domainextension f.e.: Thomas@gmail.com\n\t")
        if("@" in text and not " " in text):
            t = text.split("@")
            if(t[0] != "" and t[1] != "" and t[0]):
                if("." in t[1]):
                    u = t[1].split(".")
                    if(u[0] != "" and u[1] != ""):
                        email = text
                        rightFormat = True
        if(not rightFormat):
            input("wrong format. Try again. [PRESS ENTER]")
    password = ""
    rightFormat = False
    specChar = ",-.?:_;<<>#&@{-}\\/'\"+!%=()[]>*"
    number= "0123456789"
    while(not rightFormat):
        text = (input("password => big, small characters, special characters, numbers\n\t"))
        if(text != text.upper() and text != text.lower()):
            if(any(a in specChar for a in text)):
                if(any(a in number for a in text)):
                    password = text
                    rightFormat = True
        if(not rightFormat):
            input("wrong format. Try again. [PRESS ENTER]")
    TextAppendLI(email, password)
    input("Sikeres regisztráció! [PRESS ENTER]")

def TextAppendLI(email, password):
    a = open("loginInfo.txt", "a", encoding="utf-8")
    a.write(f"{email};{password}\n") #a pontos vessző nem jó megoldás
    a.close()

def Login():
    pass

if(__name__ == "__main__"):
    main()