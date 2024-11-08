n=int (input("Rentrez un nombre :"))
if n<0 :
    if n%2==0 :
        print(n, " est un nombre négatif et pair.")
    else :
        print(n, " est un nombre négatif et impair.")
if n>0 :
    if n%2==0 :
        print(n, " est un nombre positif et pair.")
    else :
        print(n, " est un nombre positif et impair.")
else :
    print(n, " vaut 0.")