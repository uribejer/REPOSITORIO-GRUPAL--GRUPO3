from validaciones.validaciones_usuarios import *
import json
#MENU USUARIOS

def mostrar_menu_usuarios():
    print("=== C.R.U.D de USUARIOS ===")
    print("1. Agregar/Crea un usuario")  
    print("2. Mostrar/Leer usuario")    
    print("3. Actualizar un usuario") 
    print("4. Eliminar un usuario")   
    print("5. Guardar usuarios en archivo")
    print("6. Salir")

def crear_usuario(usuarios, conjunto_ids_usuarios):
    '''
    pre: recibe un diccionario ya creado
    pos: agrega el usuario al diccionario 
    
    '''
    try:
        id_usuario = input("Ingrese un id (4 digitos): ")
        while (id_usuario in conjunto_ids_usuarios) or (not validar_id_usuarios(id_usuario)):
            if id_usuario in conjunto_ids_usuarios:
                id_usuario = input("El ID ingresado ya exsiste. Ingrese un id nuevamente (4 digitos): ")
            else:
                id_usuario = input("El ID ingresado no cumple con lo solicitado. Ingrese un id nuevamente (4 digitos): ")

        nombre_usuario = input("Ingrese un nombre (Nombre y Apellido)")

        while (not validar_nombre_usuarios(nombre_usuario)):
            nombre_usuario = input("El nombre no cumple con el formato solicitado. Ingrese un nombre (en formato Nombre y Apellido)")

        nombre_usuario.strip()
        nombre,apellido = nombre_usuario.split(' ',1)
        nombre_modificado = (f'{nombre[0].upper()}.{apellido.upper()}')
        
        email_usuario = input("Ingrese un email (en formato xxxxxx@xxx.xxxx.xxx)")
        while (not validar_email_usuario(email_usuario)):
            email_usuario = input("El mail ingresado no cumple con el formato. Ingrese un email (en formato xxxxxx@xxx.xxxx.xxx)")

        telefono_usuario = input("Ingrese un telefono (en formato (xx-xxxxxxxx)")
        while (not validar_telefono_usuario(telefono_usuario)):
            telefono_usuario = input("El telefono ingresado no cumple el formato (en formato xx-xxxxxxxx)")

        metodo_pago_usuario = input("Ingrese un metodo de pago (efectivo|tarjeta)")
        while (not validar_metodo_pago_usuario(metodo_pago_usuario)):
            metodo_pago_usuario = input("El metodo de pago es incorrecto. Ingrese un metodo de pago nuevamente (efectivo|tarjeta)")

        usuarios[id_usuario] = {"nombre" : nombre_modificado, "email" : email_usuario, "telefono" : telefono_usuario, "metodo de pago" : metodo_pago_usuario.lower()}

        conjunto_ids_usuarios.add(str(id_usuario))

        print(f'El usuario {nombre_usuario} fue creado')

    except ValueError as valor_error:
        print(f"Error valor ingresado {valor_error}")
    except KeyError as clave_error:
        print(f"Error clave en el diccionario {clave_error}.")
    except IndexError as formato_nombre_error:
        print(f"Error sobre el formato del nombre ingresado {formato_nombre_error}.")
    except Exception as error_inesperado:
        print(f"Error inesperado {error_inesperado}.")

    return usuarios, conjunto_ids_usuarios
                     
def leer_usuarios_archivos(archivo, modo):
    '''
    pre: recibe un diccionario ya creado
    pos: muestra los usuarios del diccionario

    '''
    try:
        with open(archivo, modo, encoding="UTF-8") as archivo_usuarios:
            usuarios = json.load(archivo_usuarios)
        print(f"{'ID':9} {'NOMBRE':25} {'EMAIL':25} {'TELEFONO':20} {'METODO DE PAGO':10}")
        print("-" * 100)
        for clave, valor in usuarios.items():
            try:
                print(f'{clave:9} {valor["nombre"]:25} {valor["email"]:25} {valor["telefono"]:20} {valor["metodo de pago"]:10}')
            except KeyError as e:
                print(f"Error: Falta el campo {e} en el registro del usuario con ID {clave}.")
    except (FileNotFoundError, OSError) as error:
        print(f'Error {error}')

