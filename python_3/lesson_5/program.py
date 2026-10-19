from os import system as s
from random import randrange as r

def main():
    s("cls")
    t = setup()
    print(*t)

    a = [input(f"give me the {i+1} name") for i in range(4)]

    m = tuple([tuple([a[i], r(0,61), r(10, 273), r(-2147483647, 2147483648), r(0, 265), r(0,215001)]) for i in range(len(a))])
    print(*m)

    d = {
        
        "name" : a[0],
        "footSize" : a[1],
        "height": a[2],
        "favouriteNumber" : a[3],
        "hoursSpentAwake" : a[4],
        "losesInFortnite" : a[5]
    }
    A(d)
    B(d)

def setup():
    name = input("name:\n")
    fs = float(input("\nfoot size:\n"))
    h = float(input("\nheight:\n"))
    fn = int(input("\nfavourite number: \n"))
    hsa = float(input("\nhours spent awake:\n"))
    fShit = int(input("\nlosses in fornite:\n"))
    return tuple([name, fs, h, fn, hsa, fShit])

def A(d):
    wrdCount = len(d["name"].split(" "))+1
    print(f"A névben lévő szavak száma: {wrdCount}")
    print(f"a nevek átlagos karakter száma: {sum([len(d["name"].split(" ")[i]) for i in range(len(wrdCount))])/wrdCount}")
    # print(f"a nevek átlagos karakter száma: {sum(map(len,d["name"].split(" ")))/len(d["name"].split(" ")) }")
    print(f"a nevek átlagos karakter száma: {sum([len(d["name"].split(" ")[i]) for i in range(len(wrdCount))])/wrdCount}")
        
def B(d):
    print((d["footSize"]*d["height"])/d["losesInFortnite"])

if __name__ == '__main__':
    main()