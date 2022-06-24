#Ejercicio 1
# Realizar un programa que inicialice una lista con 10 valores aleatorio
#  (del 1 al 10) yposteriormente muestre en pantalla cada elemento de la lista junto
#  con sucuadrado y su cubo.
import random
lista_numeros =[]
for indice in range(1,11):
    lista_numeros.append(random.randint(1,10))
for numero in lista_numeros:
    print(numero," ",numero ** 2,"",numero ** 3)



