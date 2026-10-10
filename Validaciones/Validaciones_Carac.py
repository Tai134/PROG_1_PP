def es_letra(caracter: str) -> bool:
    '''
    La función va a corroborar que el valor ingresado sea una letra 
    trabajando con comprobaciones en el codigo ASCII.
    
    Args: 
        Recibe valores en forma de str
    Returns:
        Retorna un bool / True = es una letra
                        / False = NO es una letra
    '''

    retorno = False

    if ord(caracter) >= 65 and ord(caracter) <= 90:
        retorno = True
    elif ord(caracter) >= 97 and ord(caracter) <= 122:
        retorno = True
    elif ord(caracter) == 32:
        retorno = True

    return retorno

def es_minus(letra:str)->bool:
    '''
    La función va a corroborar que el valor ingresado sea una minuscula
    Para unificar la escritura y funcionamiento comparte sintaxis con
    validacion de letras.
    
    Args: 
        Recibe valores en forma de str
    Returns:
        Retorna un bool / True = es minuscula
                        / False = es mayuscula
    '''

    retorno = True
    validacion = ord(letra)
   
    if validacion >= 97 and validacion <= 122:
        retorno = True
    
    elif validacion >= 65 and validacion <=90:
        retorno = False
    
    return retorno

def es_mayus(letra:str)->bool:
    '''
    La función va a corroborar que el valor ingresado sea una mayuscula
    Para unificar la escritura y funcionamiento comparte sintaxis con
    validacion de letras.
    
    Args: 
        Recibe valores en forma de str
    Returns:
        Retorna un bool / True = es mayuscula
                        / False = es minuscula
    '''
    retorno = True
    validacion = ord(letra)
   
    if validacion >= 65 and validacion <= 90:
        retorno = True
    
    elif validacion >= 97 and validacion <=122:
        retorno = False
    
    return retorno


def es_numero(caracter: str) -> bool:
    '''
    La función va a corroborar que el valor ingresado sea un número
    Para unificar la escritura y funcionamiento comparte sintaxis con
    validacion de letras.
    
    Args: 
        Recibe valores en forma de str
    
    Returns:
        Retorna un bool / True = es un número
                        / False = NO es número
    '''

    retorno = False

    if ord(caracter) >= 48 and ord(caracter) <= 57:
        retorno = True

    return retorno