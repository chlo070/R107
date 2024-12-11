#Ecrire le programme qui détermine si la date est valide ou non en affichant un message.
#traiter jjmmaaaa comme une liste
#position 0=j1, position 1=j2, 2=m1, 3=m2, 4=a1, 5=a2, 6=a3, 7=a4

taille = 8
date=[]

#demander les valeurs de la position 0 à 2 exclu

jour = int(date [0:2])
mois = int(date [2:4])
annee = int(date [4:8])


while 0 > annee or annee > 9999 or 0 > mois or mois>12 or jour < 1 or jour > 31 :
    print("Date incorrecte, entrez une nouvelle date :")
    #ou msg = "Date incorrecte"
    #puis print(msg)

#Pour une année bisextile :
if mois == 2 :
    if (annee%4 == 0 and annee%100!=0) or (annee%100 == 0) :


