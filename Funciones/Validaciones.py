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


def validar_legajo(legajo: str) -> bool:
    '''
    La función va a validar que el valor ingresado para los legajos
    sea correcto (números). Rompe el detectar que alguno o todos los str no son
    un número -> L-68
    
    Args: 
        Recibe valores en forma de str
    
    Returns:
        Retorna un bool / True = es o son números (validado)
                        / False = NO es o NO son números (NO validado)
    '''
    retorno = True

    if len(legajo) == 0:
        retorno = False
    else:
        for i in range(len(legajo)):
            caracter = legajo[i]
            valor = es_numero(caracter)

            if valor == False:
                retorno = False
                break #Rompe al encontrar un valor que NO es un número

    return retorno


def validar_nombre(nombre: str) -> bool:
    '''
    La función va a validar que el valor ingresado para los nombres
    sea correcto (letras). Rompe el detectar que alguno o todos los str no son
    letras -> L-96
    
    Args: 
        Recibe valores en forma de str
    
    Returns:
        Retorna un bool / True = es o son letras (validado)
                        / False = NO es o NO son letras (NO validado)
    '''
    retorno = True

    if len(nombre) == 0:
        retorno = False
    else:
        for i in nombre:
            valor = es_letra(i)

            if valor == False:
                retorno = False
                break # Rompe al encontrar un valor que NO es una letra

    return retorno


def validar_genero(genero: str) -> bool:
    '''
    La función valido que el genero sea una de tres opciones unicamente.
    Comprueba los unicos tres valores validos (F-M-X). Comprueba 
    
    Args:
        Recibe un str

    Returns:
        Retorna un bool / True = Es F-M-X y se valida.
                        / False = NO es F-M-X y NO se valida.
    '''
    retorno = False

#convertir tanto mayus como minusculas a mayus y ahi comprobar para que si pongo f o F igual me devuelva F

    # if genero == "F" or genero == "M" or genero == "X":
    #     retorno = True
   
    # elif genero == "f" or genero == "m" or genero == "x":
    #     retorno = True 
    
    return retorno

prueba = validar_genero('f')
print(prueba)


def validar_nota(nota: str) -> bool:
    retorno = False

    if validar_legajo(nota) == True:
        valor = int(nota)

        if valor >= 1 and valor <= 10:
            retorno = True

    return retorno
