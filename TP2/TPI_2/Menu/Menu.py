from Funciones.Funciones import carga_manual
from Funciones.Funciones import carga_hardcodeada
from Funciones.Funciones import mostrar_todos
from Funciones.Funciones import guardar_promedios
from Funciones.Funciones import ordenar_estudiantes
from Funciones.Funciones import buscar_y_mostrar
from Funciones.Funciones import mostrar_materias_mayores
from Funciones.Funciones import pedir_materia
from Funciones.Funciones import contar_notas
from Funciones.Funciones import mostrar_frecuencias
from Funciones import hardco_10
from Funciones import hardco_prueba


def mostrar_menu() -> None:
    '''
    La función muestra las opciones disponibles en el menú.

    Returns:
        Imprime las opciones para el usuario.
    '''
    print("\n\tMENU PRINCIPAL")
    print("1 - Cargar datos")
    print("2 - Mostrar todos los datos")
    print("3 - Calcular promedios")
    print("4 - Ordenar y mostrar por promedio")
    print("5 - Mostrar materia/s con mayor promedio general")
    print("6 - Buscar estudiante por legajo")
    print("7 - Contar calificaciones por materia")
    print("8 - Salir")


def opcion_cargar(cantidad: int, estudiantes: list, origen: str,
                  datos_prueba: list) -> bool:
    '''
    La función realiza la carga manual o hardcodeada según el selector.

    Args:
        cantidad (int): Cantidad de estudiantes.
        estudiantes (list): Lista de diccionarios que recibe los datos.
        origen (str): Modo seleccionado para cargar datos.
        datos_prueba (list): Registros del archivo de prueba elegido.

    Returns:
        Retorna True cuando los datos quedan cargados.
    '''
    if origen == "manual":
        carga_manual(cantidad, estudiantes)
    else:
        carga_hardcodeada(cantidad, estudiantes, datos_prueba)
    print("Los datos fueron cargados correctamente")
    return True


def opcion_mostrar(estudiantes: list, promedios_calculados: bool) -> None:
    '''
    La función muestra todos los estudiantes e indica si se imprimen promedios.

    Args:
        estudiantes (list): Lista de diccionarios.
        promedios_calculados (bool): Estado del cálculo de promedios.

    Returns:
        Muestra los datos de todos los estudiantes.
    '''
    mostrar_todos(estudiantes, promedios_calculados)


def opcion_calcular(estudiantes: list) -> None:
    '''
    La función calcula los promedios individuales.

    Args:
        estudiantes (list): Lista de diccionarios de estudiantes.

    Returns:
        Actualiza la clave Promedio en cada diccionario.
    '''
    guardar_promedios(estudiantes)
    print("Los promedios fueron calculados correctamente")


def opcion_ordenar(estudiantes: list, orden: str) -> None:
    '''
    La función ordena y muestra los registros según el orden indicado.

    Args:
        estudiantes (list): Lista de diccionarios.
        orden (str): Orden solicitado, ASC o DESC.

    Returns:
        Reordena y muestra la lista.
    '''
    ordenar_estudiantes(estudiantes, orden)
    mostrar_todos(estudiantes, True)


def opcion_materias(estudiantes: list) -> None:
    '''
    La función muestra las materias con mayor promedio general.

    Args:
        estudiantes (list): Lista de diccionarios de estudiantes.

    Returns:
        Muestra las materias con promedio máximo.
    '''
    mostrar_materias_mayores(estudiantes)


def opcion_buscar(estudiantes: list, promedios_calculados: bool) -> None:
    '''
    La función busca un estudiante por legajo y muestra sus datos.

    Args:
        estudiantes (list): Lista de diccionarios.
        promedios_calculados (bool): Indica si el promedio se incluye.

    Returns:
        Muestra el estudiante encontrado.
    '''
    buscar_y_mostrar(estudiantes, promedios_calculados)


def opcion_frecuencias(estudiantes: list) -> None:
    '''
    La función solicita una materia y presenta la frecuencia de sus notas.

    Args:
        estudiantes (list): Lista de diccionarios.

    Returns:
        Muestra el informe de frecuencias.
    '''
    materia = pedir_materia()
    frecuencias = contar_notas(estudiantes, materia)
    mostrar_frecuencias(frecuencias)


def menu() -> None:
    '''
    La función controla el menú con while y match/case y bloquea las
    consultas hasta completar la carga.

    Returns:
        Ejecuta las opciones elegidas por el usuario.
    '''
    origen_datos = "hardco_10"
    cantidad_manual = 10
    orden_punto_4 = "DESC"
    estudiantes = []
    cargados = False
    promedios_calculados = False
    salir = False

    while salir == False:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")
        match opcion:
            case "1":
                if origen_datos == "manual":
                    origen = "manual"
                    cantidad = cantidad_manual
                    datos_prueba = []
                elif origen_datos == "hardco_10":
                    origen = "hardcodeado"
                    datos_prueba = hardco_10.estudiantes
                    cantidad = len(datos_prueba)
                else:
                    origen = "hardcodeado"
                    datos_prueba = hardco_prueba.estudiantes
                    cantidad = len(datos_prueba)
                estudiantes = []
                for i in range(cantidad):
                    estudiante = {"Legajo": 0, "Nombre": "", "Genero": "",
                                  "Notas": [0] * 5, "Promedio": 0}
                    estudiantes += [estudiante]
                cargados = opcion_cargar(cantidad, estudiantes, origen,
                                         datos_prueba)
                promedios_calculados = False
            case "8":
                salir = True
                print("Programa finalizado")
            case "2" | "3" | "4" | "5" | "6" | "7":
                match cargados:
                    case False:
                        print("Debe cargar los datos antes de elegir otra opción")
                    case True:
                        match opcion:
                            case "2":
                                opcion_mostrar(estudiantes,
                                               promedios_calculados)
                            case "3":
                                opcion_calcular(estudiantes)
                                promedios_calculados = True
                            case "4":
                                match promedios_calculados:
                                    case False:
                                        print("Debe calcular los promedios primero")
                                    case True:
                                        opcion_ordenar(estudiantes,
                                                       orden_punto_4)
                            case "5":
                                opcion_materias(estudiantes)
                            case "6":
                                opcion_buscar(estudiantes,
                                              promedios_calculados)
                            case "7":
                                opcion_frecuencias(estudiantes)
            case _:
                print("Opción inválida. Ingrese una opción del 1 al 8")
