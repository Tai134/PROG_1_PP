from Funciones.Funciones import carga_manual
from Funciones.Funciones import pedir_legajo
from Funciones.Funciones import pedir_nombre
from Funciones.Funciones import pedir_genero
from Funciones.Funciones import pedir_nota
from Funciones.Funciones import normalizar_estudiantes
from Funciones.Funciones import guardar_promedios
from Funciones.Funciones import mostrar_todos
from Funciones.Funciones import ordenar_estudiantes
from Funciones.Funciones import mostrar_filtrados
from Funciones.Funciones import mostrar_materias_mayores
from Funciones.Funciones import buscar_y_mostrar
from Funciones.Funciones import pedir_materia
from Funciones.Funciones import contar_notas
from Funciones.Funciones import mostrar_frecuencias
from Funciones.Funciones import cargar_csv
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
    print("3 - Normalizar nombres y géneros a mayúscula")
    print("4 - Mostrar todos los datos")
    print("5 - Calcular y guardar promedios")
    print("6 - Ordenar y mostrar por promedio")
    print("7 - Mostrar estudiantes con promedio menor a 4")
    print("8 - Mostrar materia/s con mayor promedio general")
    print("9 - Buscar estudiante por legajo")
    print("10 - Contar calificaciones por materia")
    print("11 - Guardar datos en un archivo JSON")
    print("12 - Salir")


def opcion_1_csv(estudiantes: list) -> bool:
    '''
    La función permite elegir uno de los dos CSV y carga sus registros.

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


def opcion_3_normalizar(estudiantes: list) -> list:
    '''
    La función normaliza nombres y géneros mediante el paradigma funcional.

    Args:
        estudiantes (list): Lista de diccionarios de estudiantes.

    Returns:
        Retorna la lista normalizada.
    '''
    estudiantes = normalizar_estudiantes(estudiantes)
    print("Los nombres y géneros fueron convertidos a mayúscula")
    return estudiantes


def opcion_4_mostrar(estudiantes: list) -> None:
    '''
    La función muestra todos los registros cargados.

    Args:
        estudiantes (list): Lista de diccionarios de estudiantes.

    Returns:
        Muestra todos los estudiantes en pantalla.
    '''
    mostrar_todos(estudiantes)


def opcion_5_promedios(estudiantes: list) -> list:
    '''
    La función calcula y guarda los promedios individuales.

    Args:
        estudiantes (list): Lista de diccionarios de estudiantes.

    Returns:
        Retorna la lista con la clave Promedio actualizada.
    '''
    estudiantes = guardar_promedios(estudiantes)
    print("Los promedios fueron calculados correctamente")
    return estudiantes


def opcion_6_ordenar(estudiantes: list, orden: str) -> None:
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


def opcion_7_filtrar(estudiantes: list) -> None:
    '''
    La función muestra estudiantes cuyo promedio sea menor a cuatro.

    Args:
        estudiantes (list): Lista de diccionarios con promedios calculados.

    Returns:
        Muestra los estudiantes que cumplen el criterio.
    '''
    mostrar_filtrados(estudiantes)


def opcion_8_materias(estudiantes: list) -> None:
    '''
    La función muestra las materias con el promedio general más alto.

    Args:
        estudiantes (list): Lista de diccionarios.

    Returns:
        Muestra la/s materia/s con mayor promedio.
    '''
    mostrar_materias_mayores(estudiantes)


def opcion_9_buscar(estudiantes: list) -> None:
    '''
    La función busca un estudiante por legajo y muestra sus datos.

    Args:
        estudiantes (list): Lista de diccionarios.

    Returns:
        Muestra los datos del estudiante encontrado.
    '''
    buscar_y_mostrar(estudiantes)


def opcion_10_frecuencias(estudiantes: list) -> None:
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


def opcion_11_json(estudiantes: list, archivo_json: str) -> None:
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


def opcion_12_salir() -> bool:
    '''
    La función informa que el programa va a finalizar.

    Returns:
        Retorna True para terminar el menú.
    '''
    print("Programa finalizado")
    return True


def menu() -> None:
    '''
    La función ejecuta el menú y controla la carga y el cálculo previo.

    Returns:
        Ejecuta las opciones hasta finalizar el programa.
    '''
    cantidad_manual = 10
    archivo_json = "Datos/Alumnos.json"
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
                if cargados == False:
                    estudiantes = []
                promedios_calculados = False
            case "2":
                estudiantes = []
                opcion_2_manual(cantidad_manual, estudiantes)
                cargados = True
                promedios_calculados = False
            case "12":
                salir = opcion_12_salir()
            case "3" | "4" | "5" | "6" | "7" | "8" | "9" | "10" | "11":
                match cargados:
                    case False:
                        print("Debe cargar los datos antes de elegir otra opción")
                    case True:
                        match opcion:
                            case "3":
                                estudiantes = opcion_3_normalizar(estudiantes)
                            case "4":
                                opcion_4_mostrar(estudiantes)
                            case "5":
                                estudiantes = opcion_5_promedios(estudiantes)
                                promedios_calculados = True
                            case "6":
                                match promedios_calculados:
                                    case False:
                                        print("Debe calcular los promedios primero")
                                    case True:
                                        opcion_6_ordenar(estudiantes, ordenamiento)
                            case "7":
                                match promedios_calculados:
                                    case False:
                                        print("Debe calcular los promedios primero")
                                    case True:
                                        opcion_7_filtrar(estudiantes)
                            case "8":
                                opcion_8_materias(estudiantes)
                            case "9":
                                opcion_9_buscar(estudiantes)
                            case "10":
                                opcion_10_frecuencias(estudiantes)
                            case "11":
                                opcion_11_json(estudiantes, archivo_json)
            case _:
                print("Opción inválida. Ingrese una opción del 1 al 12")


