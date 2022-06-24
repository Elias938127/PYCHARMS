imp= []
total = []
for i in range(10):
    imp.append([])
    for j in range(3):
        imp[i].append(int(input("ingresar el importe del producto" + str(i+1)+ ",cliente"+ str(j+1)+":")))
for i in range(3):
     suma =0
     for j in range(10):
         suma =suma +imp[j][i]
     total.append(suma)
print("el importe de todos los productos por cliente son :")
print(total)