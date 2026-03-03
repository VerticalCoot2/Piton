from os import system as s
from random import randrange
import matplotlib.pyplot as plt

def main():
    numbers = []
    for i in range(20000):
        numbers.append(randrange(0,3))
    # names = ["Zero", "Two", "Four", "Six", "Eight"]
    names = ["Zero", "One"]
    quantity = []
    for i in range(0,2):
        quantity.append(numbers.count(i*2))
    plt.pie(quantity, labels=names, autopct="%.0f%%")
    plt.show()

if __name__ == '__main__':
    main()