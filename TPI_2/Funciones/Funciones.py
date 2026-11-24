from Validaciones.Validaciones import validar_legajo
from Validaciones.Validaciones import validar_legajo_unico
from Validaciones.Validaciones import validar_nombre
from Validaciones.Validaciones import validar_genero
from Validaciones.Validaciones import validar_nota
from Validaciones.Validaciones import validar_materia


#Cargas - corroborra cargas 

def pedir_legajo(estudiantes: list, cantidad_cargada: int) -> int:
    '''
    La función solicita un legajo válido y único.

    Args:
        estudiantes (list): Lista con los estudiantes ya cargados.
        cantidad_cargada (int): Cantidad de estudiantes ya ingresados.

    Returns:
        Retorna el legajo aceptado como entero.
    '''
    validacion = False
    legajo = 0
    while validacion == False:
        texto = input("Ingrese legajo de cinco cifras: ")
        validacion = validar_legajo(texto)
        if validacion == True:
            legajo = int(texto)
            validacion = validar_legajo_unico(legajo, estudiantes,
                                               cantidad_cargada)
            if validacion == False:
                print("El legajo ya fue ingresado")
        else:
            print("El legajo debe tener cinco cifras")
    return legajo


def pedir_nombre() -> str:
    '''
    La función solicita un nombre hasta que la validación lo acepte.

    Returns:
        Retorna el nombre ingresado como texto.
    '''
    validacion = False
    nombre = ""
    while validacion == False:
        nombre = input("Ingrese apellido y nombre: ")
        validacion = validar_nombre(nombre)
        if validacion == False:
            print("Nombre inválido")
    return nombre


def pedir_genero() -> str:
    '''
    La función solicita un género válido y lo deja en mayúscula.

    Returns:
        Retorna F, M o X como texto.
    '''
    validacion = False
    genero = ""
    while validacion == False:
        genero = input("Ingrese género (F-M-X): ")
        validacion = validar_genero(genero)
        if validacion == False:
            print("Género inválido")
    codigo = ord(genero[0])
    if codigo >= 97 and codigo <= 122:
        genero = chr(codigo - 32)
    return genero


def pedir_nota(materia: int) -> int:
    '''
    La función solicita una nota válida para la materia indicada.

    Args:
        materia (int): Número de materia que se está cargando.

    Returns:
        Retorna la nota validada como entero.
    '''
    validacion = False
    nota = 0
    while validacion == False:
        texto = input(f"Ingrese nota de MAT_{materia} (1-10): ")
        validacion = validar_nota(texto)
        if validacion == True:
            nota = int(texto)
        else:
            print("La nota debe ser un entero entre 1 y 10")
    return nota


def pedir_materia() -> int:
    '''
    La función solicita el número de materia entre 1 y 5.

    Returns:
        Retorna el número de materia validado como entero.
    '''
    validacion = False
    materia = 0
    while validacion == False:
        texto = input("Ingrese número de materia (1-5): ")
        validacion = validar_materia(texto)
        if validacion == True:
            materia = int(texto)
        else:
            print("Materia inválida")
    return materia


def carga_manual(cantidad: int, estudiantes: list) -> None:
    '''
    La función pide los datos de cada alumno y los guarda en un diccionario.

    Args:
        cantidad (int): Cantidad de estudiantes a cargar.
        estudiantes (list): Lista donde se guardan los diccionarios.

    Returns:
        Completa la lista recibida con los estudiantes ingresados.
    '''
    for i in range(cantidad):
        print(f"\nDATOS DEL ESTUDIANTE {i + 1}")
        estudiante = {"Legajo": 0, "Nombre": "", "Genero": "",
                      "Notas": [0] * 5, "Promedio": 0}
        estudiante["Legajo"] = pedir_legajo(estudiantes, i)
        estudiante["Nombre"] = pedir_nombre()
        estudiante["Genero"] = pedir_genero()
        for j in range(5):
            estudiante["Notas"][j] = pedir_nota(j + 1)
        estudiantes[i] = estudiante


