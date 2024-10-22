from menu import menu_general

# ID(libro)    TITULO      AUTOR       PRECIO          CANTIDAD DISPONIBLE

libros = [
    [2405, "Cien años de soledad", "Gabriel García Márquez", 100, 3],
    [7230, "Fervor de Buenos Aires", "Jorge Luis Borges", 80, 2],
    [3789, "La casa de los conejos", "Laura Alcoba", 20, 5], 
    [5501, "El secreto de sus ojos", "Eduardo Sacheri", 95, 10]
]
# ID(usuario)    NOMBRE      MAIL       NRO TELEFONO          METODO DE PAGO  

usuarios = { 
    "2010": {"nombre" : "T.VALENZUELA", "email" : "valenzuela@uade.edu,ar", "telefono" : "11-31971520", "metodo de pago" : "efectivo"},
    "4830": {"nombre" : "L.LAMAS", "email" : "lamas@uade.edu.ar","telefono" : "11-36241255","metodo de pago" : "tarjeta"},
    "5990": {"nombre" : "U.BEJER", "email" : "bejer@uade.edu.ar","telefono" : "11-42152979","metodo de pago" :"efectivo"}, 
    "1030": {"nombre" : "V.GARMENDIA", "email" :"garmendia@uade.edu.ar","telefono" : "11-35792659","metodo de pago" : "tarjeta"} 
    }
    
# ID(usuario)   LIRBOS A LLEVAR     PRECIO TOTAL    FECHA DE COMPRA
registros = {
    "2010": {"libros a llevar" : ["Cien años de soledad"], "precio total" : "100", "fecha de compra" : "10-5-2024"}
}

conjunto_ids_usuarios = {"2010", "4830", "5990", "1030"}
conjunto_ids_libros = {2405, 7230, 3789, 5501}
conjunto_ids_registros = {"2010"}

# Ejecutar el sistema
menu_general(usuarios, libros, registros, conjunto_ids_usuarios, conjunto_ids_libros, conjunto_ids_registros)