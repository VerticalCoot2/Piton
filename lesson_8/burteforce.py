from os import system as s
s("cls")

#írj egy programot, ami bekér a felhasználótól
#egy 4 jegyű számot, és növeli 1-el egy számot,
# amíg el nem éri a megadott számot.

szam = int(input("Gondolj egy négyjegyű számra a természetes számok halmazán: "))
megvan = False
guess = 1000
while(megvan == False):
    if(guess != szam):
        guess += 1

    else:
        megvan = True
    print(guess)
print(f"A szám, amire gondoltál a(z) {guess}. összesen {guess-1000} próbálkozásból lett meg!")