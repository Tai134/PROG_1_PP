import json
from Validaciones.Validaciones import validar_legajo
from Validaciones.Validaciones import validar_legajo_unico
from Validaciones.Validaciones import validar_nombre
from Validaciones.Validaciones import validar_genero
from Validaciones.Validaciones import validar_nota
from Validaciones.Validaciones import validar_materia
from Validaciones.Validaciones import validar_campos_csv


def pedir_legajo(estudiantes: list) -> int:
    '''
    La función solicita un legajo válido y único.

    Args:
        estudiantes (list): Estudiantes cargados hasta el momento.

    Returns:
        Retorna el legajo validado como entero.
    '''
    validacion = False
    legajo = 0
    while validacion == False:
        texto = input("Ingrese legajo de cinco cifras: ")
        validacion = validar_legajo(texto)
        if validacion == True:
            legajo = int(texto)
            validacion = validar_legajo_unico(legajo, estudiantes,
                                               len(estudiantes))
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
    La función solicita un género válido.

    Returns:
        Retorna F, M o X.
    '''
    validacion = False
    genero = ""
    while validacion == False:
        genero = input("Ingrese género (F-M-X): ")
        validacion = validar_genero(genero)
        if validacion == False:
            print("Género inválido")
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


def carga_manual(cantidad: int, estudiantes: list) -> None:
    '''
    La función solicita y valida los datos de cada estudiante.

    Args:
        cantidad (int): Cantidad de estudiantes a cargar.
        estudiantes (list): Lista donde se guardan los diccionarios.

    Returns:
        Completa la lista recibida con los datos ingresados.
    '''
    for i in range(cantidad):
        print(f"\nDATOS DEL ESTUDIANTE {i + 1}")
        estudiante = {"Legajo": pedir_legajo(estudiantes),
                      "Nombre": pedir_nombre(),
                      "Genero": pedir_genero(),
                      "Notas": [0] * 5,
                      "Promedio": 0}
        for j in range(5):
            estudiante["Notas"][j] = pedir_nota(j + 1)
        estudiantes.append(estudiante)


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


def guardar_promedios(estudiantes: list) -> list:
    '''
    La función guarda el promedio de cada estudiante con map y lambda.

    Args:
        estudiantes (list): Lista de diccionarios de estudiantes.

    Returns:
        Retorna una nueva lista con la clave Promedio actualizada.
    '''
    actualizados = list(map(
        lambda estudiante: {
            "Legajo": estudiante["Legajo"],
            "Nombre": estudiante["Nombre"],
            "Genero": estudiante["Genero"],
            "Notas": estudiante["Notas"],
            "Promedio": calcular_promedio(estudiante["Notas"])
        }, estudiantes))
    return actualizados


def mostrar_uno(i: int, estudiantes: list) -> None:
    '''
    La función muestra un registro usando su posición en la lista.

    Args:
        i (int): Posición del estudiante.
        estudiantes (list): Lista de diccionarios.

    Returns:
        Muestra los datos de un estudiante.
    '''
    estudiante = estudiantes[i]
    print(f"{estudiante['Legajo']}\t{estudiante['Nombre']}\t"
          f"{estudiante['Genero']}\t", end="")
    for j in range(len(estudiante["Notas"])):
        print(f"{estudiante['Notas'][j]}\t", end="")
    print(f"{estudiante['Promedio']:.2f}")


def mostrar_todos(estudiantes: list) -> None:
    '''
    La función recorre la lista y muestra cada estudiante.

    Args:
        estudiantes (list): Lista de diccionarios de estudiantes.

    Returns:
        Muestra todos los estudiantes.
    '''
    print("\nLEGAJO\tNOMBRE\tGENERO\tN1\tN2\tN3\tN4\tN5\tPROM.")
    for i in range(len(estudiantes)):
        mostrar_uno(i, estudiantes)


def ordenar_estudiantes(estudiantes: list, orden: str) -> None:
    '''
    La función ordena por promedio usando bubble sort ascendente o descendente.

    Args:
        estudiantes (list): Lista de diccionarios que se va a ordenar.
        orden (str): Orden solicitado, ASC o DESC.

    Returns:
        Reordena los estudiantes de acuerdo con el promedio.
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
    La función busca un legajo y devuelve su posición en la lista.

    Args:
        legajo (int): Legajo que se desea encontrar.
        estudiantes (list): Lista de diccionarios.

    Returns:
        Retorna la posición encontrada o -1 si no existe.
    '''
    i = 0
    while i < len(estudiantes) and estudiantes[i]["Legajo"] != legajo:
        i += 1
    if i == len(estudiantes):
        i = -1
    return i


def buscar_y_mostrar(estudiantes: list) -> None:
    '''
    La función busca un estudiante por legajo y muestra todos sus datos.

    Args:
        estudiantes (list): Lista de diccionarios.

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
    print("LEGAJO\tNOMBRE\tGENERO\tN1\tN2\tN3\tN4\tN5\tPROM.")
    mostrar_uno(i, estudiantes)


