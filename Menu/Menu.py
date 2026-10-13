from Carga_de_datos.Carga_datos import cargar_datos
from Carga_de_datos.Solicitud_datos import solicitar_legajo
from Operaciones.Promedios import calcular_promedios
from Operaciones.Busqueda import buscar_por_legajo
from Ordenamientos.Ordenamiento_listas import ordenar_por_promedio
from Display.Mostrar_estudiante import mostrar_estudiantes
from Display.Mostrar_estudiante import mostrar_estudiante
from Display.Mostrar_estudiante import mostrar_mayores

def menu() -> None:
    '''
    La función muestra y controla el menú principal del programa.
    No permite acceder a las opciones si los datos todavía no fueron
    cargados.
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
        print("\n\t\t\tMENU PRINCIPAL")
        print("1 - Cargar datos")
        print("2 - Mostrar todos los datos")
        print("3 - Calcular promedios")
        print("4 - Mostrar ordenados por promedio DESC")
        print("5 - Mostrar estudiante/s con mayor promedio")
        print("6 - Buscar estudiante por legajo")
        print("7 - Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            cargar_datos(cantidad, legajos, nombres, generos, notas_1,
                         notas_2, promedios)
            cargados = True
            print("Los datos fueron cargados correctamente")
        elif opcion == "7":
            salir = True
            print("Programa finalizado")
        elif opcion == "2" or opcion == "3" or opcion == "4" \
                or opcion == "5" or opcion == "6":
            if cargados == False:
                print("Debe cargar los datos antes de elegir otra opción")
            elif opcion == "2":
                mostrar_estudiantes(legajos, nombres, generos, notas_1,
                                    notas_2, promedios)
            elif opcion == "3":
                promedios_nuevos = calcular_promedios(notas_1, notas_2)

                for i in range(cantidad):
                    promedios[i] = promedios_nuevos[i]

                print("Los promedios fueron calculados correctamente")
            elif opcion == "4":
                orden = ""
                validacion = False

                while validacion == False:
                    orden = input("Ingrese ASC o DESC. "
                                  "Presione Enter para usar DESC: ")

                    if orden == "" or orden == "ASC" or orden == "DESC":
                        validacion = True
                    else:
                        print("Orden inválido. Ingrese ASC o DESC")

                if orden == "":
                    orden = "DESC"

                ordenar_por_promedio(promedios, legajos, nombres, generos,
                                     notas_1, notas_2, orden)
                mostrar_estudiantes(legajos, nombres, generos, notas_1,
                                    notas_2, promedios)
            elif opcion == "5":
                mostrar_mayores(legajos, nombres, generos, notas_1,
                                notas_2, promedios)
            elif opcion == "6":
                indice = -1
                print("Ingrese el legajo que desea buscar")

                while indice == -1:
                    legajo_buscado = solicitar_legajo()
                    indice = buscar_por_legajo(legajo_buscado, legajos)

                    if indice == -1:
                        print("No se encontró un estudiante con ese legajo")
                        print("Ingrese nuevamente un legajo válido")

                print("\nLEGAJO\tAPELLIDO Y NOMBRE\tGENERO\t"
                      "NOTA 1\tNOTA 2\tPROMEDIO")
                mostrar_estudiante(indice, legajos, nombres, generos,
                                   notas_1, notas_2, promedios)
        else:
            print("Opción inválida. Ingrese una opción del 1 al 7")
