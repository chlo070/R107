n=int (input("Entrez un nombre entier :"))
if n<0 :
    if n%2==0 :
        print("Le nombre négatif et pair.")
    else :
        print(n, " est un nombre négatif et impair.")
elif n>0 :
    if n%2==0 :
        print(n, " est un nombre positif et pair.")
    else :
        print(n, " est un nombre positif et impair.")
else :
    print("Le nombre est 0 (et il est pair).")