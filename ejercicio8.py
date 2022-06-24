#ejercicio8
# Queremos guardar los nombres y la edades de los alumnos de un curso. Realizaun programa que introduzca el nombre y la edad de cada alumno. El proceso delectura de datos terminará cuando se introduzca como nombre un asterisco (*) Alfinalizar se mostrará los siguientes datos:
# •Todos lo alumnos mayores de edad.
# •Los alumnos mayores (los que tienen más edad)


nombres = []
edades = []

while True:
    nombre = input("Dime el nombre de un alumno:")
    if nombre != "*":
        nombres.append(nombre)
        edades.append(int(input("Dime su edad:")))
    if nombre == "*": break;


edad_max = max(edades)

print("Alumnos mayores de edad")
print("=======================")
for nombre ,edad in zip(nombres ,edades):
    if edad >= 18:
        print(nombre)



print("Alumnos mayores")
print("===============")
for nombre ,edad in zip(nombres ,edades):
    if edad == edad_max:
        print(nombre)
