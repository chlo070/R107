nMax = 3
v1 = []
v2 = list()
n = int(input("Quelle est la taille de vos vecteurs [entre 1 et 3] ? :"))
while nMax < n or n < 1:
    n = int(input("La taille de vos vecteurs n'est pas conforme, réessayez :"))

print("Saisie du premier vecteur :")
for i in range(0, n):
    argument = float(input(f"v1[{i}]="))
    v1.append(argument)

print("Saisie du second vecteur :")
for i in range(0, n) :
    argument = float(input(f"v2[{i}]="))
    v2.append(argument)

produit = 0
resultat = 0
for i in range(0, n-1):
    produit = v1[i]*v2[i]
    resultat = round(resultat + produit, 0)

print("Le produit scalaire de v1 par v2 vaut", resultat)



#exemple:
#Quelle est la taille de vos vecteurs [entre 1 et 10] ? 3
#Saisie du premier vecteur :
#v1[0] = 2
#v1[1] = 3
#v1[2] = 4
#Saisie du second vecteur :
#v2[0] = 1
#v2[1] = 3
#v2[2] = 7


#print("Le produit scalaire de v1 par v2 vaut", 39.0)
#