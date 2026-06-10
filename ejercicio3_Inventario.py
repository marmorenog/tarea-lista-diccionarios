inventario = {
    "Laptop" : 10,
    "Mouse" : 25,
    "Teclado" : 15
}

while True:
    for x in inventario:
        print("Producto: ", x,"Cantidad: ", inventario[x])
    producto=input("Ingrese un producto: ").title().strip()
    if producto in inventario:
        try:
            cantidad=int(input("Ingrese cantidad: "))
        except:
            print("Error! Debe ingresar un número entero")
            if cantidad<=inventario[producto]:
                inventario[producto]-=cantidad
                print("Venta realizada ")
                print(producto ,":",inventario[producto], "unidades")
                break
            else:
                print("No hay suficiente stock")
    else: 
        print("Articulo no disponible, debe ingresar nombre valido")

                    