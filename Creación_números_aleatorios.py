import random #libreria para llamar y crear numeros random

numeros = [] #Colección vacía

for i in range(10): #Ciclo para repetir 100 veces las iteraciones
    n = random.randint(1,100) #Crea el numero entre 1 y 100
    numeros.append(n) #Guardamos en la lista el numero aleatorio

print(numeros) #Visualizamos lista

#Contador de números pares
cont = 0
for i in range(len(numeros)):
    if numeros[i]%2==0:
        cont+=1
print(f"Cantidad de números pares : {cont}")