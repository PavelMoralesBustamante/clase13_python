from random import randint
#1.- Crear una colección con 100 numeros del 0 al 10
numeros = []
for i in range(100):
    numeros.append(randint(0,10))
print(numeros)

#2.- Mostrar solo los índices pares
for i in range(len(numeros)):
    if i%2==0: #Solo se muestren índices pares
        print(f"[{i}] : {numeros[i]}")

#3.- Mostrar el número mayor 
print("El número mayor es ",max(numeros))

#4.- donde están los números mayores
print("Índices donde se encuentra el númro mayor")
for i in range(len(numeros)):
    if numeros[i]==max(numeros):
        print(i, end=" ⭐ ")
print(" ")

#5.- Mostrar el número menor 
print("El número menor es ",min(numeros))

#6.- donde están los números menores
print("Índices donde se encuentra el número menor")
for i in range(len(numeros)):
    if numeros[i]==min(numeros):
        print(i, end=" 💧 ")
print(" ")