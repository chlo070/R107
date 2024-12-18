N = int(input("Merci de préciser le nombre souhaité : "))

while N != int :
    N = int(input("Erreur saisissez un nombre entier : "))

ligne=[]
for i in range (1, N+1) :
        ligne.append(i)
        print(ligne)
print()
ligne.reverse()
print(ligne)
for i in range (len(ligne)-1):
        ligne.remove(ligne[0])
        print(ligne)


