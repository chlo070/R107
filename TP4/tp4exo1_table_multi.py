n=float(input("Vous cherchez la table de multiplication de quel nombre ?:"))
table=[]
i=0
for i in range (1,11) :
    res= round(n * i,1)
    table.append(res)
for i in range(1,11):
    print(f"{n} * {i} = {table[i]}")


#round(x,n)
#exemple de sortie :Vous cherchez la table de multiplication de quel nombre ?
#1.2 * 0 = 0.0
#1.2 * 1 = 1.2
#1.2 * 2 = 2.4
#1.2 * 3 = 3.6
#1.2 * 4 = 4.8
#1.2 * 5 = 6.0
#1.2 * 6 = 7.2
#1.2 * 7 = 8.4
#1.2 * 8 = 9.6
#1.2 * 9 = 10.8

#Question du Quiz :
#nbr = float(input("Vous chercher la table de multiplication de quel nombre ? "))
#L = []
#for i in range(10):
#    L.append(nbr*float(i))
#    print(f"{nbr} * {i} = {L[i]}")

