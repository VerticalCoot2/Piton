from os import system as s
import numpy as np
import pendulum as p
import datetime
import time

from MyPackages import bob

def main():
    s("cls")
    # print(bob.BobSummarise(33,14))
    # print(bob.Negyzetreemeles(2, 5))


    # lista = [1,2,3,5,7,11,30,80,7842,6]
    # print(bob.Talald_Meg_a_Primeket(lista))

    m = bob.MatrixKreacio()
    print()
    matrix(m)
    # TimeZones()



def TimeZones():
    cities = ['Europe/Budapest',
              'Europe/London',
              'Europe/Paris',
              'America/New_York',
              'America/Toronto',
              'America/Vancouver',
              'Australia/Sydney']
    times = []

    for city in cities:
        now = p.now(city)
        now = now.to_datetime_string()
        times.append(now)

    for i in range(len(cities)):
        print(f"{cities[i].split('/')[1]}\ttime: {times[i]}\n")

def matrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=" ")
        print()

if __name__ == '__main__':
    main()