def carga_hardcodeada(cantidad: int, estudiantes: list,
                      datos_prueba: list) -> None:
    '''
    La función copia registros de prueba a la lista activa del programa.

    Args:
        cantidad (int): Cantidad de estudiantes a copiar.
        estudiantes (list): Lista donde se guardan los diccionarios.
        datos_prueba (list): Lista con los registros de prueba seleccionados.

    Returns:
        Completa la lista recibida con los datos hardcodeados.
    '''
    for i in range(cantidad):
        notas = [0] * 5
        for j in range(5):
            notas[j] = datos_prueba[i]["Notas"][j]
        estudiante = {"Legajo": datos_prueba[i]["Legajo"],
                      "Nombre": datos_prueba[i]["Nombre"],
                      "Genero": datos_prueba[i]["Genero"],
                      "Notas": notas, "Promedio": 0}
        estudiantes[i] = estudiante

#Calculos - revisar promedis

def redondeo(valor: float) -> float:
    '''
    La función redondea manualmente un valor a dos decimales.

    Args:
        valor (float): Número que se desea redondear.

    Returns:
        Retorna el valor redondeado a dos decimales.
    '''
    centesimas = int(valor * 100)
    resto = valor * 100 - centesimas
    if resto >= 0.5:
        centesimas += 1
    return centesimas / 100


def calcular_promedio(estudiante: dict) -> float:
    '''
    La función calcula el promedio de las cinco notas de un estudiante.

    Args:
        estudiante (dict): Diccionario con los datos del estudiante.

    Returns:
        Retorna el promedio redondeado a dos decimales.
    '''
    suma = 0
    for i in range(len(estudiante["Notas"])):
        suma += estudiante["Notas"][i]
    promedio = suma / len(estudiante["Notas"])
    return redondeo(promedio)


def guardar_promedios(estudiantes: list) -> None:
    '''
    La función calcula los promedios y los guarda en cada diccionario.

    Args:
        estudiantes (list): Lista de diccionarios de estudiantes.

    Returns:
        Actualiza la clave Promedio de cada estudiante.
    '''
    for i in range(len(estudiantes)):
        estudiantes[i]["Promedio"] = calcular_promedio(estudiantes[i])


def mostrar_uno(i: int, estudiantes: list,
                mostrar_promedio: bool = True) -> None:
    '''
    La función imprime un estudiante usando su posición en la lista.

    Args:
        i (int): Posición del estudiante.
        estudiantes (list): Lista de diccionarios.
        mostrar_promedio (bool): Indica si se muestra el promedio.

    Returns:
        Muestra los datos de un estudiante en pantalla.
    '''
    estudiante = estudiantes[i]
    print(f"{estudiante['Legajo']}\t{estudiante['Nombre']}\t"
          f"{estudiante['Genero']}\t", end="")
    for j in range(len(estudiante["Notas"])):
        print(f"{estudiante['Notas'][j]}\t", end="")
    if mostrar_promedio == True:
        print(f"{estudiante['Promedio']:.2f}")
    else:
        print("\n", end="")


def mostrar_todos(estudiantes: list, mostrar_promedio: bool = True) -> None:
    '''
    La función recorre la lista y llama a mostrar_uno para cada alumno.

    Args:
        estudiantes (list): Lista de diccionarios de estudiantes.
        mostrar_promedio (bool): Indica si se imprime la columna promedio.

    Returns:
        Muestra todos los estudiantes en pantalla.
    '''
    print("\nLEGAJO\tNOMBRE\tGENERO\tN1\tN2\tN3\tN4\tN5", end="")
    if mostrar_promedio == True:
        print("\tPROM.")
    else:
        print("\n", end="")
    for i in range(len(estudiantes)):
        mostrar_uno(i, estudiantes, mostrar_promedio)


def ordenar_estudiantes(estudiantes: list, orden: str) -> None:
    '''
    La función ordena la lista por promedio usando bubble sort.

    Args:
        estudiantes (list): Lista de diccionarios que se va a ordenar.
        orden (str): Orden solicitado, ASC o DESC.

    Returns:
        Reordena la lista de acuerdo con el promedio.
    '''
    cantidad = len(estudiantes)
    for i in range(cantidad - 1):
        for j in range(cantidad - i - 1):
            intercambiar = False
            if orden == "ASC" and estudiantes[j]["Promedio"] > \
                    estudiantes[j + 1]["Promedio"]:
                intercambiar = True
            elif orden == "DESC" and estudiantes[j]["Promedio"] < \
                    estudiantes[j + 1]["Promedio"]:
                intercambiar = True
            if intercambiar == True:
                auxiliar = estudiantes[j]
                estudiantes[j] = estudiantes[j + 1]
                estudiantes[j + 1] = auxiliar


