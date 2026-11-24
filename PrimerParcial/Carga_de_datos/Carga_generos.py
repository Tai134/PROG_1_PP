from Carga_de_datos.Solicitud_datos import solicitar_genero


def cargar_generos(cantidad: int) -> list:
    '''
    La función carga los géneros de los estudiantes en una lista.
    Cada género es solicitado y validado antes de ser guardado.

    Args:
        cantidad (int): Cantidad de géneros que se deben cargar.

    Returns:
        Retorna una lista de géneros validados.
    '''
    generos = [""] * cantidad

    for i in range(len(generos)):
        generos[i] = solicitar_genero()

    return generos
