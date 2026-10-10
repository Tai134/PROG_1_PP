from Funciones.Conversiones import *
from Funciones.Validaciones_Carac import *


def validar_legajo(legajo: str) -> bool:
    '''
    La función va a validar que el valor ingresado para los legajos
    sea correcto (números). Rompe el detectar que alguno o todos
    los str no son un número -> L-29
    
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
    sea correcto (letras). Rompe el detectar que alguno o todos los str
    no son letras -> L-57
    
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


def validar_nota(nota: str) -> bool:
    retorno = False

    if validar_legajo(nota) == True:
        valor = int(nota)

        if valor >= 1 and valor <= 10:
            retorno = True

    return retorno
