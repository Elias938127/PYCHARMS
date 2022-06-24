#Ejercicio 2
# Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copialos elementos de la lista en otra lista pero en orden inverso,
#y muestra suselementos por la pantalla.

lista1=[]
lista2=[]
for indice in range(1,6):
    lista1.append(input("dame la cadena %d:" % indice))
lista2= lista1[::-1]

for cadena in lista2:
    print(cadena)