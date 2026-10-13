def ordenar_por_promedio(promedios: list, legajos: list, nombres: list,
                         generos: list, notas_1: list, notas_2: list,
                         orden: str) -> None:
    '''
    La función ordena las listas paralelas según el promedio de cada
    estudiante utilizando el método de ordenamiento burbuja.
    El orden puede ser ascendente o descendente según el parámetro recibido.

    Args:
        promedios (list): Lista de promedios de los estudiantes.
        legajos (list): Lista de legajos de los estudiantes.
        nombres (list): Lista de apellidos y nombres.
        generos (list): Lista de géneros de los estudiantes.
        notas_1 (list): Lista de notas del primer parcial.
        notas_2 (list): Lista de notas del segundo parcial.
        orden (str): Tipo de ordenamiento, ASC o DESC.

    Returns:
        No retorna un valor. Modifica las listas paralelas recibidas.
    '''
    cantidad = len(promedios)

    for i in range(cantidad - 1):
        for j in range(cantidad - i - 1):
            intercambiar = False

            if orden == "ASC" and promedios[j] > promedios[j + 1]:
                intercambiar = True
            elif orden == "DESC" and promedios[j] < promedios[j + 1]:
                intercambiar = True

            if intercambiar == True:
                aux = promedios[j]
                promedios[j] = promedios[j + 1]
                promedios[j + 1] = aux

                aux = legajos[j]
                legajos[j] = legajos[j + 1]
                legajos[j + 1] = aux

                aux = nombres[j]
                nombres[j] = nombres[j + 1]
                nombres[j + 1] = aux

                aux = generos[j]
                generos[j] = generos[j + 1]
                generos[j + 1] = aux

                aux = notas_1[j]
                notas_1[j] = notas_1[j + 1]
                notas_1[j + 1] = aux

                aux = notas_2[j]
                notas_2[j] = notas_2[j + 1]
                notas_2[j + 1] = aux