def actualizar_usuarios(usuarios, conjunto_ids_usuarios):
    '''
    pre: recibe un diccionario ya creado
    pos: actualiza los datos de los usuarios del diccionario

    '''
    try:
        id_usuario = (input("Cliente a actualizar (ingrese su ID)"))
        while (not validar_id_usuarios(id_usuario)):
            id_usuario = input("El ID ingresado no cumple con lo solicitado. Ingrese un id nuevamente (4 digitos): ")

        if id_usuario in conjunto_ids_usuarios:
            nombre_usuario = input("Ingrese el nombre actualizado (en formato Nombre y Apellido): ")
            while (not validar_nombre_usuarios(nombre_usuario)):
                nombre_usuario = input("El nombre no cumple con el formato solicitado. Ingrese un nombre (en formato Nombre y Apellido)")

            nombre_usuario.strip()
            nombre,apellido = nombre_usuario.split(' ',1)
            nombre_modificado = (f'{nombre[0].upper()}.{apellido.upper()}')

            email_usuario = input("Ingrese el email actualizado (en formato xxxxxx@xxx.xxxx.xxx)")
            while (not validar_email_usuario(email_usuario)):
                email_usuario = input("El email no cumple con el formato solicitado. Ingrese un email (en formato xxxxxx@xxx.xxxx.xxx)")

            telefono_usuario = input("Ingrese un telefono (en formato (xx-xxxxxxxx)")
            while (not validar_telefono_usuario(telefono_usuario)):
                telefono_usuario = input("El telefono no cumple con el formato solicitado. Ingrese un telefono (en formato xx-xxxxxxxx)")

            metodo_pago_usuario = input("Ingrese un metodo de pago (efectivo|tarjeta)")
            while (not validar_metodo_pago_usuario(metodo_pago_usuario)):
                metodo_pago_usuario = input("El metodo de pago no cumple con el formato solicitado. Ingrese un metodo de pago (efectivo|tarjeta)")

            usuarios[id_usuario]["nombre"] = nombre_modificado
            usuarios[id_usuario]["email"] = email_usuario
            usuarios[id_usuario]["telefono"] = telefono_usuario
            usuarios[id_usuario]["metodo de pago"] = metodo_pago_usuario.lower()

            print(f'Los datos del usuario {nombre_usuario} fueron actualizados')
        
        else: 
            print("No se encontro nignun cliente")
    except ValueError as valor_error:
        print(f"Error valor ingresado {valor_error}.")
    except KeyError as clave_error:
        print(f"Error clave {clave_error}")
    except IndexError as formato_nombre_error:
        print(f"Error sobre el formato del nombre ingresado {formato_nombre_error}.")
    except Exception as error_inesperado:
        print(f"Error inesperado {error_inesperado}.")

    return usuarios

def eliminar_usuarios(usuarios, conjunto_ids_usuarios):
    '''
    pre: recibe un diccionario ya creado y solicita el ID
    pos: elimina el usuario seleccionado y actualiza el diccionario
    '''
    try:
        id_usuario = (input("Cliente a eliminar (ingrese su ID)"))
        while (not validar_id_usuarios(id_usuario)):
            id_usuario = input("El ID ingresado no cumple con lo solicitado. Ingrese un id nuevamente (4 digitos): ")

        if id_usuario in conjunto_ids_usuarios:
            print(f"El cliente con el id {id_usuario} fue eliminado")
            del usuarios[id_usuario]
            conjunto_ids_usuarios.discard(id_usuario)
        else:
            print(f"El cliente con el {id_usuario}  no existe")
    except KeyError as clave_error:
        print(f"Error de clave no encontrada {clave_error}.")
    except ValueError as valor_error:
        print(f"Error valor ingresado {valor_error}.")
    except Exception as error_inesperado:
        print(f"Error inesperado {error_inesperado}.")
        
    return usuarios, conjunto_ids_usuarios

def guardar_usuarios_archivo(archivo, usuarios):
    '''
    pre: recibe el archivo JSON junto con el diccionario para hacer el guardado.
    pos: guarda los usuarios del diccionario en un archivo JSON:
  
    '''
    try:
        with open(archivo, "w", encoding="UTF-8") as archivo_usuarios:
            json.dump(usuarios, archivo_usuarios)
        print("Datos cargados exitosamente")
    except (FileNotFoundError, OSError) as error:
        print(f'Error {error}')
 
