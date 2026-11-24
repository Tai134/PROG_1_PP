from Validaciones.Validaciones import validar_legajo
from Validaciones.Validaciones import validar_legajo_unico
from Validaciones.Validaciones import validar_nombre
from Validaciones.Validaciones import validar_genero
from Validaciones.Validaciones import validar_nota
from Validaciones.Validaciones import validar_materia
from Funciones import hardcod_prueb


def pedir_legajo(legajos: list, cantidad_cargada: int) -> int:
    '''
    La función solicita un legajo y comprueba su formato y unicidad.

    Args:
        legajos (list): Lista donde se guardan los legajos.
        cantidad_cargada (int): Cantidad de legajos cargados previamente.

    Returns:
        Retorna el legajo validado como un número entero.
    '''
    validacion = False
    legajo = 0
    while validacion == False:
        texto = input("Ingrese legajo de cinco cifras: ")
        validacion = validar_legajo(texto)
        if validacion == True:
            legajo = int(texto)
            validacion = validar_legajo_unico(legajo, legajos,
                                               cantidad_cargada)
            if validacion == False:
                print("El legajo ya fue ingresado")
        else:
            print("El legajo debe tener cinco cifras")
    return legajo


def pedir_nombre() -> str:
    '''
    La función solicita un nombre y repite el pedido hasta que sea válido.

    Returns:
        Retorna el nombre validado como texto.
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
    La función solicita un género válido y lo convierte a mayúscula si hace falta.

    Returns:
        Retorna el género validado como texto.
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
    La función solicita una nota entera válida para la materia indicada.

    Args:
        materia (int): Número de materia que se está cargando.

    Returns:
        Retorna la nota validada como un número entero.
    '''
    validacion = False
    nota = 0
    while validacion == False:
        texto = input(f"Ingrese nota de materia {materia} (1-10): ")
        validacion = validar_nota(texto)
        if validacion == True:
            nota = int(texto)
        else:
            print("La nota debe ser un entero entre 1 y 10")
    return nota


