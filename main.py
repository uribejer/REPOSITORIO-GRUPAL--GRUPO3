from modulo_clientes import *
from modulo_productos import *
from modulo_prestamos import *

#TABLA CLIENTES
clientes = [
    [2, 'Thiago Valenzuela', 'efectivo'],
    [4, 'Luciano Lamas', 'tarjeta'],
    [5, 'Uriel Bejer', 'efectivo'], 
    [10, 'Valentino Garmendia','tarjeta'] 
]

#TABLA PRODUCTOS
libros = [
    [2, "Cien años de soledad", "Gabriel García Márquez", "Sudamericana", 100.5],
    [7, "Fervor de Buenos Aires", "Jorge Luis Borges", "Emecé", 80],
    [3, "La casa de los conejos", "Laura Alcoba", "Edhasa", 20], 
    [5, "El secreto de sus ojos", "Eduardo Sacheri", "Alfaguara", 95.80] 
]

#TABLA PRESTAMOS
prestamos = []

#LLAMADO A FUNNCIONES CLIENTES
impresion_tabla_desordenada_clientes = desordenada_clientes(clientes)
cant_clientes_agregar = int(input("Cuantos clientes se agregaran? "))
tabla_clientes_actualizada = agregar_clientes (clientes, cant_clientes_agregar)
tabla_clientes_actualizada = modificar_nombre (tabla_clientes_actualizada)
tabla_clientes_actualizada = eliminar_cliente(tabla_clientes_actualizada)
tabla_ordenada_clientes = sorted(tabla_clientes_actualizada, key=lambda cliente: (cliente[0]))
impresion_tabla_ordenada_clientes = ordenada_clientes(tabla_ordenada_clientes)

#LLAMADO A FUNNCIONES PRODUCTOS
impresion_tabla_desordenada_libros = desordenada_libros(libros)
cant_libros_agregar = int(input("Cuantos libros se agregaran? "))
tabla_libros_actualizada = agregar_libros (libros, cant_libros_agregar)
tabla_libros_actualizada = modificar_autor (tabla_libros_actualizada)
tabla_libros_actualizada = eliminar_libro(tabla_libros_actualizada)
tabla_ordenada_libros = sorted(tabla_libros_actualizada, key=lambda libro: (libro[0], -libro[4]))
impresion_tabla_ordenada_libros = ordenada_libros(tabla_ordenada_libros)

#LLAMDO A FUNCIONES PRESTAMOS
prestamos_data = acciones_de_prestamos(prestamos, tabla_ordenada_libros, tabla_ordenada_clientes)
print("-" * 40) 
imprimir_prestamos(prestamos)
clientes_efectivo, clientes_tarjeta = filtrar_prestamos_por_metodo_pago(prestamos)
print("Clientes que pagan en efectivo:")
for cliente in clientes_efectivo:
    print(cliente)

print("\nClientes que pagan con tarjeta:")
for cliente in clientes_tarjeta:
    print(cliente)

print()

#USAMOS UNA LISTA POR COMPRENSION CON UNA FUNCION LAMBDA INCLUIDA PARA CALCULAR EL TOTAL
totales_por_cliente = [(cliente[1], sum(map(lambda libro: libro[2], cliente[3]))) for cliente in prestamos]

#SE IMPRIMEN EL RESULTADO
for cliente, total in totales_por_cliente:
    print(f"Cliente: {cliente} - Total de libros: ${total}")