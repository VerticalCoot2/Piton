from os import system as s
from time import sleep

s("cls")

# print("egy")
# sleep(1)
# print("kettő")
# sleep(1)
#írjatok egy olyan kódot, ami elszámol 60mp ig, és utána megáll

for i in range(60, 0, -1):
    s("cls")
    print(i)
    sleep(1)
s("cls")
print("lejárt az idő")