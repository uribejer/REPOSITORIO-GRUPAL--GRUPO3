from menu import menu_general

# ID(producto)    PRODUCTO      PRECIO       STOCK          

productos = [
    [2405, "Zapatilla Nike Air Force", 200000, 10],
    [7230, "Camiseta River Plate",80000, 2],
    [3789, "Buzo Adidas", 60000, 5], 
    [5501, "Remera Puma", 17000, 10] 
]
# ID DE USUARIO  --  NOMBRE  --  MAIL  --  NRO TELEFONO  --  METODO DE PAGO  

usuarios = { 
    "2010": {"nombre" : "T.VALENZUELA", "email" : "valenzuela@uade.edu.ar", "telefono" : "11-31971520", "metodo de pago" : "efectivo"},
    "4830": {"nombre" : "L.LAMAS", "email" : "lamas@uade.edu.ar", "telefono" : "11-36241255","metodo de pago" : "tarjeta"},
    "5990": {"nombre" : "U.BEJER", "email" : "bejer@uade.edu.ar", "telefono" : "11-42152979","metodo de pago" :"efectivo"}, 
    "1030": {"nombre" : "V.GARMENDIA", "email" :"garmendia@uade.edu.ar", "telefono" : "11-35792659","metodo de pago" : "tarjeta"} 
    }

# ID DE REGISTRO  --  ID DE USUARIO  --  PRODUCTOS A LLEVAR  --  PRECIOS  --  METODO DE PAGO  --  FECHA DE COMPRA
registros = [
    ["1020", "T.VALENZUELA", ["Zapatilla Nike Air Force"], [200000], "efectivo", "10-5-2024"],
    ["2222", "L.LAMAS", ["Remera Puma", "Buzo Adidas"], [17000, 60000], "tarjeta", "12-7-2024"]
]
#CONJUNTOS CON LOS IDs DE CADA DATO  
conjunto_ids_usuarios = {"2010", "4830", "5990", "1030"}
conjunto_ids_productos = {2405, 7230, 3789, 5501}
conjunto_ids_registros = {"1020", "2222"}

#ejecucion del sistema
menu_general(usuarios, productos, registros, conjunto_ids_usuarios, conjunto_ids_productos, conjunto_ids_registros)