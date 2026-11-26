def es_numero(caracter: str) -> bool:
    '''
    La función comprueba si un carácter corresponde a un dígito.

    Args:
        caracter (str): Carácter que se desea comprobar.

    Returns:
        Retorna True si es un dígito y False si no.
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
        Retorna True si es una letra o espacio y False si no.
    '''
    retorno = False
    if len(caracter) == 1:
        codigo = ord(caracter)
        if codigo >= 65 and codigo <= 90:
            retorno = True
        elif codigo >= 97 and codigo <= 122:
            retorno = True
        elif codigo == 32:
            retorno = True
    return retorno


def validar_legajo(texto: str) -> bool:
    '''
    La función valida que un legajo tenga cinco cifras numéricas.

    Args:
        texto (str): Legajo ingresado o leído como texto.

    Returns:
        Retorna True si cumple el formato y False si no.
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


def validar_legajo_unico(legajo: int, estudiantes: list,
                         cantidad_cargada: int) -> bool:
    '''
    La función comprueba que el legajo no esté repetido.

    Args:
        legajo (int): Legajo que se desea comprobar.
        estudiantes (list): Estudiantes cargados hasta el momento.
        cantidad_cargada (int): Cantidad de estudiantes de la lista.

    Returns:
        Retorna True si el legajo es único y False si ya existe.
    '''
    retorno = True
    for i in range(cantidad_cargada):
        if estudiantes[i]["Legajo"] == legajo:
            retorno = False
            break
    return retorno


def validar_nombre(nombre: str) -> bool:
    '''
    La función valida un nombre formado por palabras y espacios simples.

    Args:
        nombre (str): Nombre completo del estudiante.

    Returns:
        Retorna True si contiene letras y False si no.
    '''
    retorno = True
    if len(nombre) == 0 or nombre[0] == " " or nombre[-1] == " " \
            or " " not in nombre:
        retorno = False
    else:
        espacio_anterior = False
        for caracter in nombre:
            if es_letra(caracter) == False:
                retorno = False
                break
            if caracter == " " and espacio_anterior == True:
                retorno = False
                break
            if caracter == " ":
                espacio_anterior = True
            else:
                espacio_anterior = False
    return retorno


def validar_genero(genero: str) -> bool:
    '''
    La función valida F, M o X, en mayúscula o minúscula.

    Args:
        genero (str): Género ingresado o leído del archivo.

    Returns:
        Retorna True si el género es válido y False si no.
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
    La función valida que una nota sea un entero entre uno y diez.

    Args:
        texto (str): Nota ingresada o leída del archivo.

    Returns:
        Retorna True si la nota es válida y False si no.
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
    La función valida que la materia sea un número entre uno y cinco.

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


def validar_campos_csv(campos: list, estudiantes: list) -> bool:
    '''
    La función valida los datos de un registro leído desde el CSV.

    Args:
        campos (list): Valores separados por comas de un registro.
        estudiantes (list): Registros leídos antes que el actual.

    Returns:
        Retorna True si todos los datos son válidos y False si no.
    '''
    retorno = False
    if len(campos) == 9:
        if validar_legajo(campos[0]) == True \
                and validar_nombre(campos[1]) == True \
                and validar_genero(campos[2]) == True:
            legajo = int(campos[0])
            retorno = validar_legajo_unico(legajo, estudiantes,
                                           len(estudiantes))
            if retorno == True:
                for i in range(3, 8):
                    if validar_nota(campos[i]) == False:
                        retorno = False
                        break
            if retorno == True and campos[8] != "0":
                if validar_nota(campos[8]) == False:
                    retorno = False
    return retorno
