notas = [ ]

acum=0
for x in range (5):
        nota=int(input("Ingrese notas:"))
        if nota>=1 and nota<=7:
            notas.append(nota)
            acum+=nota
        else:
            print("Error!, El número debe ser mayor a 0")
promedio=acum/len (notas)
    
print("Suma:",acum)
print("Promedio:",promedio)