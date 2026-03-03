from os import system as s
import matplotlib.pyplot as plt

def main():
    n = int(input("Hány játékot szeretsz?\n"))
    games = []
    likes = []
    data = []
    db = s = 0

    for i in range(n):
        game_name = input(f"What the name of {i+1} game?")
        like = int(input("1-10 ig mennyire szereted?"))
        db += like
        games.append(game_name)
        likes.append(like)

    for i in range(n):
        s = likes[i]/db * 100
        s = round(s,1)
        data.append(s)
    
    piechart(data, games)


def piechart(size, lab):
    plt.pie(size, labels = lab, autopct = '%.2f%%')
    plt.show()

if __name__ == '__main__':
    main()