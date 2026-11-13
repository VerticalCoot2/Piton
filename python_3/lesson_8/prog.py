from os import system as s
from random import randrange as r

def main():
    s("cls")
    rounds = 0
    wins = 0


    wList = readWords()
    # print(wList)
    wannaPlay = True
    while(wannaPlay):
        score = game(wList)
        if(score[0] == 1):
            wins+=1
        rounds+=1
        print(f"The word was: {score[1]}Score:\nWins:\t{wins}\tLoses:\t{rounds-wins}\nWin rate:\t{((wins / rounds) * 100)}%")
        if (input("Abba akarja hagyni? (i;n)\n") == "i"):
            wannaPlay = False
            


def game(bank):
    life = 10
    win = False
    word = bank[r(0,len(bank))].lower()
    goodGuesses = []
    badGuesses = []
    wordHash = []
    for i in range(len(word)):
        if(word[i] not in wordHash):
            wordHash.append(word[i])
    # print(wordHash)
    
    displayWord = secretifyWord(word, goodGuesses)
    
    print (displayWord)
    while(life >= 0 and win == False):
        s("cls")
        displayWord = secretifyWord(word, goodGuesses)
        print(word)
        print(displayWord)
        print(f"wrong letters: {badGuesses}\nlife: {life}/10")
        guess = input("Your next guess(a single letter): ").lower()
        if(guess in word):
            goodGuesses.append(guess)
            win = hasEveryChar(wordHash, goodGuesses)
        else:
            badGuesses.append(guess)
            life -= 1

    if(win):
        return [1, word]
    else:
        return [0, word] 

def secretifyWord(word, list):
    text = ""
    for i in range(len(word)):
        if(word[i] in list):
            text += f"{word[i]} "
        else:
            text += "_ "
    return text

def hasEveryChar(hashList, guessList):
    has = True
    index = 0
    while (has and index < len(hashList)):
        if(hashList[index] in guessList):
            index+=1
        else:
            has = False
    return has
 

def readWords():
    with open("D:\LSC\Piton\python_3\lesson_8\szavak.csv", mode="r", encoding="utf-8") as a:
        lista = a.read().strip().split(";")
    return lista


if(__name__=='__main__'):
    main()