def promedios_materias(estudiantes: list) -> list:
    '''
    La función calcula el promedio general de cada materia.

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
    La función muestra el nombre y promedio de una materia.

    Args:
        i (int): Posición de la materia.
        promedios (list): Promedios generales por materia.

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


def pedir_materia() -> int:
    '''
    La función solicita el número de materia entre uno y cinco.

    Returns:
        Retorna el número de materia validado.
    '''
    validacion = False
    materia = 0
    while validacion == False:
        texto = input("Ingrese número de materia (1-5): ")
        validacion = validar_materia(texto)
        if validacion == True:
            materia = int(texto)
        if validacion == False:
            print("Materia inválida")
    return materia


def contar_notas(estudiantes: list, numero_materia: int) -> list:
    '''
    La función cuenta cuántas veces aparece cada nota en una materia.

    Args:
        estudiantes (list): Lista de diccionarios de estudiantes.
        numero_materia (int): Materia elegida, entre uno y cinco.

    Returns:
        Retorna una lista con las frecuencias de las notas del uno al diez.
    '''
    frecuencias = [0] * 10
    for i in range(len(estudiantes)):
        nota = estudiantes[i]["Notas"][numero_materia - 1]
        frecuencias[nota - 1] += 1
    return frecuencias


def mostrar_frecuencias(frecuencias: list) -> None:
    '''
    La función muestra las frecuencias de las calificaciones.

    Args:
        frecuencias (list): Cantidades de apariciones de las notas del uno al diez.

    Returns:
        Muestra el informe de frecuencias.
    '''
    print("\nNOTA\tCANTIDAD")
    for i in range(len(frecuencias)):
        print(f"{i + 1}\t{frecuencias[i]}")


def cargar_csv(ruta: str, estudiantes: list) -> bool:
    '''
    La función lee el CSV, valida cada registro y lo guarda en la lista.

    Args:
        ruta (str): Nombre o ubicación del archivo CSV.
        estudiantes (list): Lista donde se guardan los diccionarios.

    Returns:
        Retorna True cuando todos los registros fueron cargados.
    '''
    with open(ruta, "r") as archivo:
        lineas = archivo.readlines()

    if len(lineas) <= 1:
        print("El archivo CSV no contiene registros")
        return False

    cargado = True
    estudiantes_cargados = []
    for i in range(1, len(lineas)):
        linea = lineas[i].rstrip("\n")
        campos = linea.split(",")
        if validar_campos_csv(campos, estudiantes_cargados) == True:
            notas = [0] * 5
            for j in range(5):
                notas[j] = int(campos[j + 3])
            estudiante = {"Legajo": int(campos[0]),
                          "Nombre": campos[1],
                          "Genero": campos[2],
                          "Notas": notas,
                          "Promedio": 0}
            estudiantes_cargados.append(estudiante)
        else:
            print(f"Datos inválidos en la línea {i + 1} del CSV")
            cargado = False
            break
    if cargado == True:
        for i in range(len(estudiantes_cargados)):
            estudiantes.append(estudiantes_cargados[i])
    return cargado


def guardar_json(estudiantes: list, ruta: str) -> bool:
    '''
    La función guarda los estudiantes en formato JSON.

    Args:
        estudiantes (list): Lista de diccionarios a guardar.
        ruta (str): Nombre o ubicación del archivo.

    Returns:
        Retorna True si los datos fueron guardados.
    '''
    datos_json = []
    for i in range(len(estudiantes)):
        estudiante_json = {"legajo": estudiantes[i]["Legajo"],
                           "nombre": estudiantes[i]["Nombre"],
                           "genero": estudiantes[i]["Genero"],
                           "notas": estudiantes[i]["Notas"],
                           "promedio": estudiantes[i]["Promedio"]}
        datos_json.append(estudiante_json)
    with open(ruta, "w") as archivo:
        json.dump(datos_json, archivo, indent=4)
    return True


def convertir_caracter_mayuscula(caracter: str) -> str:
    '''
    La función convierte una letra minúscula a mayúscula usando su código.

    Args:
        caracter (str): Un carácter de texto.

    Returns:
        Retorna el carácter en mayúscula cuando corresponde.
    '''
    codigo = ord(caracter)
    if codigo >= 97 and codigo <= 122:
        caracter = chr(codigo - 32)
    return caracter


def convertir_mayuscula(texto: str) -> str:
    '''
    La función convierte un texto a mayúsculas mediante map.

    Args:
        texto (str): Texto que se desea convertir.

    Returns:
        Retorna el texto convertido a mayúsculas.
    '''
    resultado = ""
    caracteres = map(convertir_caracter_mayuscula, texto)
    for caracter in caracteres:
        resultado += caracter
    return resultado


def normalizar_estudiantes(estudiantes: list) -> list:
    '''
    La función crea una lista nueva con nombres y géneros en mayúscula.

    Args:
        estudiantes (list): Lista de diccionarios de estudiantes.

    Returns:
        Retorna la lista normalizada sin modificar la lista recibida.
    '''
    normalizados = list(map(
        lambda estudiante: {
            "Legajo": estudiante["Legajo"],
            "Nombre": convertir_mayuscula(estudiante["Nombre"]),
            "Genero": convertir_mayuscula(estudiante["Genero"]),
            "Notas": estudiante["Notas"],
            "Promedio": estudiante["Promedio"]
        }, estudiantes))
    return normalizados


calcular_promedio = lambda notas: redondeo((notas[0] + notas[1] + notas[2] + \
                                            notas[3] + notas[4]) / 5)


def mostrar_filtrados(estudiantes: list) -> None:
    '''
    La función filtra y muestra estudiantes con promedio menor a cuatro.

    Args:
        estudiantes (list): Lista de diccionarios con promedios calculados.

    Returns:
        Muestra los estudiantes que cumplen el criterio.
    '''
    filtrados = list(filter(lambda estudiante: estudiante["Promedio"] < 4, estudiantes))
    if len(filtrados) == 0:
        print("No hay estudiantes con promedio menor a 4")
    else:
        mostrar_todos(filtrados)


