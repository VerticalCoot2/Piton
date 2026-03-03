from os import system

# írjunk egy olyan brogramot ami bekéri, hogy hány oldalú sokszöget szeretnénk, és megrajzolja
a = int(input())

import turtle
t = turtle.Turtle()
t.speed(5)

for i in range(a):
    t.forward(1000/a)
    t.left(360/a)
input()