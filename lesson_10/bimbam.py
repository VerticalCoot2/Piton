from os import system as s
s("cls")

for i in range (1,51):
    oszthato = i%3 == 0
    harmasKarakter = "3" in str(i)
    if(oszthato and harmasKarakter):
        print("bimbam") 
    elif(oszthato):
        print("bim")
    elif(harmasKarakter):
        print("bam")
    else:
        print(i)