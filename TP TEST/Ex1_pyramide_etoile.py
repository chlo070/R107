

N = int(input("Merci de préciser le nombre de lignes : "))
etoile = ['*']

for i in range(1, N+1) :
    print(etoile * i)
print()

listEspace=[]
ligneTriangle = []

print(etoile)
for i in range(len(etoile)) :
    listEspace.append(' ')
    etoile.remove(etoile[-1])
    ligneTriangle.append(listEspace[i], etoile[i])
    print(ligneTriangle)
""""""
