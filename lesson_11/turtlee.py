import turtle
t = turtle.Turtle()
t.color("blue")
t.speed(0)
i = 0
# while(True):
#     t.forward(i/100)
#     t.left(8)
#     i += 1
oldal = int(input("hány oldalú sokszög?\t"))
for i in range(oldal):
    t.forward(50)
    t.left(360/oldal)
while(True):
    t.forward(0)