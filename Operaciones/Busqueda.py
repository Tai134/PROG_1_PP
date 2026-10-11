def buscar_por_legajo(legajo_buscado: int, legajos: list) -> int:
    '''
    La función busca un legajo dentro de la lista de legajos.
    La búsqueda se realiza recorriendo la lista por índice.

    Args:
        legajo_buscado (int): Legajo que se desea encontrar.
        legajos (list): Lista de legajos de los estudiantes.

    Returns:
        Retorna el índice del legajo encontrado.
        Retorna -1 si el legajo no se encuentra en la lista.
    '''
    indice_buscado = -1

    for i in range(len(legajos)):
        if legajos[i] == legajo_buscado:
            indice_buscado = i
            break

    return indice_buscado
