def obtener_mayor_promedio(promedios: list) -> float:
    '''
    La función obtiene el mayor promedio de la lista de promedios.

    Args:
        promedios (list): Lista con los promedios de los estudiantes.

    Returns:
        Retorna el mayor promedio de la lista.
    '''
    mayor = 0

    if len(promedios) > 0:
        mayor = promedios[0]

        for i in range(1, len(promedios)):
            if promedios[i] > mayor:
                mayor = promedios[i]

    return mayor


def obtener_indices_mayor_promedio(promedios: list) -> list:
    '''
    La función obtiene los índices de todos los estudiantes que tienen
    el mayor promedio.

    Args:
        promedios (list): Lista con los promedios de los estudiantes.

    Returns:
        Retorna una lista con los índices de los mayores promedios.
    '''
    indices_mayores = []
    mayor = obtener_mayor_promedio(promedios)

    for i in range(len(promedios)):
        if promedios[i] == mayor:
            indices_mayores += [i]

    return indices_mayores
