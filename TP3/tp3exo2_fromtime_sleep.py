import time
n=int(input("Entrer un nombre positif :"))
while n<0 :
    n = int(input("Entrer un nombre positif :"))
for i in range(n,-1,-1) :
        print(i)
        time.sleep(1)


m=int(input("Entrer un nombre positif :"))
i=0
while m<0 :
    m = int(input("Entrer un nombre positif :"))
while i<=m :
        print(m-i)
        i=i+1
        time.sleep(1)