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

def agregar_producto(productos, conjunto_ids_productos):
    '''
    pre: recibe una matriz ya creada
    pos: agrega el producto a la matriz

    '''
    try:
        id_producto = int(input("Ingrese el ID del producto a agregar: "))
        while (id_producto in conjunto_ids_productos) or (not validar_id_producto(id_producto)):
            if id_producto in conjunto_ids_productos:
                print("El ID ingresado ya existe.")
            else:
                print("El ID ingresado no cumple con lo solicitado.")
            # Asegúrate de convertir a entero después de recibir el input nuevamente
            try:
                id_producto = int(input("Ingrese un ID válido (4 dígitos): "))
            except ValueError:
                print("Debe ingresar un número entero.")
                continue
            
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

def leer_productos_archivos(archivo, modo):
    '''
    pre: recibe archivo de texto ya creado
    pos: muestra los productos cargados en el archivo

    '''
    try:
        arch = open(archivo, modo, encoding="UTF-8")
    except OSError:
        print("No es posbile leer el archivo")
    else:
        registro = arch.readline().strip()
        print(f"{'ID':9} {'PRODUCTO':25} {'PRECIO':13} {'STOCK':4}")
        print("-" * 100)
        while registro:
            id, producto, precio, stock = registro.split(";")
            print(f'{id:10}{producto:25}${precio:15}{stock:4}')
            registro = arch.readline().strip()
    finally:
        arch.close()

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

def guardar_productos_archivo(archivo, modo, productos):
    '''
    pre: recibe el archivo de texto junto con la matriz para hacer el guardado.
    pos: guarda los productos de la matriz en un archivo de texto:
  
    '''
    try:
        arch = open(archivo, modo, encoding="UTF-8")
        registro = [f'{fila[0]};{fila[1]};{fila[2]};{fila[3]}\n' for fila in productos]
        arch.writelines(registro)
        print("Datos cargados exitosamente")
    except ValueError:
        print("No se pudo convertir el tipo de dato de forma correcta")
    except OSError:
        print("No se pudo crear el archivo")
    finally:
        arch.close()