tab=[5,2,4,8,1,3]


#Partie 1 avec print(sorted(tab))
for i in range (len(tab)) :
    for j in range (len(tab)-1):
        if j < i :
            temp = tab[i]
            tab[i]=tab[j]
            tab[j]=temp
    print(tab)

print(sorted(tab))


#Partie 2 avec tab.sort()