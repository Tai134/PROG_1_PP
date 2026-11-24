def es_numero(caracter: str) -> bool:
    '''
    La función comprueba si un carácter corresponde a un dígito decimal.

    Args:
        caracter (str): Carácter que se desea comprobar.

    Returns:
        Retorna True si es un número y False en caso contrario.
    '''
    retorno = False
    if len(caracter) == 1 and ord(caracter) >= 48 and ord(caracter) <= 57:
        retorno = True
    return retorno


def es_letra(caracter: str) -> bool:
    '''
    La función comprueba si un carácter es una letra o un espacio.

    Args:
        caracter (str): Carácter que se desea comprobar.

    Returns:
        Retorna True si es una letra o espacio y False en caso contrario.
    '''
    retorno = False
    if len(caracter) == 1:
        codigo = ord(caracter)
        if codigo >= 65 and codigo <= 90: #Mayusculas
            retorno = True
        elif codigo >= 97 and codigo <= 122: #Minusculas
            retorno = True
        elif codigo == 32: #Espacio
            retorno = True
    return retorno


def validar_legajo(texto: str) -> bool:
    '''
    La función valida que el legajo tenga exactamente cinco cifras.

    Args:
        texto (str): Legajo ingresado como texto.

    Returns:
        Retorna True si es válido y False si no cumple.
    '''
    retorno = True
    if len(texto) != 5:
        retorno = False
    else:
        for caracter in texto:
            if es_numero(caracter) == False:
                retorno = False
                break
    return retorno


def validar_legajo_unico(legajo: int, legajos: list,
                         cargados: int) -> bool:
    '''
    La función comprueba que el legajo no esté repetido entre los cargados.

    Args:
        legajo (int): Legajo que se desea validar.
        legajos (list): Lista de legajos ya ingresados.
        cargados (int): Cantidad de legajos ya cargados.

    Returns:
        Retorna True si es único y False si ya existe.
    '''
    retorno = True
    for i in range(cargados):
        if legajos[i] == legajo:
            retorno = False
            break
    return retorno


def validar_nombre(nombre: str) -> bool:
    '''
    La función valida un nombre con al menos dos palabras, letras y espacios
    simples, sin espacios al inicio ni al final.

    Args:
        nombre (str): Nombre ingresado.

    Returns:
        Retorna True si es válido y False si no cumple.
    '''
    retorno = True
    if len(nombre) == 0 or nombre[0] == " " or nombre[-1] == " " or " " not in nombre:
        retorno = False
    else:
        doble_espacio = False
        for caracter in nombre:
            if es_letra(caracter) == False:
                retorno = False
                break
            if caracter == " " and doble_espacio == True:
                retorno = False
                break
            if caracter == " ":
                doble_espacio = True
            else:
                doble_espacio = False
    return retorno


def validar_genero(genero: str) -> bool:
    '''
    La función valida que el género sea F, M o X en mayúscula o minúscula.

    Args:
        genero (str): Género ingresado.

    Returns:
        Retorna True si es válido y False si no cumple.
    '''
    retorno = False
    if len(genero) == 1:
        codigo = ord(genero[0])
        if codigo >= 97 and codigo <= 122:
            genero = chr(codigo - 32)
            
        if genero == "F" or genero == "M" or genero == "X":
            retorno = True
    return retorno


def validar_nota(texto: str) -> bool:
    '''
    La función valida que la nota sea un número entero entre 1 y 10.

    Args:
        texto (str): Nota ingresada como texto.

    Returns:
        Retorna True si es válida y False si no cumple.
    '''
    retorno = True
    if len(texto) == 0 or len(texto) > 2:
        retorno = False
    else:
        for caracter in texto:
            if es_numero(caracter) == False:
                retorno = False
                break
    if retorno == True:
        nota = int(texto)
        if nota < 1 or nota > 10:
            retorno = False
    return retorno


def validar_materia(texto: str) -> bool:
    '''
    La función valida que el número de materia esté entre 1 y 5.

    Args:
        texto (str): Número de materia ingresado como texto.

    Returns:
        Retorna True si corresponde a una materia y False si no.
    '''
    retorno = False
    if len(texto) == 1 and es_numero(texto) == True:
        materia = int(texto)
        if materia >= 1 and materia <= 5:
            retorno = True
    return retorno
