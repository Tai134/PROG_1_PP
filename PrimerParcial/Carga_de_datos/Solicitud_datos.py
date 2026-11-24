from Validaciones.Validaciones_Texto import validar_legajo
from Validaciones.Validaciones_Texto import validar_nombre
from Validaciones.Validaciones_Texto import validar_genero
from Validaciones.Validaciones_Texto import validar_nota


def solicitar_legajo() -> int:
    '''
    La función solicita un legajo y lo valida antes de devolverlo.
    Valida lo ingresado llamando a validar_legajo y repite la solicitud
    mientras el dato ingresado no sea válido.

    Returns:
        Retorna el legajo validado como un número entero.
    '''
    retorno = 0
    validacion = False

    while validacion == False:
        legajo = input("Ingrese el legajo: ")
        validacion = validar_legajo(legajo)

        if validacion == True:
            retorno = int(legajo)
        else:
            print("El legajo ingresado no es válido")

    return retorno


def solicitar_nombre() -> str:
    '''
    La función solicita el apellido y nombre de un estudiante. Valida
    llamando a validar_nombre y repite la solicitud mientras el dato
    ingresado no sea válido.

    Returns:
        Retorna el apellido y nombre validado como un str.
    '''
    retorno = ""
    validacion = False

    while validacion == False:
        nombre = input("Ingrese el apellido y nombre: ")
        validacion = validar_nombre(nombre)

        if validacion == True:
            retorno = nombre
        else:
            print("El apellido y nombre ingresado no es válido")

    return retorno


def solicitar_genero() -> str:
    '''
    La función solicita el género de un estudiante y lo valida.
    Valida llamando a validar_genera y repite la solicitud mientras el
    dato ingresado no sea válido.

    Returns:
        Retorna el género validado como un str.
    '''
    retorno = ""
    validacion = False

    while validacion == False:
        genero = input("Ingrese el género (F - M - X): ")
        validacion = validar_genero(genero)

        if validacion == True:
            retorno = genero
        else:
            print("El género ingresado no es válido")

    return retorno


def solicitar_nota(numero_nota: int) -> int:
    '''
    La función solicita una nota y la valida dentro del rango permitido.
    Valida llamando a validar_nota y repite la solicitud mientras el 
    dato ingresado no sea válido.

    Returns:
        numero_nota (int): Indica si se solicita la nota 1 o la nota 2.

        Retorna la nota validada como un número entero.
    '''
    retorno = 0
    validacion = False

    while validacion == False:
        nota = input(f"Ingrese la nota {numero_nota} (1 a 10): ")
        validacion = validar_nota(nota)

        if validacion == True:
            retorno = int(nota)
        else:
            print("La nota ingresada no es válida")

    return retorno
