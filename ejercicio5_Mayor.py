
numeros = []

for x in range (8):
    try:
        numero=int(input("Ingrese números: "))
        numeros.append(numero)
    except:
        print("Error! Ingresar número entero")

numeros.sort()

print("Número Mayor: ",numeros[7])
print("Número Menor: ", numeros[0])
print("Cantidad de elementos: ",len(numeros))

#no se si esta bien pero es lo único que se me ocurrio 