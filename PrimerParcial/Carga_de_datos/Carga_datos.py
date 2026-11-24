from Carga_de_datos.Solicitud_datos import solicitar_legajo
from Carga_de_datos.Solicitud_datos import solicitar_nombre
from Carga_de_datos.Solicitud_datos import solicitar_genero
from Carga_de_datos.Solicitud_datos import solicitar_nota
from Operaciones.Promedios import calcular_promedio
from Validaciones.Validaciones_Texto import validar_legajo_repetido


def cargar_datos(cantidad: int, legajos: list, nombres: list,
                 generos: list, notas_1: list, notas_2: list,
                 promedios: list) -> None:
    '''
    La función carga todos los datos de los estudiantes y completa las
    listas paralelas recibidas por parámetro.

    Args:
        cantidad (int): Cantidad de estudiantes que se deben cargar.
        legajos (list): Lista donde se guardan los legajos.
        nombres (list): Lista donde se guardan los apellidos y nombres.
        generos (list): Lista donde se guardan los géneros.
        notas_1 (list): Lista donde se guardan las notas del primer parcial.
        notas_2 (list): Lista donde se guardan las notas del segundo parcial.
        promedios (list): Lista donde se guardan los promedios.
    '''
    for i in range(cantidad):
        print(f"\nDATOS DEL ESTUDIANTE {i + 1}")

        validacion = False

        while validacion == False:
            legajo = solicitar_legajo()
            validacion = validar_legajo_repetido(legajo, legajos, i)

            if validacion == False:
                print("El legajo ya fue ingresado. Ingrese otro")

        legajos[i] = legajo
        nombres[i] = solicitar_nombre()
        generos[i] = solicitar_genero()
        notas_1[i] = solicitar_nota(1)
        notas_2[i] = solicitar_nota(2)
        promedios[i] = calcular_promedio(notas_1[i], notas_2[i])
