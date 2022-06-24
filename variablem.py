m =[]
n = int(input("ingrese el total de filas y columna de la matriz :"))
for i in range(n):
    m.append([])
    for j in range(n):
        m[i].append(int(input("ingresar el valor de la fila" + str(i + 1) + "columna" + str(j + 1)+ ":")))
print("los valores de la diagonal principal son:")
for i in range(n):
  print(m[i][i])