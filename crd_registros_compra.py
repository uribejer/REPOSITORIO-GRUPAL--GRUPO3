from crud_productos import *
from crud_usuarios import *
from validaciones.validaciones_usuarios import validar_id_usuarios
from validaciones.validaciones_productos import validar_id_libro
from validaciones.validaciones_registros_compra import validacion_fecha_compra
from functools import reduce

def mostrar_menu_registros_compra():
    print("=== C.R.U.D de REGISTROS DE COMPRA ===")
    print("1. Agregar/Crea un registro de compra")  
    print("2. Mostrar/Leer registros de compra")    
    print("3. Eliminar un registro de compra")   
    print("4. Salir")


def agregar_registros(libros, registros, conjunto_ids_registros):
    '''
    pre: recibe un diccionario ya creado
    pos: agrega el registro de compra al diccionario 
    
    '''

    #obtengo las CLAVES de mi diccionarios "usuarios"

    #ingresar un id de usuario que este en el diccionario
    id_usuario = input("Ingrese el ID del usuario: ")
    while (not(id_usuario in conjunto_ids_registros)) or (not (validar_id_usuarios(id_usuario))):
        if (not(id_usuario in conjunto_ids_registros)): 
            id_usuario = input("El ID del usuario ingresado no exisite. Ingrese el ID nuevamente porfavor: ")
        else:
            id_usuario = input("El ID del usuario ingreado no es valido. Ingrese el ID nuevamente porfavor: ")


    #cuantos libros va a llevar
    cant_libros_a_llevar = int(input("Cuantos libros va a llevar: "))
    libros_a_llevar = []
    precios = []
    while cant_libros_a_llevar > 0:
        id_libro = (int(input("Ingrese el ID del libro que va a llevar: ")))
        encontrado = False
        for libro in libros:
            if (id_libro == libro[0]):
                encontrado = True
                libros_a_llevar.append(libro[1])
                precios.append(libro[3])
                libro[4] -= 1
                break

        if (not(encontrado)):
            print("Error 1") 
        else:
            cant_libros_a_llevar -= 1

    fecha_compra = input("Ingrese la fecha de compra (formato dd-mm-aaaa): ")
    while (not(validacion_fecha_compra(fecha_compra))):
        fecha_compra = input("La fecha ingresada no es valida> Ingrese la fecha nuevamente (formato dd-mm-aaaa): ")
    
    precio_total = reduce(lambda x,y: x + y, precios)

    conjunto_ids_registros.add(id_usuario)

    registros[id_usuario] = {"libros a llevar" : libros_a_llevar, "precio total" : precio_total, "fecha de compra" : fecha_compra}

    return registros, conjunto_ids_registros

def leer_registros(registros):
    '''
    pre: recibe un diccionario ya creado
    pos: muestra los registros del diccionario

    '''
    print(f"{'ID (usuario)':^10} {'LIBROS A LLEVAR':^20} {'TOTAL A PAGAR':^10} {'FECHA COMPRA':^20}")
    print("-" * 100)
    for clave, valor in registros.items():
        libros = ", ".join(valor['libros a llevar'])
        print(f"{clave:^10} {libros:^20} {valor['precio total']:^10} {valor['fecha de compra']:^20}")


def eliminar_registro(registros, conjunto_ids_registros):
    '''
    pre: recibe un diccionario ya creado y solicita el ID
    pos: elimina el registro seleccionado y actualiza el diccionario
    '''

    id_usuario = (input("Registro a eliminar (ingrese el ID del usuario)"))
    if id_usuario in conjunto_ids_registros:
        del registros[id_usuario]
        print(f"El cliente con el id {id_usuario} fue eliminado")
        conjunto_ids_registros.discard(id_usuario)
    else:
        print("El cliente con el {id_usuario}  no existe")

    return registros, conjunto_ids_registros