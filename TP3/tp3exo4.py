n=int(input("Entrer un nombre entier :"))
b=input("Quelle boucle utiliser ? (for/while)")
f=1
if b=="for" :
    for i in range (1, n+1) :
        f *= i
        print(f)
elif b=="while" :
    j=1
    while j<=n:
        f *= j
        print(f)
        j += 1
else :
    b=input("Erreur de frappe, recommencez : ")