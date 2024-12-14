#les dictionnaires

dico = {}
dico['firstname'] = 'Chloé'
dico['name'] = 'Sondag'
dico['promo'] = 'RT1 2024'
dico['group'] = 'RT132'
#print(dico)
print()
#5.
print(f"Votre nom est {dico['name']}, votre prénom est {dico['firstname']}, vous faites partie de la promo {dico['promo']} et votre groupe est {dico['group']}")
print()
#6.Affichage avec les méthodes keys(), values() et items()
print(f"Les clés du dictionnaire sont :,")
for i in dico.keys() :
    print(f"-{i}")
print(f"Les valeurs du dictionnaire sont :,")
for i in dico.values() :
    print (f"-{i}")
print(f"Les tuplets du dictionnaire sont :,")
for i in dico.items() :
    print(f"-{i}")
print()

#7.Ajout d'un binome
dicobin = {}
dicobin['firstname'] = 'Lea'
dicobin['name'] = 'Schmidt'
dicobin['promo'] = 'RT1 2024'
dicobin['group'] = 'RT132'
print(dicobin)
print()
#8.
binome = {}
binome['étudiant 1'] = dico
binome['étudiant 2'] = dicobin
print(binome)
print()

#9 Affichage ligne par ligne des membres du binome
print(f"Les étudiants formants le binôme sont :")
print(f"- L'étudiant {dico['firstname']} {dico['name']} du groupe {dico['group']}")
print(f"- L'étudiant {dicobin['firstname']} {dicobin['name']} du groupe {dicobin['group']}")

