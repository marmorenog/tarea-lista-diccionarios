notas = {
    "Pedro" : 5.5,
    "Maria" : 6.2,
    "Juan" : 4.8,
    "Ana" : 7.0
}
while True:
    for x in notas:
        print("Nombres:",x)

    nombre=input("Ingrese nombre: ") .title()
    
    if nombre in notas:
        print("La notas es:", notas[nombre])
        break
    else:
         print("El nombre no existe")


