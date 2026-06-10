notas = {
    "Pedro" : 5.5,
    "Maria" : 6.2,
    "Juan" : 4.8,
    "Ana" : 7.0
}

nombre=input("Ingrese nombre: ") .title()

if nombre in notas:
    print("La notas es:", notas[nombre])
else:
    print("El nombre no existe")
