from crud_productos import *
from crud_usuarios import *
from validaciones.validaciones_usuarios import validar_id_usuarios
from validaciones.validaciones_registros_compra import validar_id_registro_de_compra,validacion_fecha_compra
from functools import reduce

def mostrar_menu_registros_compra():
    print("=== C.R.U.D de REGISTROS DE COMPRA ===")
    print("1. Agregar/Crea un registro de compra")  
    print("2. Mostrar/Leer registros de compra")    
    print("3. Eliminar un registro de compra")   
    print("4. Salir")


def agregar_registros(productos, registros, conjunto_ids_registros, conjunto_ids_usuarios):
    '''
    pre: recibe un diccionario ya creado
    pos: agrega el registro de compra al diccionario 
    
    '''
    try:
        id_registro_de_compra = input("Ingrese el ID del registro de compras: ")
        while (id_registro_de_compra in conjunto_ids_registros) or (not (validar_id_registro_de_compra(id_registro_de_compra))):
            if id_registro_de_compra in conjunto_ids_registros:
                id_registro_de_compra = input("El ID ingresado ya exsiste. Ingrese un id nuevamente (4 digitos): ")
            else:
                id_registro_de_compra = input("El ID ingresado no cumple con lo solicitado. Ingrese un id nuevamente (4 digitos): ")

        
        id_usuario = input("Ingrese el ID del usuario (4 digitos): ")
        while (id_usuario not in conjunto_ids_usuarios) or (not validar_id_usuarios(id_usuario)):
            if id_usuario not in conjunto_ids_usuarios:
                print("El ID ingresado no exsiste.")
                return registros, conjunto_ids_registros
            else:
                print("El ID ingresado no cumple con lo solicitado.")
                return registros, conjunto_ids_registros

        cant_productos_a_llevar = int(input("Cuantos productos va a llevar: "))
        if cant_productos_a_llevar <= 0:
            raise ValueError("La cantidad de productos a llevar tiene que ser un numero positivo")

        carrito = []
        precios = []

        while cant_productos_a_llevar > 0:
            try: 
                id_producto = (int(input("Ingrese el ID del producto que va a llevar: ")))

                encontrado = False

                for producto in productos:
                    if (id_producto == producto[0]):
                        encontrado = True
                        carrito.append(producto[1])
                        precios.append(producto[2])
                        if producto[3] <= 0:
                            raise ValueError("No hay stock suficiente del producto.")

                        producto[3] -= 1
                        break

                if (not(encontrado)):
                    raise LookupError("El producto no fue encontrado") 
                else:
                    cant_productos_a_llevar -= 1

            except ValueError as error_producto:
                print(f"Error con el producto {error_producto}.")
            except LookupError as error_de_busqueda:
                print(f"Error de busqueda {error_de_busqueda}.")

        fecha_compra = input("Ingrese la fecha de compra (formato dd-mm-aaaa): ")
        if (not(validacion_fecha_compra(fecha_compra))):
            raise ValueError("La fecha ingresada no es valida. (formato dd-mm-aaaa): ")
        
        precio_total = reduce(lambda x,y: x + y, precios)

        conjunto_ids_registros.add(id_registro_de_compra)

        registro_de_compra_nuevo = [id_registro_de_compra, id_usuario, carrito, precio_total, fecha_compra]

        registros.append(registro_de_compra_nuevo)

        print(f'El registro con ID {id_registro_de_compra}, fue agregado con exito')

        return registros, conjunto_ids_registros

        
    except ValueError as error_id:
        print(f"Error en el ingreso de datos {error_id}.")
    except Exception as error_inesperado:
        print(f"Error inesperado {error_inesperado}")

    return registros, conjunto_ids_registros

def leer_registros(registros):
    '''
    pre: recibe un diccionario ya creado
    pos: muestra los registros del diccionario

    '''
    print(f"{'ID (registro de compra)':^20} {'ID (cliente)':^20} {'PRODUCTOS A LLEVAR':^20} {'TOTAL A PAGAR':^20} {'FECHA COMPRA':^20}")
    print("-" * 100)
    for registro in registros:
        print(f"{registro[0]:^10} {registro[1]:^20} {str(registro[2]):^10} {registro[3]:^20} {registro[4]:^20}")


def eliminar_registro(registros, conjunto_ids_registros):
    '''
    pre: recibe un diccionario ya creado y solicita el ID
    pos: elimina el registro seleccionado y actualiza el diccionario
    '''
    try: 
        id_registro_de_compra = int(input("Ingrese el ID del prodcuto a eliminar: "))
        if (not validar_id_registro_de_compra(id_registro_de_compra)):
            raise ValueError("El ID ingresado no existe o no es valido. Porfavor ingrese el id nuevamente: ")
        
        id_encontrado = False

        for registro in registros:
            if registro[0] == id_registro_de_compra:
                registros.remove(registro)
                print("El registro de compra fue eliminado")

                conjunto_ids_registros.discard(id_registro_de_compra)
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

    return registros, conjunto_ids_registros