 # Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
# déclaration d’une liste vide qui va contenir autant de notes que d'étudiants
notes = []
i=0
somme=0

for i in range (1, nombreEtudiants+1):
    note = float(input(f"Donnez la note de l'etudiant {round(i,1)}: "))
    notes.append(note)
    somme += note

moyenne=somme/nombreEtudiants

print(f"Moyenne de classe : {moyenne}")


print("Numéro de l'Etudiants | note | ecart a la moyenne")
for i in range(nombreEtudiants):
    ecart=notes[i]-moyenne
    print(f"{i} | {notes[i]} | {round(ecart,1)}")







#exemple:
#Donnez le nombre d'etudiants : 4
#Note etudiant 0 : 4.0
#Note etudiant 1 : 4.0
#Note etudiant 2 : 5.0
#Note etudiant 3 : 6.0
#Moyenne de classe : 4.75
#Numéro de l’Etudiant | note | ecart a la moyenne
#0 | 4.0 | -0.75
#1 | 4.0 | -0.75
#2 | 5.0 | 0.25
#3 | 6.0 | 1.25



