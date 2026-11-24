from Carga_de_datos.Solicitud_datos import solicitar_nombre


def cargar_nombres(cantidad: int) -> list:
    '''
    La función carga los apellidos y nombres de los estudiantes.
    Cada dato es solicitado y validado antes de ser guardado.

    Args:
        cantidad (int): Cantidad de nombres que se deben cargar.

    Returns:
        Retorna una lista de apellidos y nombres validados.
    '''
    nombres = [""] * cantidad

    for i in range(len(nombres)):
        nombres[i] = solicitar_nombre()

    return nombres
