def calcular_promedio(nota_1: int, nota_2: int) -> float:
    '''
    La función calcula el promedio de las dos notas de un estudiante.

    Args:
        nota_1 (int): Nota del primer parcial.
        nota_2 (int): Nota del segundo parcial.

    Returns:
        Retorna el promedio de las dos notas como un número real.
    '''
    promedio = round((nota_1 + nota_2) / 2, 2)
    return promedio


def calcular_promedios(notas_1: list, notas_2: list) -> list:
    '''
    La función calcula los promedios de todos los estudiantes.
    Las notas se recorren utilizando el mismo índice porque son listas
    paralelas.

    Args:
        notas_1 (list): Lista de notas del primer parcial.
        notas_2 (list): Lista de notas del segundo parcial.

    Returns:
        Retorna una lista con el promedio de cada estudiante.
    '''
    promedios = [0] * len(notas_1)

    for i in range(len(promedios)):
        promedios[i] = calcular_promedio(notas_1[i], notas_2[i])

    return promedios
