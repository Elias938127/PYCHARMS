#Ejercicio 5
# Hacer un programa que inicialice una lista de números con valores aleatorios (10valores), y #
#posterior ordene los elementos de menor a mayor.

import random
lista = []
for indice in range(1,11):
	lista.append(random.randint(1,10))

lista.sort()


for numero in lista:
	print(numero," ",end="")
