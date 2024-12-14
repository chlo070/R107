#Ecrire le programme qui détermine si la date est valide ou non en affichant un message.
#traiter jjmmaaaa comme une liste
#position 0=j1, position 1=j2, 2=m1, 3=m2, 4=a1, 5=a2, 6=a3, 7=a4


msg = "date correcte"

date=input("Quelle est la date?:")
jour = int(date[0])*10 + int(date[1])
mois = int(date[2])*10 + int(date[3])
annee = int(date[4])*1000 + int(date[5])*100 + int(date[6])*10 + int(date[7])

print (f"{jour}/{mois}/{annee}")

while 0 > annee or annee > 9999 or 0 > mois or mois>12 or jour < 1 or jour > 31 :
    print("Date incorrecte, entrez une nouvelle date :")
    jour = int(date[0]) * 10 + int(date[1])
    mois = int(date[2]) * 10 + int(date[3])
    annee = int(date[4]) * 1000 + int(date[5]) * 100 + int(date[6]) * 10 + int(date[7])


#Pour mois à 30j (liste)
m30=[4,6,9,11]
if mois != m30 :
    if jour > 30:
        msg = "date incorrecte"
    else:
        msg = "date correcte"
#Pour une année bisextile + mois de février:
elif mois == 2 :
   if (annee%4 == 0 and annee%100!=0) or annee%400 == 0 :
       if jour > 29 :
           msg = "date incorrecte"
       else :
           msg = "date correcte"
   else :
       if jour > 28:
           msg = "date incorrecte"
       else:
           msg = "date correcte"


print(msg)

"""
#autre methode

#demander les valeurs de la position 0 à 8 exclu
date = input ("Entrez une date de la forme jjmmaaaa :")
jour = int(date[0:2])
mois = int(date[2:4])
annee = int(date[4:8])

print (f"{jour}/{mois}/{annee}")
"""