#Ejercicio 4
# Programa que declare una lista y la vaya llenando de números hasta queintroduzcamos un número negativo. Entonces se debe
# imprimir el vector (sólo loselementos introducidos).


lista = []
numero = int(input("Introduce un número en la lista:"))
while numero>=0:
	lista.append(numero)
	numero = int(input("Introduce un número en la lista:"))

for numero in lista:
	print(numero," ",end="")
