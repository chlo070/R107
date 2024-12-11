#Ecrire le programme qui détermine si la date est valide ou non en affichant un message.
#traiter jjmmaaaa comme une liste
#position 0=j1, position 1=j2, 2=m1, 3=m2, 4=a1, 5=a2, 6=a3, 7=a4

taille = 8
date=[]
msg = "date correcte"

#demander les valeurs de la position 0 à 2 exclu
jour = int(jjmmaaaa[0]*10 + jjmmaaaa[1])
jour = int(input(date [0:2]))
mois = int(input(date [2:4]))
annee = int(input(date [4:8]))

print (f{jour}/{mois}/{annee})

while 0 > annee or annee > 9999 or 0 > mois or mois>12 or jour < 1 or jour > 31 :
    print("Date incorrecte, entrez une nouvelle date :")
    #ou msg = "Date incorrecte"
    #puis print(msg)
    jour = int(input("Quel est le jour?:"))
    jour = int(input(date[0:2]))
    mois = int(input(date[2:4]))
    annee = int(input(date[4:8]))

#Pour une année bisextile :
if mois == 2 :
   if ((annee%4 == 0 and annee%100!=0) or annee%400 == 0) :
       if (1 <= jour and jour <= 29)


#lilste des mois à 31jrs
m31=[1,3,5,7,8,10,12]




#autre methode
date = input ("Entrez une date de la forme jjmmaaaa :")
jour = int(date[0:2])
mois = int(date[2:4])
annee = int(date[4:8])