#modulo_clientes.py
#FUNCIONES DEL MODULO CLIENTES

def desordenada_clientes(clientes):
    # IMPRESION ENCABEZADO CON FORMATO f-strings (CLIENTES)
    print(f"{'ID':^10} {'NOMBRE':^30} {'METODO DE PAGO':^30}")
    print('-' * 96)

    for cliente in clientes:
        print(f"{cliente[0]:^10} {cliente[1]:^30} {cliente[2]:^30}")
    return clientes


def agregar_clientes (clientes, cant_clientes_agregar):
    i = 1
    for i in range (cant_clientes_agregar):
        cliente = []
        ID = int(input("Ingrese el ID: "))
        cliente.append(ID)
        nombre = (input("Ingrese el nombre del cliente (Nombre y Apellido): "))
        cliente.append(nombre)
        metodo_pago = (input("Ingrese el metodo de pago (efectivo / tarjeta): ")).lower()
        while (metodo_pago != 'efectivo') and (metodo_pago != 'tarjeta'):
            print('El metodo de pago es invalido. Tiene que ser efectivo o tarjeta')
            metodo_pago = (input("Ingrese el metodo de pago (efectivo / tarjeta): ")).lower()
        cliente.append(metodo_pago)
        
        clientes.append(cliente)  
    return clientes
        
def modificar_nombre (tabla_clientes_actualizada):
    for cliente in tabla_clientes_actualizada:
        for dato in cliente:
            if dato == cliente[1]:
                nombre_completo = cliente[1]   
                nombre_completo.strip() #elimina espacio sobrantes al principio y al final del texto
                nombre, apellido = nombre_completo.split(' ', 1) #divide el nombre y apellido por el primer espacio
                nombre_modificado = (f"{nombre[0].upper()}.{apellido.upper()}")
                cliente[1] = nombre_modificado
    return tabla_clientes_actualizada


def eliminar_cliente(tabla_clientes_actualizada):
    print()
    print(f"{'ID':^10} {'NOMBRE':^30} {'METODO DE PAGO':^30}")
    print('-' * 96)
    for cliente in tabla_clientes_actualizada:
        print(f"{cliente[0]:^10} {cliente[1]:^30} {cliente[2]:^30}")
    cuantos_clientes_eliminar = int(input("Cuantos clientes quiere eliminar? "))
    while cuantos_clientes_eliminar > 0:
        cliente_a_eliminar = int(input("Que cliente quiere eliminar (ingrese su ID)? "))
        for cliente in tabla_clientes_actualizada:
            if cliente[0] == cliente_a_eliminar:
                tabla_clientes_actualizada.remove(cliente)
                cuantos_clientes_eliminar -= 1
                print(f"El cliente {cliente[1]} fue eliminado")
    return  tabla_clientes_actualizada
         
def ordenada_clientes(tabla_ordenada_clientes):
    # IMPRESION ENCABEZADO CON FORMATO f-strings (CLIENTES)
    print()
    print(f"{'ID':^10} {'NOMBRE':^30} {'METODO DE PAGO':^30}")
    print('-' * 96)

    for cliente in tabla_ordenada_clientes:
        print(f"{cliente[0]:^10} {cliente[1]:^30} {cliente[2]:^30}")

    return tabla_ordenada_clientes
