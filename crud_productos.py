from validaciones.validaciones_productos import *
#MENU PRODUCTOS

def mostrar_menu_productos():
    print("=== C.R.U.D de PRODUCTOS ===")
    print("1. Agregar/Crea un producto")  
    print("2. Mostrar/Leer productos")    
    print("3. Actualizar stock de un producto") 
    print("4. Eliminar un producto")   
    print("5. Guardar productos en archivo")
    print("6. Salir")

def guardar_productos_en_archivo(productos):
    """
    Guarda los productos de la matriz en un archivo de texto.
    Cada producto se guarda en una línea con el formato:
    id_producto;nombre_producto;precio_producto;stock_producto
    """
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f"{producto[0]};{producto[1]};{producto[2]};{producto[3]}\n")
    print("Productos guardados en archivo.")


def agregar_producto(productos, conjunto_ids_productos):
    '''
    pre: recibe una matriz ya creada
    pos: agrega el producto a la matriz

    '''
    try:
        id_producto = int(input("Ingrese el ID del producto a agregar: "))
        while (id_producto in conjunto_ids_productos) or (not validar_id_producto(id_producto)):
            if (id_producto in conjunto_ids_productos):
                id_producto = input("El ID ingresado ya exsiste. Ingrese un id nuevamente (4 digitos): ")
            else:
                id_producto = input("El ID ingresado no cumple con lo solicitado. Ingrese un id nuevamente (4 digitos): ")
                
        producto = input("Ingrese el nombre del producto: ")
        while (not validar_producto(producto)):
            producto = input("El producto ingresado no es valido. Ingrese el producto nuevamente: ")

        while True:
            try:
                precio_producto = int(input("Ingrese el precio del prodcuto: "))
                if (not validar_precio_producto (precio_producto)):
                    raise ValueError("El precio no es valido.")
                break 
            except ValueError as error_validacion:
                print(error_validacion)

        while True:
            try:     
                stock_producto = int(input("Ingrese el stock del producto ingresado: "))
                if (not validar_stock_producto(stock_producto)):
                    raise ValueError("La cantidad ingresada no es valida")
                break
            except ValueError as error_validacion:
                print(error_validacion)

        conjunto_ids_productos.add(id_producto)

        producto_nuevo = [id_producto, producto, int(precio_producto), int(stock_producto)]

        productos.append(producto_nuevo)

        print(f'El producto {producto}, fue agregado')

        return productos, conjunto_ids_productos
    
    except ValueError:
        print("Error: Tiene que ingresar un numero entero.")
    except Exception as error_inesperado:
        print(f'Error inesperado: {error_inesperado}.')

def leer_productos(productos):
    '''
    pre: recibe una matriz ya creada
    pos: muestra los productos de la matriz

    '''
    print(f"{'ID':^10} {'PRODUCTO':^25} {'PRECIO':^10} {'STOCK':^10}")
    print("-" * 100)
    for producto in productos:
        print(f"{producto[0]:^10} {producto[1]:^25} {producto[2]:^10} {producto[3]:^10} ")


def actualizar_ejemplares(productos, conjunto_ids_productos):
    '''
    pre: recibe una matriz ya creada
    pos: actualiza la cantidad de stock de un prodcuto en la matriz

    '''
    try:
        id_producto = int(input("Ingrese el ID del producto a actualizar el stock: "))
        if (not(id_producto in conjunto_ids_productos)) or (not validar_id_producto(id_producto)):
            raise ValueError("El ID ingresado no existe o no es valido.")
        
        for producto in productos:
            if producto[0] == id_producto:
                print(f"El producto {producto[1]} tiene {producto[3]} cantidades en stock")
                while True:
                        try:
                            stock_producto = int(input("Ingrese la cantidad de stock actualizados: "))
                            if (not validar_stock_producto(stock_producto)):
                                raise ValueError("La cantidad de stock ingresado no es valido.")
                            
                            producto[3] = int(stock_producto)
                            print(f'El stock del producto {producto[1]}, fue actualizado')
                            break

                        except ValueError as error_stock:
                            print(error_stock)
                break
        else:
            raise LookupError("El producto con el ID ingresado no fue encontrado")
    except ValueError as error_id:
        print(f'Error de ID: {error_id}. Tenes que asegurarte de ingresar un ID valido y existente.')    
    except LookupError as error_de_busqueda:
        print(f'Error de busqueda: {error_de_busqueda}. Tenes que revisar que el ID ingresado se encuentre registrado en el sistema.')
    except Exception as error_inesperado:
        print(f'Error inesperado: {error_inesperado}.')
        
    return productos

def eliminar_producto(productos, conjunto_ids_productos):
    '''
    pre: recibe una matriz ya creada
    pos: elimina un prodcuto de la matriz

    '''
    try: 
        id_producto = int(input("Ingrese el ID del prodcuto a eliminar: "))
        if (not validar_id_producto(id_producto)):
            raise ValueError("El ID ingresado no existe o no es valido. Porfavor ingrese el id nuevamente: ")
        
        id_encontrado = False

        for producto in productos:
            if producto[0] == id_producto:
                productos.remove(producto)
                print("El producto fue eliminado")

                conjunto_ids_productos.discard(id_producto)
                id_encontrado = True
                break

        if (not id_encontrado):
            raise LookupError("El ID ingresado no esta registrado en el sistema")
        
    except ValueError as error_id:
        print(f'Error de ID: {error_id}. Tiene que ingresar un ID valido')
    except LookupError as error_de_busqueda:
        print(f'Error de busqueda: {error_de_busqueda}.Tenes que revisar que el ID ingresado se encuentre registrado en el sistema.')
    except Exception as error_inesperado:
        print(f'Error inesperado: {error_inesperado}.')

    return productos, conjunto_ids_productos