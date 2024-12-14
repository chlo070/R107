#les dictionnaires
"""
#exemple :
dico = {}
dico['computer'] = 'ordinateur'
dico['mouse'] ='souris'
dico['keyboard'] ='clavier'
print(dico)
{'computer': 'ordinateur', 'keyboard': 'clavier', 'mouse': 'souris'}
"""

dico = {}
dico['firstname'] = 'Chloé'
dico['name'] = 'Sondag'
dico['promo'] = 'RT1 2024'
dico['group'] = 'RT132'
#print(dico)
print(f"Votre nom est {dico['name']}, prénom est {dico['firstname']}, vous faites partie de la promo {dico['promo']} et votre groupe est {dico['group']}")

#Affichage avec les méthodes keys(), values() et items()
print(f"Les clés du dictionnaire sont :,")
for i in dico.keys() :
    print(f"-{i}")
print(f"Les valeurs du dictionnaire sont :,")
for i in dico.values() :
    print (f"-{i}")
print(f"Les tuplets du dictionnaire sont :,")
for i in dico.items() :
    print(f"-{i}")

"""
dicobin = {}
dicobin['firstname'] = 'Lea'
dicobin['name'] = 'Schmidt'
dicobin['promo'] = 'RT1 2024'
dicobin['group'] = 'RT132'
print(dicobin)



#Affichage avec les méthodes keys(), values() et items()

Un exemple d’affichage à produire pour le dictionnaire : dic={"name":"toto","firstname":"titi","promo":2022,"group":202} :
 
Les clés du dictionnaire sont :
-name
-firstname
-promo
-group
Les valeurs du dictionnaire sont :
-toto
-titi
-2022
-202
Les tuplets du dictionnaire sont :
-('name', toto)
-('firstname', titi)
-('promo', 2022)
-('group', 202)
"""