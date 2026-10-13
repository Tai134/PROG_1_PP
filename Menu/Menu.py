from Carga_de_datos.Carga_datos import cargar_datos
from Carga_de_datos.Solicitud_datos import solicitar_legajo
from Operaciones.Promedios import calcular_promedios
from Operaciones.Busqueda import buscar_por_legajo
from Ordenamientos.Ordenamiento_listas import ordenar_por_promedio
from Display.Mostrar_estudiante import mostrar_estudiantes
from Display.Mostrar_estudiante import mostrar_estudiante
from Display.Mostrar_estudiante import mostrar_mayores


def mostrar_menu() -> None:
    '''
    La función muestra en pantalla las opciones disponibles del menú.
     
    '''
    print("\n\t\t\tMENU PRINCIPAL")
    print("1 - Cargar datos")
    print("2 - Mostrar todos los datos")
    print("3 - Calcular promedios")
    print("4 - Mostrar ordenados por promedio DESC")
    print("5 - Mostrar estudiante/s con mayor promedio")
    print("6 - Buscar estudiante por legajo")
    print("7 - Salir")


def actualizar_promedios(notas_1: list, notas_2: list, promedios: list,
                         cantidad: int) -> None:
    '''
    La función calcula nuevamente los promedios de todos los estudiantes
    y copia cada resultado en la lista de promedios.

    Args:
        notas_1 (list): Lista de notas del primer parcial.
        notas_2 (list): Lista de notas del segundo parcial.
        promedios (list): Lista donde se guardan los resultados.
        cantidad (int): Cantidad de estudiantes.
    '''
    promedios_nuevos = calcular_promedios(notas_1, notas_2)
    for i in range(cantidad):
        promedios[i] = promedios_nuevos[i]
    print("Los promedios fueron calculados correctamente")


def solicitar_orden() -> str:
    '''
    La función solicita el tipo de ordenamiento.
    Acepta ASC, DESC o Enter para utilizar DESC por defecto.

    Returns:
        Retorna el orden validado como un str.
    '''
    orden = ""
    validacion = False
    while validacion == False:
        orden = input("Ingrese ASC o DESC. Presione Enter para usar DESC: ")
        match orden:
            case "" | "ASC" | "DESC":
                validacion = True
            case _:
                print("Orden inválido. Ingrese ASC o DESC")
    match orden:
        case "":
            orden = "DESC"
    return orden


def mostrar_ordenados(promedios: list, legajos: list, nombres: list,
                      generos: list, notas_1: list, notas_2: list) -> None:
    '''
    La función solicita el orden, ordena las listas paralelas según el
    promedio y muestra todos los estudiantes ordenados.

    Args:
        Recibe las listas paralelas de los estudiantes.
    '''
    orden = solicitar_orden()
    ordenar_por_promedio(promedios, legajos, nombres, generos, notas_1,
                         notas_2, orden)
    mostrar_estudiantes(legajos, nombres, generos, notas_1, notas_2,
                        promedios)


def buscar_estudiante(legajos: list, nombres: list, generos: list,
                      notas_1: list, notas_2: list, promedios: list) -> None:
    '''
    La función solicita un legajo y busca el estudiante correspondiente.
    Si el legajo no existe, lo vuelve a solicitar hasta encontrarlo.

    Args:
        Recibe las listas paralelas de los estudiantes.
    '''
    indice = -1
    while indice == -1:
        legajo_buscado = solicitar_legajo()
        indice = buscar_por_legajo(legajo_buscado, legajos)
        match indice:
            case -1:
                print("No se encontró un estudiante con ese legajo")
                print("Ingrese nuevamente un legajo válido")
    print("\nLEGAJO\tAPELLIDO Y NOMBRE\tGENERO\tNOTA 1\tNOTA 2\tPROMEDIO")
    mostrar_estudiante(indice, legajos, nombres, generos, notas_1, notas_2,
                       promedios)


def menu() -> None:
    '''
    La función controla el menú principal y coordina las operaciones del
    programa. Inicializa las listas, controla que los datos estén cargados
    y llama a la función correspondiente según la opción elegida.
    '''
    cantidad = 30
    cargados = False
    salir = False
    legajos = [0] * cantidad
    nombres = [""] * cantidad
    generos = [""] * cantidad
    notas_1 = [0] * cantidad
    notas_2 = [0] * cantidad
    promedios = [0] * cantidad

    while salir == False:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")
        match opcion:
            case "1":
                cargar_datos(cantidad, legajos, nombres, generos, notas_1,
                             notas_2, promedios)
                cargados = True
                print("Los datos fueron cargados correctamente")
            case "7":
                salir = True
                print("Programa finalizado")
            case "2" | "3" | "4" | "5" | "6":
                match cargados:
                    case False:
                        print("Debe cargar los datos antes de elegir otra opción")
                    case True:
                        match opcion:
                            case "2":
                                mostrar_estudiantes(
                                    legajos, nombres, generos,
                                    notas_1, notas_2, promedios)
                            case "3":
                                actualizar_promedios(
                                    notas_1, notas_2, promedios, cantidad)
                            case "4":
                                mostrar_ordenados(
                                    promedios, legajos, nombres, generos,
                                    notas_1, notas_2)
                            case "5":
                                mostrar_mayores(
                                    legajos, nombres, generos,
                                    notas_1, notas_2, promedios)
                            case "6":
                                buscar_estudiante(
                                    legajos, nombres, generos,
                                    notas_1, notas_2, promedios)
            case _:
                print("Opción inválida. Ingrese una opción del 1 al 7")
