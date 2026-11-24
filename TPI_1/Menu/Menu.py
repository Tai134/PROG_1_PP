from Funciones.Funciones import cargar_datos
from Funciones.Funciones import cargar_hardcodeados
from Funciones.Funciones import mostrar_todos
from Funciones.Funciones import carga_promedios
from Funciones.Funciones import ordenar
from Funciones.Funciones import buscar_y_mostrar
from Funciones.Funciones import mostrar_materias_mayores
from Funciones.Funciones import pedir_materia
from Funciones.Funciones import contar_notas
from Funciones.Funciones import mostrar_frecuencias


def mostrar_menu() -> None:
    '''
    La función muestra las opciones disponibles en el menú principal.

    Returns:
        Imprime las opciones en pantalla.
    '''
    print("\n\tMENU PRINCIPAL")
    print("1 - Cargar datos")
    print("2 - Mostrar todos los datos")
    print("3 - Calcular promedios")
    print("4 - Ordenar y mostrar por promedio DESC")
    print("5 - Mostrar materia/s con mayor promedio general")
    print("6 - Buscar estudiante por legajo")
    print("7 - Contar calificaciones por materia")
    print("8 - Salir")


def opcion_cargar(cantidad: int, matriz: list, legajos: list,
                  nombres: list, generos: list, origen: str) -> bool:
    '''
    La función carga los datos por teclado o copia los datos de prueba.

    Args:
        cantidad (int): Cantidad de estudiantes que se cargan.
        matriz (list): Matriz donde se guardan las notas.
        legajos (list): Lista de legajos.
        nombres (list): Lista de nombres.
        generos (list): Lista de géneros.
        origen (str): Indica si se usa carga manual o hardcodeada.

    Returns:
        Retorna True cuando termina la carga.
    '''
    if origen == "manual":
        cargar_datos(cantidad, matriz, legajos, nombres, generos)
    else:
        cargar_hardcodeados(cantidad, matriz, legajos, nombres, generos)
    print("Los datos fueron cargados correctamente")
    return True


def opcion_mostrar(matriz: list, legajos: list, nombres: list,
                   generos: list, promedios: list, calculados: bool) -> None:
    '''
    La función muestra todos los datos de los estudiantes.

    Args:
        matriz (list): Matriz de calificaciones.
        legajos (list): Lista de legajos.
        nombres (list): Lista de nombres.
        generos (list): Lista de géneros.
        promedios (list): Lista de promedios.
        calculados (bool): Indica si ya se calcularon los promedios.

    Returns:
        Delega la presentación a mostrar_todos.
    '''
    mostrar_todos(matriz, legajos, nombres, generos, promedios, calculados)


def opcion_calcular(matriz: list, promedios: list) -> None:
    '''
    La función calcula los promedios individuales y los guarda en la lista.

    Args:
        matriz (list): Matriz con las notas de los estudiantes.
        promedios (list): Lista donde se guardan los promedios.

    Returns:
        Actualiza la lista recibida.
    '''
    carga_promedios(matriz, promedios)
    print("Los promedios fueron calculados correctamente")


def opcion_ordenar(matriz: list, legajos: list, nombres: list,
                   generos: list, promedios: list) -> None:
    '''
    La función ordena los estudiantes por promedio descendente y los muestra.

    Args:
        matriz (list): Matriz de calificaciones.
        legajos (list): Lista de legajos.
        nombres (list): Lista de nombres.
        generos (list): Lista de géneros.
        promedios (list): Lista de promedios.

    Returns:
        Reordena y muestra los datos.
    '''
    ordenar(matriz, legajos, nombres, generos, promedios, "DESC")
    mostrar_todos(matriz, legajos, nombres, generos, promedios, True)


def opcion_materias(matriz: list) -> None:
    '''
    La función muestra las materias con mayor promedio general.

    Args:
        matriz (list): Matriz de calificaciones.

    Returns:
        Muestra las materias correspondientes.
    '''
    mostrar_materias_mayores(matriz)


def opcion_buscar(matriz: list, legajos: list, nombres: list,
                  generos: list, promedios: list) -> None:
    '''
    La función busca un estudiante por legajo y muestra sus datos.

    Args:
        matriz (list): Matriz de calificaciones.
        legajos (list): Lista de legajos.
        nombres (list): Lista de nombres.
        generos (list): Lista de géneros.
        promedios (list): Lista de promedios.

    Returns:
        Muestra el estudiante encontrado.
    '''
    buscar_y_mostrar(matriz, legajos, nombres, generos, promedios)


def opcion_frecuencias(matriz: list) -> None:
    '''
    La función solicita una materia y muestra las frecuencias de sus notas.

    Args:
        matriz (list): Matriz de calificaciones.

    Returns:
        Muestra el informe de frecuencias.
    '''
    materia = pedir_materia()
    frecuencias = contar_notas(matriz, materia)
    mostrar_frecuencias(frecuencias)


def menu() -> None:
    '''
    Ejecuta el menu al completo. Cuenta con la opcion de modificar el ingreso de datos

    '''
    cantidad = 30
    origen_datos = "hardcodeado" #Hardcodeado usa los de datos prueba / manual para cargar yo
    matriz = []
    for i in range(cantidad):
        matriz += [[0] * 5]
    legajos = [0] * cantidad
    nombres = [""] * cantidad
    generos = [""] * cantidad
    promedios = [0] * cantidad
    cargados = False
    promedios_calculados = False
    salir = False

    while salir == False:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")
        match opcion:
            case "1":
                cargados = opcion_cargar(cantidad, matriz, legajos,
                                         nombres, generos, origen_datos)
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
                                opcion_mostrar(matriz, legajos, nombres,
                                               generos, promedios,
                                               promedios_calculados)
                            case "3":
                                opcion_calcular(matriz, promedios)
                                promedios_calculados = True
                            case "4":
                                match promedios_calculados:
                                    case False:
                                        opcion_calcular(matriz, promedios)
                                        promedios_calculados = True
                                opcion_ordenar(matriz, legajos, nombres,
                                               generos, promedios)
                            case "5":
                                opcion_materias(matriz)
                            case "6":
                                opcion_buscar(matriz, legajos, nombres,
                                              generos, promedios)
                            case "7":
                                opcion_frecuencias(matriz)
            case _:
                print("Opción inválida. Ingrese una opción del 1 al 8")
