from Operaciones.Conversiones import *
from Validaciones.Validaciones_Carac import *


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


def validar_legajo_repetido(legajo: int, legajos: list,
                            cantidad_cargada: int) -> bool:
    '''
    La función valida que el legajo ingresado no se encuentre repetido
    entre los legajos que ya fueron cargados.

    Args:
        Recibe el legajo y la lista de legajos cargados hasta el momento.

    Returns:
        Retorna True si el legajo no está repetido y False si ya existe.
    '''
    retorno = True

    for i in range(cantidad_cargada):
        if legajo == legajos[i]:
            retorno = False
            break

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

    if len(nombre) == 0 or nombre[0] == " " or nombre[-1] == " " \
            or " " not in nombre:
        # Exige nombre y apellido y evita ' Pablo' y 'Juan'
        retorno = False
    else:
        espacio_anterior = False

        for i in nombre:
            if i == " " and espacio_anterior == True:
                retorno = False
                break

            valor = es_letra(i)

            if valor == False:
                retorno = False
                break # Rompe al encontrar un valor que NO es una letra

            if i == " ":
                espacio_anterior = True
            else:
                espacio_anterior = False

    return retorno


def validar_genero(genero: str) -> bool:
    '''
    La función va a validar que el género ingresado sea F, M o X.
    Acepta tanto letras mayúsculas como minúsculas y realiza la
    conversión a mayúscula antes de validar.
    
    Args:
        Recibe un str

    Returns:
        Retorna un bool / True = Es F-M-X y se valida.
                        / False = NO es F-M-X y NO se valida.
    '''
    retorno = False

    if len(genero) == 1: # Comprueba que se sea de un solo digito
        
        #Convierte a mayus para poder validar sin importar que ingrese
        genero_mayus = convertir_mayus(genero) 

        if genero_mayus == "F" or genero_mayus == "M" or genero_mayus == "X":
            retorno = True
    
    return retorno


def validar_nota(nota: str) -> bool:
    '''
    La función primero valida que el que no sea un str vacio (' ') luego
    valida que el caracter ingresado efectivamente sea un número haciendo
    la llamada a la funcion es_numero. Si lo comprueba convierte el valor
    a int para validar que sea un valor entre 1 y 10 (Notas validas).

    Args:
        Recibe un str

    Retorno:
            Retorna un bool / True = La nota esta entre 1 y 10
                            / False = NO es un valor int o 1 > nota > 10
    '''
    retorno = True

    if len(nota) == 0:
        retorno = False
    else:
        for i in nota:
            valor = es_numero(i)

            if valor == False:
                retorno = False
                break

    if retorno == True:
        valor = int(nota)

        if valor < 1 or valor > 10:
            retorno = False

    return retorno
