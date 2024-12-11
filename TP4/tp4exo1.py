n=float(input("Vous cherchez la table de multiplication de quel nombre ?:"))
table=[]
i=0
for i in range (10) :
    res= round(n * i,1)
    table.append(res)

print(table)
for i in range(10):
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


