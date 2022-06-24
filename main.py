nombres = ["ana", "sonia",  "helena"]
nombres2 = ["miguel", "carlos", "juan"]
nombresfinales = [nombres, nombres2]
print("imprimiendo valor [0][1]", nombresfinales[0][1])
print("lista completa :", nombresfinales)

for i in range(len(nombresfinales)):
    print("\n")
    if i ==0:
        print("######## nombres femeninos ######")
    elif i == 1 :
        print("###### nombres masculinos ####")
    for j in range(len(nombresfinales[i])):
        print(nombresfinales [i][j] , end=" ,")