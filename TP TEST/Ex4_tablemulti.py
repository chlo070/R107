#saisir un nombre, entier ou réel, et renvoyer une liste contenant les résultats de la table de multiplication de ce nombre.
table = []
n = float(input("Vous cherchez la table de multiplication de quel nombre ?:"))
def tabl_multi():
    for i in range(1, 11):
        res = round(n * i, 1)
        table.append(res)
print("Voici la table de multiplication de", n)
for i in range(1, 11):
    print(f"{n} * {i} = {table[i]}")
    return (L)

"""
#fonction qui prend en argument une liste L et qui affiche la table de multiplication à partir de cette liste.
L=[]
def affich_table(L):
    
"""