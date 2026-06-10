menu="""
1.Agregar estudiantes
2.Buscar estudiantes
3.Eliminar estudiantes
4.Mostrar estudiantes
5.Salir"""

estudiantes = []
while True:
    print(menu)
    opc=input("Ingresar opción: ")
    if opc=="1":
        while True:
            estudiante=input("Ingresar nombre de estudiante:").lower().strip()
            if len(estudiante)>=(3):
                estudiantes.append(estudiante)
                break
            else:
                print("Error! Debe ingresar un nombre mayor a 3 caracteres ")
    elif opc=="2":
        while True:
            estudiante=input("Ingrese el nombre de estudiante que busca: ").lower().strip()
            if estudiante in estudiantes:
                print("Estudiante ingresado")
                break
            else:
                print("Estudiante no ingresado")
                break
            
    elif opc=="3":
        while True:
            estudiante=input("Ingresar nombre de estudiante para eliminar:").lower().strip()
            if estudiantes in estudiantes:
                estudiantes.remove(estudiante)
                print("Estudiante Eliminado")
                break
            else:
                print("No se encontró estudiante")
    elif opc=="4":
        for estudiante in estudiantes:
            print("Lista de nombre de estudiantes: ",estudiante)
            
    elif opc=="5":
        print("Adios, gracias por utilizar el programa!")
    else:
        print("Error! Ingresar opción (1-5)")
