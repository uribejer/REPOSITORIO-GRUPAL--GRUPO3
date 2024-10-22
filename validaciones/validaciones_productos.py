import re
from crud_productos import * 

def validar_id_libro (id_libro):
    ''' 
    pre: recibe una cadena de caracteres (en formato "xxxx")
    pos: devuelve una validacion True/Flase si cumple o no 
    '''
    patron_id_libro = "^[0-9]{4}$"
    id_str = str(id_libro)
    return (bool(re.match(patron_id_libro, id_str)))

def validar_titulo_libro (titulo_libro):
    ''' 
    pre: recibe una cadena de caracteres de tipo string 
    pos: devuelve una validacion True/Flase si cumple o no 
    '''
    patron_titulo_libro = "^[A-Za-z0-9\s]+$"
    return (bool(re.match(patron_titulo_libro, titulo_libro)))


def validar_autor_libro (autor_libro):
    ''' 
    pre: recibe una cadena de caracteres de tipo string (en formato "Nombre y Apellido")
    pos: devuelve una validacion True/Flase si cumple o no 
    '''
    patron_autor_libro = "^[A-Z][a-z]+ [A-Z][a-z]+$"
    return (bool(re.match(patron_autor_libro, autor_libro)))

def validar_precio_libro (precio_libro):
    ''' 
    pre: recibe un numero entero para el precio
    pos: devuelve una validacion True/Flase si cumple o no 
    '''
    patron_precio_libro = "^[0-9]+$"
    precio_str = str(precio_libro)
    return (bool(re.match(patron_precio_libro, precio_str)))

def validar_ejemplares_libro (ejemplares_libro):
    ''' 
    pre: recibe un numero entero para la cantidad de ejemplares
    pos: devuelve una validacion True/Flase si cumple o no 
    '''

    patron_ejemplares_libro = "^[0-9]+$"
    ejemplares_str = str(ejemplares_libro)
    return (bool(re.match(patron_ejemplares_libro, ejemplares_str)))