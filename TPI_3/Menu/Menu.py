from Funciones.Funciones import cargar_csv
from Funciones.Funciones import carga_manual
from Funciones.Funciones import mostrar_todos
from Funciones.Funciones import guardar_promedios
from Funciones.Funciones import ordenar_estudiantes
from Funciones.Funciones import mostrar_materias_mayores
from Funciones.Funciones import buscar_y_mostrar
from Funciones.Funciones import pedir_materia
from Funciones.Funciones import contar_notas
from Funciones.Funciones import mostrar_frecuencias
from Funciones.Funciones import guardar_json


def mostrar_menu() -> None:
    '''
    La función muestra las opciones disponibles en el menú principal.

    Returns:
        Imprime las opciones en pantalla.
    '''
    print("\n\tMENU PRINCIPAL")
    print("1 - Cargar datos desde un archivo CSV")
    print("2 - Cargar datos manualmente")
    print("3 - Mostrar todos los datos")
    print("4 - Calcular y guardar promedios")
    print("5 - Ordenar y mostrar por promedio")
    print("6 - Mostrar materia/s con mayor promedio general")
    print("7 - Buscar estudiante por legajo")
    print("8 - Contar calificaciones por materia")
    print("9 - Guardar datos en un archivo JSON")
    print("10 - Salir")


def opcion_1_csv(estudiantes: list) -> bool:
    '''
    La función solicita una ubicación CSV y carga los registros validados.

    Args:
        estudiantes (list): Lista donde se guardan los estudiantes.
    Returns:
        Retorna True si la carga terminó correctamente.
    '''
    print("Seleccione el archivo CSV que desea cargar")
    print("1 - Alumnos_10.csv")
    print("2 - Alumnos_1000.csv")
    seleccion = input("Ingrese una opción: ")
    while seleccion != "1" and seleccion != "2":
        print("Opción inválida. Elija 1 o 2")
        seleccion = input("Ingrese una opción: ")
    if seleccion == "1":
        ruta = "Datos/Alumnos_10.csv"
    else:
        ruta = "Datos/Alumnos_1000.csv"
    cargado = cargar_csv(ruta, estudiantes)
    if cargado == True:
        print("Los datos del CSV fueron cargados correctamente")
    return cargado


def opcion_2_manual(cantidad: int, estudiantes: list) -> None:
    '''
    La función solicita manualmente los datos de los estudiantes.

    Args:
        cantidad (int): Cantidad de estudiantes que se van a cargar.
        estudiantes (list): Lista donde se guardan los estudiantes.

    Returns:
        Completa la lista con los datos ingresados y validados.
    '''
    carga_manual(cantidad, estudiantes)
    print("Los datos fueron cargados correctamente")


def opcion_3_mostrar(estudiantes: list) -> None:
    '''
    La función muestra todos los estudiantes cargados.

    Args:
        estudiantes (list): Lista de diccionarios.

    Returns:
        Muestra todos los estudiantes en pantalla.
    '''
    mostrar_todos(estudiantes)


def opcion_4_promedios(estudiantes: list) -> None:
    '''
    La función calcula y guarda los promedios individuales.

    Args:
        estudiantes (list): Lista de diccionarios.

    Returns:
        Actualiza la clave Promedio de cada estudiante.
    '''
    guardar_promedios(estudiantes)
    print("Los promedios fueron calculados correctamente")


def opcion_5_ordenar(estudiantes: list, orden: str) -> None:
    '''
    La función ordena por promedio y muestra los registros.

    Args:
        estudiantes (list): Lista de diccionarios.
        orden (str): Orden solicitado, ASC o DESC.

    Returns:
        Reordena y muestra los estudiantes.
    '''
    ordenar_estudiantes(estudiantes, orden)
    mostrar_todos(estudiantes)


def opcion_6_materias(estudiantes: list) -> None:
    '''
    La función muestra las materias con el promedio general más alto.

    Args:
        estudiantes (list): Lista de diccionarios.

    Returns:
        Muestra la/s materia/s con mayor promedio.
    '''
    mostrar_materias_mayores(estudiantes)


def opcion_7_buscar(estudiantes: list) -> None:
    '''
    La función busca un estudiante por legajo y muestra todos sus datos.

    Args:
        estudiantes (list): Lista de diccionarios.

    Returns:
        Muestra los datos del estudiante encontrado.
    '''
    buscar_y_mostrar(estudiantes)


def opcion_8_frecuencias(estudiantes: list) -> None:
    '''
    La función solicita una materia y muestra las frecuencias de sus notas.

    Args:
        estudiantes (list): Lista de diccionarios.

    Returns:
        Muestra el informe de frecuencias.
    '''
    materia = pedir_materia()
    frecuencias = contar_notas(estudiantes, materia)
    mostrar_frecuencias(frecuencias)


def opcion_9_json(estudiantes: list, archivo_json: str) -> None:
    '''
    La función guarda los datos cargados en el archivo JSON configurado.

    Args:
        estudiantes (list): Lista de diccionarios que se va a guardar.
        archivo_json (str): Nombre o ubicación del archivo JSON.

    Returns:
        Guarda los estudiantes en formato JSON.
    '''
    guardado = guardar_json(estudiantes, archivo_json)
    if guardado == True:
        print("Los datos se guardaron correctamente en el archivo JSON")


def opcion_10_salir() -> bool:
    '''
    La función informa que el programa va a finalizar.

    Returns:
        Retorna True para terminar el menú.
    '''
    print("Programa finalizado")
    return True


def menu() -> None:
    '''
    La función ejecuta el menú dentro de un ciclo y controla la carga previa.

    Returns:
        Ejecuta la opción seleccionada hasta salir del programa.
    '''
    archivo_json = "Datos/Alumnos.json"
    cantidad_manual = 1000
    ordenamiento = "DESC"
    estudiantes = []
    cargados = False
    promedios_calculados = False
    salir = False

    while salir == False:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")
        match opcion:
            case "1":
                estudiantes = []
                cargados = opcion_1_csv(estudiantes)
                promedios_calculados = False
            case "2":
                estudiantes = []
                opcion_2_manual(cantidad_manual, estudiantes)
                cargados = True
                promedios_calculados = False
            case "10":
                salir = opcion_10_salir()
            case "3" | "4" | "5" | "6" | "7" | "8" | "9":
                match cargados:
                    case False:
                        print("Debe cargar los datos antes de elegir otra opción")
                    case True:
                        match opcion:
                            case "3":
                                opcion_3_mostrar(estudiantes)
                            case "4":
                                opcion_4_promedios(estudiantes)
                                promedios_calculados = True
                            case "5":
                                match promedios_calculados:
                                    case False:
                                        print("Debe calcular los promedios primero")
                                    case True:
                                        opcion_5_ordenar(estudiantes,
                                                        ordenamiento)
                            case "6":
                                opcion_6_materias(estudiantes)
                            case "7":
                                opcion_7_buscar(estudiantes)
                            case "8":
                                opcion_8_frecuencias(estudiantes)
                            case "9":
                                opcion_9_json(estudiantes, archivo_json)
            case _:
                print("Opción inválida. Ingrese una opción del 1 al 10")
