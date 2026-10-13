from Validaciones.Validaciones_Carac import es_minus
from Validaciones.Validaciones_Carac import es_mayus
from Validaciones.Validaciones_Carac import es_letra

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


def primer_mayus(nombre: str) -> str:
    '''
    La función convierte la primera letra de cada palabra a mayúscula
    y el resto de las letras a minúscula.

    Args:
        nombre (str): Texto que se desea convertir.

    Returns:
        Retorna el texto con la primera letra de cada palabra en mayúscula.
    '''
    retorno = ""

    for i in range(len(nombre)):
        caracter = nombre[i]

        if i == 0:
            if es_letra(caracter) == True and caracter != " ":
                retorno += convertir_mayus(caracter)
            else:
                retorno += caracter
        elif caracter == " ":
            retorno += caracter
        elif nombre[i - 1] == " ": #Valido si hay un espacio antes de i
            retorno += convertir_mayus(caracter)
        else:
            retorno += convertir_minus(caracter)

    return retorno
