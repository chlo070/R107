

N = int(input("Merci de préciser le nombre de lignes : "))
etoile = "*"
"""
for i in range (1,N+1) :
    print(etoile * i)

print()
"""
espace = " "
ligneTriangle = ""
for i in range (N,0,-1) :
    for j in range (0,N) :
        ligneTriangle = (espace*j) + (etoile*i)
        print(ligneTriangle)

