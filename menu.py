from crud_productos import *
from crud_usuarios import *
from crd_registros_compra import *


def menu_general(usuarios, productos, registros, conjunto_ids_usuarios, conjunto_ids_productos, conjunto_ids_registros):
    while True:
        try:
            opcion = int(input("1) Gestion de Usarios 2) Gestion de Productos 3) Gestion de Registros de compra 4) Salir: "))
            if opcion == 1:
                while True:
                    mostrar_menu_usuarios()
                    try:
                        seleccion = (input("Seleccione una opción: "))
                        
                        if (not(seleccion.isdigit())):
                            raise ValueError("El valor ingreasado debe ser un numero.")
                        
                        seleccion = int(seleccion)

                        if seleccion == 1:
                            crear_usuario(usuarios, conjunto_ids_usuarios)
                        elif seleccion == 2:
                            leer_usuarios(usuarios)
                        elif seleccion == 3:
                            actualizar_usuarios(usuarios, conjunto_ids_usuarios)
                        elif seleccion == 4:
                            eliminar_usuarios(usuarios, conjunto_ids_usuarios)
                        elif seleccion == 5:
                            print("Saliendo del sistema...")
                            break
                        else:
                            print("Opción inválida, por favor intente nuevamente.")
                    except ValueError as msj_error:
                        print(f"Error valor ingresado no numerico {msj_error}. Ingrese un numero porfavor.")
            elif opcion == 2:
                while True:
                    mostrar_menu_productos()
                    try:
                        seleccion = (input("Seleccione una opción: "))

                        if (not(seleccion.isdigit())):
                            raise ValueError("El valor ingreasado debe ser un numero.")
                        
                        seleccion = int(seleccion)

                        if seleccion == 1:
                            agregar_producto(productos, conjunto_ids_productos)
                        elif seleccion == 2:
                            leer_productos(productos)
                        elif seleccion == 3:
                            actualizar_ejemplares(productos, conjunto_ids_productos)
                        elif seleccion == 4:
                            eliminar_producto(productos, conjunto_ids_productos)
                        elif seleccion == 5:
                            guardar_productos_en_archivo(productos)
                        elif seleccion == 6:
                            print("Saliendo del sistema...")
                            break
                        else:
                            print("Opción inválida, por favor intente nuevamente. ")
                    except ValueError as msj_error:
                        print(f"Error valor ingresado no numerico {msj_error}. Ingrese un numero porfavor.")
            elif opcion == 3:
                 while True:
                    mostrar_menu_registros_compra()
                    try:
                        seleccion = (input("Seleccione una opción: "))

                        if (not(seleccion.isdigit())):
                            #forzamos al error 
                            raise ValueError("El valor ingreasado debe ser un numero.")
                        
                        seleccion = int(seleccion)

                        if seleccion == 1:
                            agregar_registros(productos, registros, conjunto_ids_registros, conjunto_ids_usuarios)
                        elif seleccion == 2:
                            leer_registros(registros)
                        elif seleccion == 3:
                            eliminar_registro(registros, conjunto_ids_registros)
                        elif seleccion == 4:
                            print("Saliendo del sistema...")
                            break
                        else:
                            print("Opción inválida, por favor intente nuevamente.")
                    except ValueError as msj_error:
                        print(f"Error valor ingresado no numerico {msj_error}. Ingrese un numero porfavor.")            
            elif opcion == 4:
                print("Saliendo del sistema...")
                break
            else: 
                print("Opción inválida, por favor intente nuevamente.")
        except ValueError:
            print("Error: Valor ingresado no numerico. Ingrese un numero porfavor.")