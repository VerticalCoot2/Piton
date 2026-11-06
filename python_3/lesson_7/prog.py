from os import system as s
true = True
false = False

def main():
    s("cls")
    # x = 15
    # y = 2
    # print(5>>2)
    task1()

def task1():
    maxBricks = int(input("Hány téglából épjtsünk piramist?\t"))
    index = 0
    done = false
    bricksUsed = 0
    
    while(not done):
        if(0>(maxBricks-index)):
            done = true
        else:
            maxBricks-=index
            bricksUsed += index
            index += 1
            # print(f"{maxBricks}\n{bricksUsed}\n{index}\n")

    remainingBricks = maxBricks
    levels = index-1
    print(f"A torony {levels} szintes lett, {bricksUsed}db tégla felhasználásával. ennyi tégla maradt: {remainingBricks}")




if (__name__ == "__main__"):
    main()