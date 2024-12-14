print("De quelle heure à quelle heure se fait la location?")
debut=int(input("Heure de début (un entier) :"))
fin=int(input("Heure de fin (un entier) :"))
temps=fin-debut
tarif1=0
tarif2=0

        
while debut == fin or debut > 25 or fin < 0 or debut > fin :
  print("Attention ! L'heure de fin est identique à l'heure de début")
  print("Les heures doivent être comprises entre 0 et 24")
  print("Attention ! Le début de la location est après la fin...")
  debut=int(input("Heure de début (un entier) :"))
  fin=int(input("Heure de fin (un entier) :"))
  

        
for i in range(debut, fin) :
    if i < 7 or i >= 17 :
        tarif1 += 1
    elif 7<= i < 17 :
        tarif2 += 2



prix = tarif1 + tarif2
          
print("Vous avez loué votre vélo pendant")
if tarif1!=0 :
    print(tarif1, "heure(s) au tarif horaire de 1.0 euro")
if tarif2!=0 :
    print(tarif2//2, "heure(s) au tarif horaire de 2.0 euros")
print("Le montant total à payer est de", prix, "euro(s)")
          
