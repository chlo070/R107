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
print(f"Votre nom est {'name'}, prénom est {'firstname'}, vous faites partie de la promo {'promo'} et votre groupe est {'group'}")

#Affichage avec les méthodes keys(), values() et items()
"""
. Un exemple d’affichage à produire pour le dictionnaire 
dic={"name":"toto","firstname":"titi","promo":2022,"group":202} :
 
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