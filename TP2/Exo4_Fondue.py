BASE=4
fromage=800
eau=2
ail=2
pain=400
nbConvives=int (input("Pour combien de convive veut-on préparer la recette ? "))
varFr = fromage * (nbConvives / BASE)
varEau = eau * (nbConvives / BASE)
varAil = ail * (nbConvives / BASE)
varP = pain * (nbConvives / BASE)
print("Pour faire une fondue fribourgeoise pour ", nbConvives, " personnes, il vous faut :")
print("- ", varFr, " gr de fromage")
print("- ", varEau, " dl d'eau")
print("- ", varAil, " gousse(s) d'ail")
print("- ", varP, "gr de pain")
