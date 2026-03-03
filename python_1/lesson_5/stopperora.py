from os import system as s
from time import sleep
s("cls")

input("\n\tSTART\n")
sec = 0
min = 0
hour = 0
days = 0
years = 0

while(True):
    s("cls")
    print(f"years:{years}\tdays:{days} \t {hour}:{min}:{sec}")
    if(sec == 59):
        sec = 0

        if(min == 59):
            min = 0

            if(hour == 23):
                hour = 0

                if(days == 364):
                    days =0
                    years += 1

                else:
                    days += 1
            else:
                hour += 1
        else:
            min += 1
    else:
        sec += 1
    sleep(1)
