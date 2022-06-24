paises =[]
for x in range(5):
    nom = input("ingrese el nombre de pais:")
    paises.append(nom)
for k in range (4):
    for x in range(4):
        if paises [x]> paises [x+1]:
            aux = paises[x]
            paises[x]= paises[x+1]
            paises[x+1]=aux
print("listado de paises")
print(paises)