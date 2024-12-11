L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
#Partie1
n = len(L1)
occurence = 0
maxOcc=0
maxIndice = 0
for i in range (n) :
    for j in range (i+1, n) :
        if L1[i] == L1[j] :
            occurence += 1
            if occurence > maxOcc :
                maxOcc = occurence
                MaxIndice = L1[i]

L1.index(maxIndice)

print(f"Le nombre le plus frequent dans la liste est le : , {maxIndice} ({occurence} x)")


#Partie2
n = len(L1)
count()



""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
#Question du Quiz :
#L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
#a = -1
#b = 0

#for i in range( ?? ):
#    if L1. ?? > b and ?? :
#        a = L1[i]
#        b = ??

#print(f"Le nombre le plus frequent dans le tableau est le : { ?? } (il apparait { ?? })")