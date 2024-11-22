v1=0
v2=0
v3=0
for i in range (10) :
    n = int(input("Entrer un nombre :"))
    if n>20 :
        n = int(input("Entrer un nombre :"))
    if n<10 :
        v1=v1+1
    elif n>=10 and n<15 :
        v2=v2+1
    else :
        v3=v3+1

print(v1, "nombre(s) sont strictement inférieurs à 10.")
print(v2, "nombre(s) sont supérieur ou égal à 10 et strictement inférieur à 15.")
print(v3, "nombre(s) sont supérieur ou égal à 15.")