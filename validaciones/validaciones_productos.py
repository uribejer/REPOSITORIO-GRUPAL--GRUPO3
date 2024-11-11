import re
from crud_productos import * 

def validar_id_producto(id_producto):
    ''' 
    pre: recibe una cadena de caracteres (en formato "xxxx")
    pos: devuelve una validacion True/Flase si cumple o no 
    '''
    patron_id_producto = "^[0-9]{4}$"
    id_str = str(id_producto)
    return (bool(re.match(patron_id_producto, id_str)))

def validar_producto(producto):
    ''' 
    pre: recibe una cadena de caracteres de tipo string 
    pos: devuelve una validacion True/Flase si cumple o no 
    '''
    patron_producto = "^[A-Za-z0-9\s]+$"
    return (bool(re.match(patron_producto, producto)))


def validar_precio_producto (precio_producto):
    ''' 
    pre: recibe un numero entero para el precio
    pos: devuelve una validacion True/Flase si cumple o no 
    '''
    patron_precio_producto = "^[0-9]+$"
    precio_str = str(precio_producto)
    if (bool(re.match(patron_precio_producto, precio_str))):
        return int(precio_str) > 0 
    return False 

def validar_stock_producto (stock_producto):
    ''' 
    pre: recibe un numero entero para la cantidad de stock
    pos: devuelve una validacion True/Flase si cumple o no 
    '''
    patron_stock_producto= "^[0-9]+$"
    stock_str = str(stock_producto)
    if (bool(re.match(patron_stock_producto, stock_str))):
        return int(stock_str) >= 0
    return False