def pedir_materia() -> int:
    '''
    La función solicita el número de una materia y valida su rango.

    Returns:
        Retorna el número de materia como un entero entre 1 y 5.
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


def cargar_datos(cantidad: int, matriz: list, legajos: list,
                 nombres: list, generos: list) -> None:
    '''
    La función solicita los datos de cada estudiante y carga las listas
    paralelas y la matriz de calificaciones.

    Args:
        cantidad (int): Cantidad de estudiantes que se deben cargar.
        matriz (list): Matriz donde se guardan las cinco notas.
        legajos (list): Lista donde se guardan los legajos.
        nombres (list): Lista donde se guardan los nombres.
        generos (list): Lista donde se guardan los géneros.

    Returns:
        Completa las estructuras recibidas.
    '''
    for i in range(cantidad):
        print(f"\nESTUDIANTE {i + 1}")
        legajos[i] = pedir_legajo(legajos, i)
        nombres[i] = pedir_nombre()
        generos[i] = pedir_genero()
        for j in range(5):
            matriz[i][j] = pedir_nota(j + 1)


def cargar_hardcodeados(cantidad: int, matriz: list, legajos: list,
                        nombres: list, generos: list) -> None:
    '''
    La función copia los datos de prueba a las listas y matriz del programa.

    Args:
        cantidad (int): Cantidad de estudiantes a copiar.
        matriz (list): Matriz donde se copian las calificaciones.
        legajos (list): Lista donde se copian los legajos.
        nombres (list): Lista donde se copian los nombres.
        generos (list): Lista donde se copian los géneros.

    Returns:
        Completa las estructuras recibidas.
    '''
    for i in range(cantidad):
        legajos[i] = hardcod_prueb.legajos[i]
        nombres[i] = hardcod_prueb.nombres[i]
        generos[i] = hardcod_prueb.generos[i]
        for j in range(5):
            matriz[i][j] = hardcod_prueb.matriz[i][j]


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
    valor_redondeado = centesimas / 100
    return valor_redondeado


def calcular_promedio(fila: list) -> float:
    '''
    La función calcula el promedio de las notas de un estudiante.

    Args:
        fila (list): Fila de la matriz con las notas del estudiante.

    Returns:
        Retorna el promedio redondeado a dos decimales.
    '''
    suma = 0
    for i in range(len(fila)):
        suma += fila[i]
    promedio = suma / len(fila)
    return redondeo(promedio)


def carga_promedios(matriz: list, promedios: list) -> None:
    '''
    La función calcula el promedio de cada estudiante y lo guarda en la
    posición correspondiente de la lista de promedios.

    Args:
        matriz (list): Matriz de calificaciones.
        promedios (list): Lista donde se guardan los promedios calculados.

    Returns:
        Completa la lista recibida.
    '''
    for i in range(len(matriz)):
        promedios[i] = calcular_promedio(matriz[i])


def mostrar_uno(indice: int, matriz: list, legajos: list, nombres: list,
                generos: list, promedios: list,
                mostrar_promedio: bool = True) -> None:
    '''
    La función muestra los datos de un estudiante usando el mismo índice
    en las listas paralelas y la matriz.

    Args:
        indice (int): Posición del estudiante que se desea mostrar.
        matriz (list): Matriz de calificaciones.
        legajos (list): Lista de legajos.
        nombres (list): Lista de nombres.
        generos (list): Lista de géneros.
        promedios (list): Lista de promedios.
        mostrar_promedio (bool): Indica si se debe imprimir el promedio.

    Returns:
        Muestra los datos en pantalla.
    '''
    print(f"{legajos[indice]}\t{nombres[indice]}\t{generos[indice]}\t", end="")
    for j in range(len(matriz[indice])):
        print(f"{matriz[indice][j]}\t", end="")
    if mostrar_promedio == True:
        print(f"{promedios[indice]:.2f}")
    else:
        print("\n", end="")


def mostrar_todos(matriz: list, legajos: list, nombres: list,
                  generos: list, promedios: list,
                  mostrar_promedio: bool = True) -> None:
    '''
    La función recorre todos los estudiantes y llama a mostrar_uno para
    imprimir cada registro.

    Args:
        matriz (list): Matriz de calificaciones.
        legajos (list): Lista de legajos.
        nombres (list): Lista de nombres.
        generos (list): Lista de géneros.
        promedios (list): Lista de promedios.
        mostrar_promedio (bool): Indica si se imprime la columna promedio.

    Returns:
        Muestra todos los registros en pantalla.
    '''
    print("\nLEGAJO\tNOMBRE\tGENERO\tMAT_1\tMAT_2\tMAT_3\tMAT_4\tMAT_5",
          end="")
    if mostrar_promedio == True:
        print("\tPROMEDIO")
    else:
        print("\n", end="")
    for i in range(len(legajos)):
        mostrar_uno(i, matriz, legajos, nombres, generos, promedios,
                    mostrar_promedio)


def ordenar(matriz: list, legajos: list, nombres: list, generos: list,
            promedios: list, orden: str) -> None:
    '''
    La función ordena los estudiantes por promedio con el método burbuja.
    Al intercambiar, conserva juntos los datos paralelos y su fila de notas.

    Args:
        matriz (list): Matriz de calificaciones.
        legajos (list): Lista de legajos.
        nombres (list): Lista de nombres.
        generos (list): Lista de géneros.
        promedios (list): Lista de promedios.
        orden (str): Orden solicitado, ASC o DESC.

    Returns:
        Reordena las estructuras recibidas.
    '''
    cantidad = len(promedios)
    for i in range(cantidad - 1):
        for j in range(cantidad - i - 1):
            intercambiar = False
            if orden == "ASC" and promedios[j] > promedios[j + 1]:
                intercambiar = True
            elif orden == "DESC" and promedios[j] < promedios[j + 1]:
                intercambiar = True
            if intercambiar == True:
                auxiliar = promedios[j]
                promedios[j] = promedios[j + 1]
                promedios[j + 1] = auxiliar
                auxiliar = legajos[j]
                legajos[j] = legajos[j + 1]
                legajos[j + 1] = auxiliar
                auxiliar = nombres[j]
                nombres[j] = nombres[j + 1]
                nombres[j + 1] = auxiliar
                auxiliar = generos[j]
                generos[j] = generos[j + 1]
                generos[j + 1] = auxiliar
                auxiliar = matriz[j]
                matriz[j] = matriz[j + 1]
                matriz[j + 1] = auxiliar


def buscar_indice(legajo: int, legajos: list) -> int:
    '''
    La función busca un legajo recorriendo la lista por índice.

    Args:
        legajo (int): Legajo que se desea encontrar.
        legajos (list): Lista de legajos.

    Returns:
        Retorna el índice encontrado o -1 si el legajo no existe.
    '''
    indice = -1
    for i in range(len(legajos)):
        if legajos[i] == legajo:
            indice = i
            break
    return indice


def buscar_y_mostrar(matriz: list, legajos: list, nombres: list,
                     generos: list, promedios: list) -> None:
    '''
    La función solicita un legajo, lo busca y muestra el registro encontrado.
    Si no existe, vuelve a solicitarlo.

    Args:
        matriz (list): Matriz de calificaciones.
        legajos (list): Lista de legajos.
        nombres (list): Lista de nombres.
        generos (list): Lista de géneros.
        promedios (list): Lista de promedios.

    Returns:
        Muestra el estudiante encontrado.
    '''
    indice = -1
    while indice == -1:
        texto = input("Ingrese legajo a buscar: ")
        if validar_legajo(texto) == True:
            indice = buscar_indice(int(texto), legajos)
        if indice == -1:
            print("No se encontró el legajo; intente nuevamente")
    print("LEGAJO\tNOMBRE\tGENERO\tMAT_1\tMAT_2\tMAT_3\tMAT_4\tMAT_5\tPROMEDIO")
    mostrar_uno(indice, matriz, legajos, nombres, generos, promedios)


def promedios_materias(matriz: list) -> list:
    '''
    La función calcula los promedios generales de las cinco materias.

    Args:
        matriz (list): Matriz con las calificaciones de los estudiantes.

    Returns:
        Retorna una lista con el promedio general de cada materia.
    '''
    promedios = [0] * 5
    for j in range(5):
        suma = 0
        for i in range(len(matriz)):
            suma += matriz[i][j]
        promedio = suma / len(matriz)
        promedios[j] = redondeo(promedio)
    return promedios


def mostrar_materia(indice: int, promedios: list) -> None:
    '''
    La función muestra el nombre y el promedio de una materia.

    Args:
        indice (int): Índice de la materia en la lista de promedios.
        promedios (list): Lista con los promedios generales por materia.

    Returns:
        Muestra una materia en pantalla.
    '''
    print(f"MATERIA_{indice + 1}\t{promedios[indice]:.2f}")


def mostrar_materias_mayores(matriz: list) -> None:
    '''
    La función obtiene y muestra todas las materias con mayor promedio
    general, incluyendo las que empaten.

    Args:
        matriz (list): Matriz con las calificaciones de los estudiantes.

    Returns:
        Muestra las materias con mayor promedio.
    '''
    promedios = promedios_materias(matriz)
    mayor = promedios[0]
    for i in range(1, len(promedios)):
        if promedios[i] > mayor:
            mayor = promedios[i]
    print("\nMATERIA/S CON MAYOR PROMEDIO GENERAL")
    print("MATERIA\tPROMEDIO")
    for i in range(len(promedios)):
        if promedios[i] == mayor:
            mostrar_materia(i, promedios)


def contar_notas(matriz: list, numero_materia: int) -> list:
    '''
    La función cuenta cuántas veces aparece cada nota en una materia.

    Args:
        matriz (list): Matriz con las calificaciones.
        numero_materia (int): Número de materia entre 1 y 5.

    Returns:
        Retorna una lista de diez posiciones con la frecuencia de las notas
        del 1 al 10.
    '''
    frecuencias = [0] * 10
    for i in range(len(matriz)):
        nota = matriz[i][numero_materia - 1]
        frecuencias[nota - 1] += 1
    return frecuencias


def mostrar_frecuencias(frecuencias: list) -> None:
    '''
    La función muestra cuántas veces aparece cada calificación.

    Args:
        frecuencias (list): Lista con las cantidades de notas del 1 al 10.

    Returns:
        Imprime las frecuencias en pantalla.
    '''
    print("\nNOTA\tCANTIDAD")
    for i in range(len(frecuencias)):
        print(f"{i + 1}\t{frecuencias[i]}")