def buscar_indice(legajo: int, estudiantes: list) -> int:
    '''
    La función busca un legajo y devuelve la posición del estudiante.

    Args:
        legajo (int): Legajo que se desea encontrar.
        estudiantes (list): Lista de diccionarios.

    Returns:
        Retorna el índice encontrado o -1 si no existe.
    '''
    i = 0
    while i < len(estudiantes) and estudiantes[i]["Legajo"] != legajo:
        i += 1
    if i == len(estudiantes):
        i = -1
    return i


def buscar_y_mostrar(estudiantes: list, mostrar_promedio: bool) -> None:
    '''
    La función busca por legajo y muestra los datos encontrados.

    Args:
        estudiantes (list): Lista de diccionarios.
        mostrar_promedio (bool): Indica si se muestra el promedio.

    Returns:
        Muestra el registro encontrado.
    '''
    i = -1
    while i == -1:
        texto = input("Ingrese legajo a buscar: ")
        if validar_legajo(texto) == True:
            i = buscar_indice(int(texto), estudiantes)
        if i == -1:
            print("No se encontró el legajo; intente nuevamente")
    print("LEGAJO\tNOMBRE\tGENERO\tN1\tN2\tN3\tN4\tN5", end="")
    if mostrar_promedio == True:
        print("\tPROM.")
    else:
        print("\n", end="")
    mostrar_uno(i, estudiantes, mostrar_promedio)


def promedios_materias(estudiantes: list) -> list:
    '''
    La función calcula el promedio general de cada una de las cinco materias.

    Args:
        estudiantes (list): Lista de diccionarios con las calificaciones.

    Returns:
        Retorna una lista con el promedio general por materia.
    '''
    promedios = [0] * 5
    for j in range(5):
        suma = 0
        for i in range(len(estudiantes)):
            suma += estudiantes[i]["Notas"][j]
        promedios[j] = redondeo(suma / len(estudiantes))
    return promedios


def mostrar_materia(i: int, promedios: list) -> None:
    '''
    La función muestra el nombre y promedio general de una materia.

    Args:
        i (int): Posición de la materia.
        promedios (list): Promedios generales de las materias.

    Returns:
        Muestra una materia en pantalla.
    '''
    print(f"MAT_{i + 1}\t{promedios[i]:.2f}")


def mostrar_materias_mayores(estudiantes: list) -> None:
    '''
    La función muestra todas las materias empatadas en el promedio máximo.

    Args:
        estudiantes (list): Lista de diccionarios con las notas.

    Returns:
        Muestra las materias con mayor promedio general.
    '''
    promedios = promedios_materias(estudiantes)
    mayor = promedios[0]
    for i in range(1, len(promedios)):
        if promedios[i] > mayor:
            mayor = promedios[i]
    print("\nMATERIA/S CON MAYOR PROMEDIO GENERAL")
    print("MATERIA\tPROMEDIO")
    for i in range(len(promedios)):
        if promedios[i] == mayor:
            mostrar_materia(i, promedios)


def contar_notas(estudiantes: list, numero_materia: int) -> list:
    '''
    La función cuenta las repeticiones de las notas en una materia elegida.

    Args:
        estudiantes (list): Lista de diccionarios de estudiantes.
        numero_materia (int): Número de materia, del 1 al 5.

    Returns:
        Retorna diez cantidades, una por cada nota del 1 al 10.
    '''
    frecuencias = [0] * 10
    for i in range(len(estudiantes)):
        nota = estudiantes[i]["Notas"][numero_materia - 1]
        frecuencias[nota - 1] += 1
    return frecuencias


def mostrar_frecuencias(frecuencias: list) -> None:
    '''
    La función muestra cuántas veces aparece cada calificación.

    Args:
        frecuencias (list): Lista de cantidades para las notas del 1 al 10.

    Returns:
        Muestra el informe de frecuencias.
    '''
    print("\nNOTA\tCANTIDAD")
    for i in range(len(frecuencias)):
        print(f"{i + 1}\t{frecuencias[i]}")
