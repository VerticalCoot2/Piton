from os import system as s
from random import randint

def main():
    s("cls")
    options = ["Scissors", "Paper", "Rock"]
    win = lose = tie = 0
    round = 1
    while(True):
        print(f"Round {round}")
        userInput = input("Choose: Rock, Paper, Scissors\t(type it in)\n")
        game = MiniGame(options, userInput)

        match(game):
            case 0:
                print("Tie.")
                tie += 1
                break
            
            case 1:
                print("You won.")
                win += 1
            
            case 2:
                print("You lost.")
                lose += 1

        print(f"Stats\n\tWins: {win}\n\tLoses: {lose}\n\tTies: {tie}")
        round += 1

def MiniGame(options, playerChoice):
    compChoice = options[ randint(0, len(options)-1) ]
    print(f"Computer choice: {compChoice}")

    if(compChoice == playerChoice): #tie
        return 0
    
    elif (playerChoice == options[0] and compChoice == options[1]) or (playerChoice == options[1] and           compChoice == options[2]) or (playerChoice == options[2] and compChoice == options[0]): #user win
        return 1
    
    return 2 # user lose
        

if __name__ == '__main__':
    main()