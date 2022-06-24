#Ejercicio 3
# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por unalumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas,la nota media, la nota
# más alta que ha sacado y la menor.

notas = []
for indice in range(1,6):
        while True:
            nota = int(input("introduce la nota %d:" % indice))
            if nota>=0 and nota<=10: break
        notas.append(nota)



print("notas:",end="")
for nota in notas:
    print(nota," ",end="")
print()
print("nota media:", sum(notas)/len(notas))
print("nota max: ", max(notas))
print("nota min:", min(notas))