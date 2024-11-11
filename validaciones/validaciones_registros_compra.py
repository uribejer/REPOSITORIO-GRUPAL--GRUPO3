import re
from crd_registros_compra import *

def validar_id_registro_de_compra(id_registro_de_compra):
    ''' 
    pre: recibe una cadena de caracteres (en formato "xxxx")
    pos: devuelve una validacion True/Flase si cumple o no 
    '''
    patron_id_registro_de_compra = "^[0-9]{4}$"
    id_str = str(id_registro_de_compra)
    return (bool(re.match(patron_id_registro_de_compra, id_str)))

def validacion_fecha_compra(fecha_compra):
    ''' 
    pre: recibe una cadena de caracteres (en formato "dd-mm-aaaa)")
    pos: devuelve una validacion True/Flase si cumple o no 
    '''
    fecha_compra.strip()
    partes = fecha_compra.split("-")
    
    if len(partes) == 3:
        dia_compra, mes_compra, anio_compra = partes
        if dia_compra.isdigit() and mes_compra.isdigit() and anio_compra.isdigit():
            dia_compra = int(dia_compra)
            mes_compra = int(mes_compra)
            anio_compra = int(anio_compra)
            if (1 <= dia_compra <= 30) and (1 <= mes_compra <= 12 ) and (anio_compra >= 2024):
                return fecha_compra
            else:
                return False
        else:
            return False
    else: 
        return False
    
