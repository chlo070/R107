from random import randint
nombre = randint (0, 100)
i=0
n=int(input("Devinez le nombre tiré au hasard :"))
while n!=nombre :
    if n<nombre :
        print("La valeur est plus grande.")
        n=int(input("Recommencez :"))
        i=i+1
    elif n>nombre :
        print("La valeur est plus petite.")
        n = int(input("Recommencez : "))
        i=i+1
print("Le nombre était bien", n,". Il vous a fallu", i, "tentatives.")

