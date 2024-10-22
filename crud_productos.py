from validaciones.validaciones_productos import *
#MENU PRODUCTOS

def mostrar_menu_productos():
    print("=== C.R.U.D de PRODUCTOS ===")
    print("1. Agregar/Crea un producto")  
    print("2. Mostrar/Leer productos")    
    print("3. Actualizar la cantidad de ejemplares de un producto") 
    print("4. Eliminar un producto")   
    print("5. Salir")


def agregar_producto(libros, conjunto_ids_libros):
    '''
    pre: recibe una matriz ya creada
    pos: agrega el producto a la matriz

    '''
    #ID
    id_libro = int(input("Ingrese el ID del producto a agregar: "))
    while (id_libro in conjunto_ids_libros) or (not validar_id_libro(id_libro)):
        if (id_libro in conjunto_ids_libros):
            id_libro = input("El ID ingresado ya exsiste. Ingrese un id nuevamente (4 digitos): ")
        else:
            id_libro = input("El ID ingresado no cumple con lo solicitado. Ingrese un id nuevamente (4 digitos): ")
    
    #TITULO
    titulo_libro = input("Ingrese el titulo del libro: ")
    while (not validar_titulo_libro (titulo_libro)):
        titulo_libro = input("El titulo ingresado no es valido. Ingrese el titulo nuevamente: ")
    
    #AUTOR
    autor_libro = input("Ingrese un nombre (Nombre y Apellido): ")
    while (not validar_autor_libro (autor_libro)):
        autor_libro = input("El nombre no cumple con el formato solicitado. Ingrese un nombre (en formato Nombre y Apellido): ")

    #PRECIO
    precio_libro = int(input("Ingrese el precio del libro: "))
    while (not validar_precio_libro (precio_libro)):
           precio_libro = int(input("El precio no es valido. Ingrese el precio nuevamente: "))
    
    #EJEMPLARES
    ejemplares_libro = int(input("Ingrese la cantidad de ejemplares del libro ingresado: "))
    while (not validar_ejemplares_libro(ejemplares_libro)):
        ejemplares_libro = int(input("La cantidad no es valida. Porfavor, ingrese nuevamente la cantidad: "))

    conjunto_ids_libros.add(id_libro)

    libro_nuevo = [id_libro, titulo_libro, autor_libro, int(precio_libro), int(ejemplares_libro)]

    libros.append(libro_nuevo)

    print(f'El libro {titulo_libro}, fue agregado')

    return libros, conjunto_ids_libros

def leer_productos(libros):
    '''
    pre: recibe una matriz ya creada
    pos: muestra los productos de la matriz

    '''
    print(f"{'ID':^10} {'TITULO':^25} {'AUTOR':^25} {'PRECIO':^10} {'CANTIDAD DE EJEMPLARES':^10}")
    print("-" * 100)
    for libro in libros:
        print(f"{libro[0]:^10} {libro[1]:^25} {libro[2]:^25} {libro[3]:^10} {libro[4]:^20}")


def actualizar_ejemplares(libros, conjunto_ids_libros):
    '''
    pre: recibe una matriz ya creada
    pos: actualiza la cantidad de ejemplares de un prodcuto en la matriz

    '''
    id_libro = int(input("Ingrese el ID del producto a actualizar los ejemplares: "))
    for libro in libros:
        while (not(id_libro in conjunto_ids_libros)) or (not validar_id_libro(id_libro)):
            id_libro = int(input("El ID ingresado no existe o no es valido. Porfavor ingrese el id nuevamente: "))
    
    for libro in libros:
        if libro[0] == id_libro:
            print(f"El libro {libro[1]} tiene {libro[4]} ejemplares")

            ejemplares_libro = int(input("Ingrese la cantidad de ejemplares actualizados: "))

            while (not validar_ejemplares_libro(ejemplares_libro)):
                ejemplares_libro = int(input("La cantidad de ejemplares ingresado no es valido. Intente neuvamente: "))
        
            libro[4] = int(ejemplares_libro)
            print(f'Los ejemplares del libro {libro[1]}, fueron actualizados')
            break

    return libros


def eliminar_producto(libros, conjunto_ids_libros):
    '''
    pre: recibe una matriz ya creada
    pos: elimina un prodcuto de la matriz

    '''
    id_libro = int(input("Ingrese el ID del prodcuto a eliminar: "))
    while (not validar_id_libro(id_libro)):
        id_libro = int(input("El ID ingresado no existe o no es valido. Porfavor ingrese el id nuevamente: "))
    
    id_encontrado = False

    for libro in libros:
        if libro[0] == id_libro:
            libros.remove(libro)
            print("El producto fue eliminado")
            conjunto_ids_libros.discard(id_libro)
            id_encontrado = True
            break
    if (not id_encontrado):
        print("El ID ingresado no existe")
    
    return libros, conjunto_ids_libros