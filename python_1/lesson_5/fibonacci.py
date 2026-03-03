from os import system as s
from time import sleep

s("cls")

num1 = 0
num2 = 1
num3 = num1+num2
input()
print(num1)
print(num2)
input()
print(num3)
print()
while(True):
    input()
    num1 = num2
    num2 = num3
    num3 = num1+num2
    print(num3)

