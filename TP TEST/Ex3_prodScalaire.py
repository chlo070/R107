#Initialisation & conditions
v1=[]
v2=[]
def produit_scalair() :
    v1=list(input("Merci de saisir les composantes du vecteur V1, séparés par des virgules (exemple : 3,4,11,3,13):"))
    v2=list(input("Merci de saisir les composantes du vecteur V2, séparés par des virgules :"))
    while len(v1) == 1 or len(v2) == 1 :
        print("Un des deux vecteurs est composé d'un seul élément ou bien un autre séparateur a été utilisé")
        return(-1)
    while len(v1) != len(v2) :
        print("Les deux vecteurs ne sont pas de même taille")
        return(-2)

#Calcul scalaire
produit = 0
resultat = 0
for i in range(0, len(v1)):
    produit = v1[i]*v2[i]
    resultat = round(resultat + produit, 0)
print("Le produit scalaire de v1 par v2 vaut", resultat)

"""
"""
