from Carga_de_datos.Solicitud_datos import solicitar_legajo


def cargar_legajos(cantidad: int) -> list:
    '''
    La función carga los legajos de los estudiantes en una lista.
    Cada legajo es solicitado y validado antes de ser guardado.

    Args:
        cantidad (int): Cantidad de legajos que se deben cargar.

    Returns:
        Retorna una lista de legajos validados como números enteros.
    '''
    legajos = [0] * cantidad

    for i in range(len(legajos)):
        legajos[i] = solicitar_legajo()

    return legajos
