#min,max,sort: key
#függvények: lambda, argumentum/paraméter alapértelmezett érték - pédák: átváltók

import random
a = []
for i in range(10):
    a.append(random.randint(1,10))
a = [random.randint(1,10) for i in range(10)]
print(a)


#maximum (minimum) keresés
m = 0#olyan szám, ami mindennél kisebb (nagyobb) - általános megoldás: lista egyik eleme
for elem in a:
    if elem > m: #(<)
        m = elem
print(max(a))

n = ["Dóri","Huba","Boti","Tomi","Áron","Teó","Kadosa","Imi","Tibi"]
print(max(n,key=len))
m = n[0]
for elem in n: 
    if len(elem) > len(m): # len("Dóri") > len("Huba")
        m = elem
print(m)

n.sort(key=len)
print(n)

#keressük meg a legtöbb i betűt tartalmazó nevet!
def kacsa(x): # function kacsa(x){}
    return x.lower().count("i")
print(max(n,key=kacsa))

#lambda függvények: egysoros függvények amik visszatérnek
kacsa_l = lambda x: x.lower().count("i")

#lambda függvények felhasználása: max (és hozzá hasonló függvényekben) key-nek kiváló mert nem kell neki feleslegesen envet adni
print(max(n, key= lambda x: x.lower().count("i"))) 

def CentigradeFarenheit(deg,scale="C"):
    if scale == "C":
        return deg*1.8+32
    if scale == "F":
        return (deg-32)/1.8

print(CentigradeFarenheit(100,"F"))# 100 F -> C
print(CentigradeFarenheit(100))# 100 C -> F