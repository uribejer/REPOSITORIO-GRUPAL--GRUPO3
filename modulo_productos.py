#modulo_productos.py
#FUNCIONES DEL MODULO PRODUCTOS

def desordenada_libros(libros):
    # IMPRESION ENCABEZADO CON FORMATO f-strings (PRODUCTOS)
    print()
    print(f"{'ID':^10} {'TITULO':^30} {'AUTOR':^30} {'EDITORIAL':^30} {'PRECIO':^10}")
    print('-' * 120)

    for libro in libros:
        print(f"{libro[0]:^10} {libro[1]:^30}  {libro[2]:^30} {libro[3]:^30} {libro[4]:^10}")
    return libros

def agregar_libros (libros, cant_libros_agregar):
    i = 1
    for i in range (cant_libros_agregar):
        libro = []
        ID = int(input("Ingrese el ID: "))
        libro.append(ID)
        titulo = (input("Ingrese el nombre libro: "))
        libro.append(titulo)
        autor = (input("Ingrese el autor del libro: "))
        libro.append(autor)
        editorial = (input("Ingrese la editorial del libro: "))
        libro.append(editorial)
        precio = int(input("Ingrese el precio del libro: "))
        libro.append(precio)

        libros.append(libro)
    return libros
        
def modificar_autor (tabla_libros_actualizada):
    for libro in tabla_libros_actualizada:
        for dato in libro:
            if dato == libro[1]:
                nombre_completo = libro[2]   
                nombre_completo.strip() #ELIMINA LOS ESCPACIOS SORANTES AL PRINCIPIO Y AL FINAL
                nombre, apellido = nombre_completo.split(' ', 1) #DIVIDE EL NOMBRE Y APELLIDO POR EL PRIMER ESPACIO
                nombre_modificado = (f"{nombre[0].upper()}.{apellido.upper()}")
                libro[2] = nombre_modificado
    return tabla_libros_actualizada


def eliminar_libro(tabla_libros_actualizada):
    print()
    print(f"{'ID':^10} {'TITULO':^30} {'AUTOR':^30} {'EDITORIAL':^30} {'PRECIO':^10}")
    print('-' * 120)
    for libro in tabla_libros_actualizada:
        print(f"{libro[0]:^10} {libro[1]:^30}  {libro[2]:^30} {libro[3]:^30} {libro[4]:^10}")
    cuantos_libro_eliminar = int(input("Cuantos libros quiere eliminar? "))
    while cuantos_libro_eliminar > 0:
        libro_a_eliminar = int(input("Que libro quiere eliminar (ingrese su ID)? "))
        for libro in tabla_libros_actualizada:
            if libro[0] == libro_a_eliminar:
                tabla_libros_actualizada.remove(libro)
                cuantos_libro_eliminar -= 1
                print(f"El libro {libro[1]} fue eliminado")
    return  tabla_libros_actualizada
         

def ordenada_libros(tabla_ordenada_libros):
    # IMPRESION ENCABEZADO CON FORMATO f-strings (PRODUCTOS)
    print()
    print(f"{'ID':^10} {'TITULO':^30} {'AUTOR':^30} {'EDITORIAL':^30} {'PRECIO':^10}")
    print('-' * 120)

    for libro in tabla_ordenada_libros:
        print(f"{libro[0]:^10} {libro[1]:^30}  {libro[2]:^30} {libro[3]:^30} {libro[4]:^10}")

    return tabla_ordenada_libros