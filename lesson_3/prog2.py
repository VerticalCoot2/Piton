from os import system as s

s("cls")

num1 = float(input("Kérem az első számot: "))
num2 = float(input("Kérem a második számot: "))

while(True):
    s("cls")
    choice = input("Milyen műveletet végezzek el? \nösszeadás:\t\'+\' \nkivonás:\t\'-\'\nszorzás:\t\'*\'\nosztás:\t\t\'/\'\nm. osztás:\t\'%\'\nn.m. osztas2:\t\'//\'\nhatványozás:\t\'**\'\n")

    if(choice == "+"):
        print(f"{num1} {choice} {num2} = {num1 + num2}")

    elif (choice == "-"):
        print(f"{num1} {choice} {num2} = {num1 - num2}")

    elif (choice == "*"):
        print(f"{num1} {choice} {num2} = {num1 * num2}")

    elif (choice == "/"):
        print(f"{num1} {choice} {num2} = {num1 / num2}")

    elif (choice == "%"):
        print(f"{num1} {choice} {num2} = {num1 % num2}")

    elif (choice == "**"):
        print(f"{num1} {choice} {num2} = {num1 ** num2}")

    elif (choice == "//"):
        print(f"{num1} {choice} {num2} = {num1 // num2}")
    else:
        s("cls")
        print("Valamit elkúrtál!")
        input()
        s("cls")
        print("NAGYON!")
    input()