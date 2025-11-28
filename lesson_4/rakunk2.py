#írj egy kódot, amely bekér egy számot ezt nevezzük 'x' nek, majd még egyet, ezt nevezzük 'y' nak, majd a program írja ki, hogy x osztható-e y-al

from os import system as s
s("cls")

x = int(input("kérem az egyik számot: "))
y = int(input("kérem a másik számot: "))
if(y == 0):
    print("0-val nem osztunk")
elif(x == 0):
    print("A nullának végtelen sok osztója van")
elif(x%y == 0):
    print(f"A(z) {y} osztója {x}-nek")
else:
    print(f"A(z) {y} nem osztója {x}-nek")