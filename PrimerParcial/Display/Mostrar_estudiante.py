from Operaciones.Maximos import obtener_indices_mayor_promedio


def mostrar_estudiante(indice: int, legajos: list, nombres: list,
                       generos: list, notas_1: list, notas_2: list,
                       promedios: list) -> None:
    '''
    La función muestra los datos de un estudiante utilizando el índice
    correspondiente en cada una de las listas paralelas.

    Args:
        indice (int): Índice del estudiante que se desea mostrar.
        legajos (list): Lista de legajos de los estudiantes.
        nombres (list): Lista de apellidos y nombres.
        generos (list): Lista de géneros de los estudiantes.
        notas_1 (list): Lista de notas del primer parcial.
        notas_2 (list): Lista de notas del segundo parcial.
        promedios (list): Lista de promedios de los estudiantes.
    '''
    print(f"{legajos[indice]}\t{nombres[indice]}\t\t"
          f"{generos[indice]}\t{notas_1[indice]}\t"
          f"{notas_2[indice]}\t{promedios[indice]:.2f}")


def mostrar_estudiantes(legajos: list, nombres: list, generos: list,
                        notas_1: list, notas_2: list,
                        promedios: list) -> None:
    '''
    La función recorre las listas paralelas y muestra los datos de todos
    los estudiantes. Para mostrar cada registro llama a la función
    mostrar_estudiante().

    Args:
        legajos (list): Lista de legajos de los estudiantes.
        nombres (list): Lista de apellidos y nombres.
        generos (list): Lista de géneros de los estudiantes.
        notas_1 (list): Lista de notas del primer parcial.
        notas_2 (list): Lista de notas del segundo parcial.
        promedios (list): Lista de promedios de los estudiantes.
    '''
    print("\n\t\t\tLISTADO DE ESTUDIANTES")
    print("LEGAJO\tAPELLIDO Y NOMBRE\tGENERO\t"
          "NOTA 1\tNOTA 2\tPROMEDIO")

    for i in range(len(legajos)):
        mostrar_estudiante(i, legajos, nombres, generos, notas_1, notas_2,
                           promedios)


def mostrar_mayores(legajos: list, nombres: list, generos: list,
                    notas_1: list, notas_2: list,
                    promedios: list) -> None:
    '''
    La función obtiene los estudiantes con mayor promedio y muestra sus
    datos utilizando la función que muestra un estudiante.
    '''
    indices_mayores = obtener_indices_mayor_promedio(promedios)

    print("\n\t\t\tESTUDIANTE/S CON MAYOR PROMEDIO")
    print("LEGAJO\tAPELLIDO Y NOMBRE\tGENERO\t"
          "NOTA 1\tNOTA 2\tPROMEDIO")

    for i in indices_mayores:
        mostrar_estudiante(i, legajos, nombres, generos, notas_1,
                           notas_2, promedios)
