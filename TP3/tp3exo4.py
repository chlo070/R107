n=int(input("Entrer un nombre entier :"))
b=input("Quelle boucle utiliser ? (for/while) : ")
f=1
while b!="for" and b!="while":
    b = input("Erreur de frappe, recommencez (for/while) : ")

if b=="for" :
        for i in range (1, n+1) :
            f *= i
            print(f)
else :
        j=1
        while j<=n:
            f *= j
            print(f)
            j += 1
