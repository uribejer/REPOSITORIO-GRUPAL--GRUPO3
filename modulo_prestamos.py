#modulo_prestamos.py
#FUNCIONES DEL MODULO PRESTAMOS

def acciones_de_prestamos(prestamos, tabla_ordenada_libros, tabla_ordenada_clientes):
    #RECORREMOS LA LISTA DE CLIENTES #PARA PREGUNTAR A CADA CLIENTE SI QUIERE LLEVAR O NO 
    for cliente in tabla_ordenada_clientes:
        print(f"Cliente {cliente[1]}: ") #VAMOS CLIENTE POR CLIENTE 

        cuantos_libros_a_llevar = int(input("Cuantos libros quiere llevar: ")) #CUANTOS LIBROS QUIERE LLEVAR
        carrito = [] #SECCION FINAL CON TODOS LOS LIBROS
        while cuantos_libros_a_llevar > 0:
                seccion = [] #CREAMOS LA SECCION PARA CADA PRESTAMOS CON LOS DATOS 
                #SE AGREGAN LOS DATOS DEL CLIENTE
                seccion.append(cliente[0]) #ID DE CLIENTE, LO AGREGAMOS
                seccion.append(cliente[1])#NOMBRE DEL CLIENTE, LO AGREGAMOS
                seccion.append(cliente[2]) #EL METODO DE PAGO, LO AGREGAMOS

                libro_a_llevar = int(input("Que libro quiere llevar? (ingrese su ID) ")) #QUE LIBRO QUIERE LLEVAR EN BASE AL ID DEL LIBRO
                for libro in tabla_ordenada_libros: #VAMOS LIBRO POR LIBRO
                    if libro[0] == libro_a_llevar: #VERIFICAMOS QUE EL ID INGRESADO COINCIDA CON LA LA ITERACION

                        seccion_libro_a_llevar = [] #ACA VAN TODOS LOS DATOS DEL LIBRO
                        seccion_libro_a_llevar.append(libro[0]) #AGREGAMOS EL ID DEL LIBRO A LA SECCION DE LOS DATOS DEL LIBRO
                        seccion_libro_a_llevar.append(libro[1]) #AGREGAMOS EL TITULO DEL LIBRO A LA SECCION DE LOS DATOS DEL LIBRO
                        seccion_libro_a_llevar.append(libro[4]) #AGREGAMOS EL PRECIO DEL LIBRO A LA SECCION DE LOS DATOS DEL LIBRO

                        carrito.append(seccion_libro_a_llevar) #AGREGAMOS LA SECCION DEL LIBRO A LA SECCION CARRITO

                        cuantos_libros_a_llevar -= 1
        seccion = [cliente[0], cliente[1], cliente[2], carrito] #ACA VAN LOS DATOS DEL CLIENTE Y LA LISTA DE LIBROS
        prestamos.append(seccion)
    return prestamos

def imprimir_prestamos(prestamos):
    for cliente in prestamos:
        print(f"Cliente: {cliente[1]}")
        print(f"ID: {cliente[0]}")
        print(f"Método de pago: {cliente[2]}")
        print("Libros seleccionados:")
        
        if len(cliente[3]) > 0:  #CORROBORAMOS SI HAY LIBROS EN LA LISTA
            for libro in cliente[3]:
                print(f"  - ID Libro: {libro[0]}, Título: {libro[1]}, Precio: ${libro[2]}")
        else:
            print("  No seleccionó ningún libro.")
        
        print("-" * 40)  #SEPARAMOS ENTRE CADA CLIENTE

def filtrar_prestamos_por_metodo_pago(prestamos):
    #LISTA DE CLIENTE QUE PAGAN EN EFECTIVO
    clientes_efectivo = [cliente for cliente in prestamos if cliente[2].lower() == 'efectivo']

    #LISTA DE CLIENTES QUE PAGAN CON TARJETA
    clientes_tarjeta = [cliente for cliente in prestamos if cliente[2].lower() == 'tarjeta']

    #RETORNAMOS LAS DOS LISTAS ACA
    return clientes_efectivo, clientes_tarjeta

def impresion_por_metodo_de_pago(clientes_efectivo, clientes_tarjeta):
    print("Clientes que pagan en efectivo:")
    for cliente in clientes_efectivo:
        print(f"El cliente {cliente[1]} paga en efectivo")

    print("-" * 40)

    print("\nClientes que pagan con tarjeta:")
    for cliente in clientes_tarjeta:
        print(f"El cliente {cliente[1]} paga con tarjeta")


def impresion_total(totales_por_cliente):
    for cliente, total in totales_por_cliente:
        print(f"Cliente: {cliente} - Total de libros: ${total}")