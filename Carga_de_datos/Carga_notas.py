from Carga_de_datos.Solicitud_datos import solicitar_nota


def cargar_notas(cantidad: int) -> list:
    '''
    La función carga las notas de los estudiantes en una lista.
    Cada nota es solicitada y validada antes de ser guardada.
    Carga solo 1 nota -> se debe llamar la cantidad de veces necesarias
    por la cantidad de parciales.

    Args:
        cantidad (int): Cantidad de notas que se deben cargar.

    Returns:
        Retorna una lista de notas validadas como números enteros.
    '''
    notas = [0] * cantidad

    for i in range(len(notas)):
        notas[i] = solicitar_nota()

    return notas
