import re
from crud_usuarios import * 

def validar_id_usuarios (id_usuario):
    ''' 
    pre: recibe una cadena de caracteres (en formato "xxxx")
    pos: devuelve una validacion True/Flase si cumple o no 
    '''
    patron_id_usuarios = "^[0-9]{4}$"
    return (bool(re.match(patron_id_usuarios, id_usuario)))

def validar_nombre_usuarios (nombre_usuario):
    ''' 
    pre: recibe una cadena de caracteres de tipo string (en formato "Nombre y Apellido")
    pos: devuelve una validacion True/Flase si cumple o no 
    '''
    patron_nombre_usuario = "^[A-Z][a-z]+ [A-Z][a-z]+$"
    return (bool(re.match(patron_nombre_usuario, nombre_usuario)))

def validar_email_usuario (email_usuario):
    ''' 
    pre: recibe una cadena de caracteres de tipo string (en formato "xxxxxx@xxx.xxxx.xxx")
    pos: devuelve una validacion True/Flase si cumple o no 
    '''

    patron_email_usuario = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return (bool(re.match(patron_email_usuario, email_usuario)))

def validar_telefono_usuario(telefono_usuario):
    ''' 
    pre: recibe una cadena de caracteres de numeros (xx-xxxxxxxx)
    pos: devuelve una validacion True/Flase si cumple o no 
    '''
    patron_telefono_usuario = "^[0-9]{2}-[0-9]{8}$"
    return (bool(re.match (patron_telefono_usuario, telefono_usuario)))


def validar_metodo_pago_usuario(metodo_pago_usuario):           
    ''' 
    pre: recibe una cadena de caracteres 
    pos: devuelve una validacion True/Flase si cumple o no 
    '''

    patron_metodo_pago_usuario = "^(efectivo|tarjeta)$"
    return (bool(re.match (patron_metodo_pago_usuario, metodo_pago_usuario, re.IGNORECASE)))


