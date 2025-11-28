from os import system as s
from getpass import getpass
s("cls")

correct = False
while(not correct):
    password = getpass("Please insert the password.")
    print(password)
    # password = input("Password: ")
    if(len(password) >= 6 and len(password) <= 16 ):
        caps = False
        lower = False
        num = False
        specChar = False
        i = 0

        while(i < len(password) and (not caps or not lower or not num or not specChar)):
            if(password[i].isnumeric()):
                num = True

            elif(password[i].isupper()):
                caps = True

            elif(password[i].islower()):
                lower = True

            elif(password[i] in "$@#&!-_"):
                specChar = True

            i+=1
        if(caps and lower and num and specChar):
            correct = True
        else:
            input("Your password is incorrect. Password requirements:\n\t-Upper case character\n\t-Lower case character\n\tAt least 6 characters\n\t-Less than 17 character\n\t-A special character($ @ # & ! - _)\n\t-A number\n\npress ENTER to restart.")
    else:
        input("The password is too short/long. Please try again...\npress ENTER to restart.")
print("Your password is correct, and had been saved.")