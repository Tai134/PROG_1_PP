from Validaciones.Validaciones_Carac import *

def convertir_minus(letra: str) -> str:
    validacion = es_minus(letra)
    
    if validacion == True:
        resultado = letra
    elif validacion == False:
        resultado = chr(ord(letra) + 32)
        
    return resultado

def convertir_mayus(letra: str) -> str:
    validacion = es_mayus(letra)
    
    if validacion == True:
        resultado = letra
    elif validacion == False:
        resultado = chr(ord(letra) - 32)
        
    return resultado