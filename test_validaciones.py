from validaciones.validaciones_usuarios import validar_telefono_usuario
from validaciones.validaciones_productos import validar_precio_producto

def tester_validacion_telefono_usuario():
    assert(validar_telefono_usuario("11-34352034")) == True
    assert(validar_telefono_usuario("Hello World")) == False
    assert(validar_telefono_usuario("1130343637"))  == False

def tester_validacion_precio_producto():
    assert(validar_precio_producto(5000)) == True
    assert(validar_precio_producto('"#@.?"')) == False
    assert(validar_precio_producto("Hello World")) == False