########## PRACTICA 1. Automata Finito No Determinista ##########
### Elaborado por: Mauro Sampayo Hernandez
### Compiladores Grupo 3CV17

## IMPORTACION DE LAS CLASES PARA LA GENERACION DE ARBOLES
from anytree import Node, RenderTree, PostOrderIter, Walker
from tabulate import tabulate

## DEFINICION VARIALES GLOBALES ##
# Varaibles para la generacion del AFN
Estados = []
Alfabeto = []
edo_inicial = ""
Edos_finales = []
Transiciones = []
#Variables para la validacion de una cadena dentro del AFN
cadena = []
errores = []
recorrido = []
Nodos = {}


## FUNCION GENERAR LISTA
# Genera una lista de los elementos de la tula del AFN a partir de las primeras lineas del archivo
def GenerarLista(linea, lista):
    aux = ""

    for i in linea:
        # En caso de que se halle una coma o salto de linea, indicara que un estado termino de ser leeido
        if i == "," or i == "\n":
            lista.append(aux)
            aux = ""
            continue;
        else:
            aux = aux + i

## FUNCION GENERAR TRANSICIONES
# Genera la tabla de Transiciones delta del AFN a partir de las lineas restantes del archivo
def GenerarTransiciones (linea):
    # Variables locales para el proceso de rellenado de la tabla de Transiciones
    fila_edo = 0
    col_simb = 0
    aux = ""
    cont_comas = 0
    listaAux1 = []
    listaAux2 = []

    # Ciclo que recorrera todas las lineas restantes del archivo de texto convertidas en una cadena de texto
    for j in linea:
        for i in j:
            ## La función principal de estos condicionales, es el de determinar en que posicion dentro de la tabla de Transiciones
            ## del AFN se ubicarán los estados resultantes de cada una de las transiciones. Se debe recordar que esta tabla esta
            ## representada por una lista de 3 dimensiones y que se esta tomando como referencia los indices de las tablas del
            ## alfabeto y estados para determinar dichas posiciones

            # En caso de que se encuentre una coma, significa que uno de los atributos de la tabla sigma de una transicion termino de leerse
            if i == ",":
                cont_comas += 1

                # Si se encontro la primera coma de una línea significa que se termino de leer el estado origen.
                # Comprueba que el estado sea parte de la lista de estados del AFN
                if cont_comas == 1:
                    if not (aux in Estados):
                        print(" !! ERROR: Estado no valido en tabla de Transiciones")
                        exit(1)
                    else:
                        fila_edo = Estados.index(aux)
                # Si se encontro la segunda coma de una línea significa que se termino de leer el simbolo de transicion.
                # Comprueba que el simbolo sea parte del alfabeto del AFN.
                elif cont_comas == 2:
                    if not (aux in Alfabeto):
                        print(" !! ERROR: Simbolo no valido en tabla de Transiciones")
                        exit(1)
                    else:
                        col_simb = Alfabeto.index(aux)
                # Como solo pueden haber 2 comas por linea de texto, cualquier otro caso dara error y finalizara el programa
                else:
                    print("ERROR: Hay un error en el formato del archivo")
                    exit(1)

                aux = ""  # Se libera la funcion aux para leer el siguienre atributo de la ytabla sigma de la linea
            # Para el caso en que se encuentre un salto de linea, significa que la lectura del ultimo atributo de la tabla sigma de la tabla
            # sigma de una transicion termino de leerse
            ## --NOTA: Debido a que la ultima linea del archivo no cuenta con un salto de linea, se debe añadir una linea vacia extra al final
            ## el archivo para que el prohgrama funcione correctamente.
            elif i == "\n":
                # Para el caso de que ya exista la lista de estados resultantes de una transicion de un estado determinado, simplemente se
                # añadiran los demas resultantes de dicha transicion en la misma
                if fila_edo < len(Transiciones):
                    # En caso de que ya exista la lista de estados destinos de una transicion, simplemente se añadiran el resto de estados en
                    # la misma
                    if col_simb < len(Transiciones[fila_edo]):
                        # Para el caso de que la lista de estados destinos de una transicion haya sido rellenada provisionalmente con un error, este se quita
                        if "_err" in Transiciones[fila_edo][col_simb]:
                            Transiciones[fila_edo][col_simb].remove("_err")

                        Transiciones[fila_edo][col_simb].append(aux)
                    # Para el caso de que no se haya creado la lista de estados destinos de una transiciono, se realizara la creacion de dicha lista
                    else:
                        # Para el caso de que se quiera incializar una lista insertando un elemento en una posicion mayor a la de la longitud de la lista,
                        # Phyton automaticamente colocara el item despues del ultimo elemento agregado a la misma para evitar dejar espacios sin información.
                        # Por lo tanto, todos los espacios que esten entre la posicion del último item añadido a la lista y la posicion en la que se desea
                        # colocar el nuevo item se relleneran con un estado de error provisionalmente
                        if col_simb > len(Transiciones[fila_edo]):
                            listaAux2.append("_err") # _err sera el estado de error del AFN
                            for x in range(len(Transiciones[fila_edo]),col_simb):
                                Transiciones[fila_edo].insert(x, listaAux2[:])

                        listaAux2.clear()
                        listaAux2.append(aux)
                        Transiciones[fila_edo].append(listaAux2[:]) # Envia una copia de la listaAux2, para evitar que se modifique dentro de la lista Transiciones
                        listaAux2.clear()

                    # Se realiza el ordenamiento de los estados destino, con el objetivo de llevar un mejor orden y sea mas entendible
                    ##Transiciones[fila_edo][col_simb].sort() ###!!!!!
                    ######print(Transiciones)
                # Para el caso de que no se haya creado la lista de estados resultantes de la transicion de un determinado estado, se realizara
                # la creacion de dicha lista
                else:
                    # Para el caso de que se quiera incializar una lista insertando un elemento en una posicion distinta a 0, y debido a que Phyton
                    # en el caso que se quiera insertar un item en una Lista una posicion mayor a la de la longitud de la misma automaticamente lo
                    # colocara despues del ultimo elemento de la Lista para evitar dejar espacios dentro e esta sin información; es que se rellenaran
                    # todos los espacios que presceden a la posicion donde se quiere insertar el item con un estado de error
                    if col_simb > 0:
                        listaAux2.append("_err") # _err sera el estado de error del AFN
                        for x in range(col_simb):
                            listaAux1.append(listaAux2[:]) # Envia una copia de la listaAux2, para evitar que se modifique dentro de la listaAux1

                    listaAux2.clear()
                    listaAux2.append(aux)
                    listaAux1.insert(col_simb, listaAux2[:]) # Envia una copia de la listaAux2, para evitar que se modifique dentro de la listaAux1
                    Transiciones.append(listaAux1[:]) # Envia una copia de la listaAux1, para evitar que se modifique dentro de la lista Transiciones
                    listaAux2.clear()
                    listaAux1.clear()
                    ######print(Transiciones)

                # Se resetean las variables utilizadas en el proceso para las transiciones de los estados siguientes
                fila_edo = 0
                col_simb = 0
                aux = ""
                cont_comas = 0
            # En caso de que no se encuente una coma o salto de linea, significa que se esta leyendo un atributo de la tabla de Transiciones
            else:
                aux = aux + i
                #######print(aux)
    # print(Transiciones)

## FUNCION GENERAR AUTOMATA
# Abrirá el archivo de texto que contiene la informacion necesaria para la construccion de un AFN y
# a partir de los datos contenidos en esta generara el AFN
def GenerarAutomata():
    # Se abre el archivo de texto para su lectura
    f = open("2.txt", "r")
    global edo_inicial

    # De la primera linea se obtiene la lista de estados que conforman al AFN
    GenerarLista(f.readline(), Estados)
    # De la segunda linea se obtiene los simbolos que conforman el alfabeto del AFN
    GenerarLista(f.readline(), Alfabeto)

    # De la tercera linea se obtiene el estado incial del AFN
    for i in f.readline():
        if i != "\n":
            edo_inicial = edo_inicial + i
    # Comprobamos que el estado inicial sea un estado valido
    if not(edo_inicial in Estados):
        print(" !! ERROR: Estado inicial no está en la lista de Estados definida para el AFN")
        exit(1)

    # De la cuarta linea se obtiene la lista de estados finales del AFN
    GenerarLista(f.readline(), Edos_finales)
    # Comprobamos que los estados finales sean validos
    for i in Edos_finales:
        if not(i in Estados):
            print(f" !! ERROR: Estado final '{i}' no está en la lista de Estados definida para el AFN")
            exit(1)

    # Del resto de lineas se obtiene la tabla de Transiciones delta
    GenerarTransiciones(f.readlines())

## FUNCION COMPLETAR AUTOMATA
# Genera las transiciones de error faltantes en la tabla de Transiciones, y añade el estado de error a la lista de Estados
# junto a sus respectivas transiciones (todas van a resulktar en estado de error)
def CompletarAutomata():
    listaAux = ["_err"]
    listaAux2 = []

    # Bucle que completa las transiciones que van a error en cada estado
    for i in Transiciones:
        if len(i) < len(Alfabeto):
            for j in range(len(i), len(Alfabeto)):
                i.append(listaAux[:])
        else:
            continue

    # Bucle para generar todos los estados de error para el estado final, en caso de que este no haya sido creado previamenre
    if len(Transiciones) < len(Estados):
        for i in range (0, len(Alfabeto)):
            listaAux2.append(listaAux)

        Transiciones.append(listaAux2)
        Estados.append("_err")

    # Para el caso de que se halla añadido un estado de error se añaden sus transiciones
    if len(Transiciones) < len(Estados):
        Transiciones.append(listaAux2)
    #print(Transiciones)

## FUNCION IMPRIMIR LISTA
# Da formato a la impresion de los elementos de una lista determinada
# Devuelve una cadena con la impresion de los elementos de la lista en dicho formato
def ImprimirLista(lista):
    c = ', '.join(lista)
    return c

## FUNCION IMPRIMIR AUTOMATA
# Imprime cada uno de los elementos de la tupla del AFN con sus respectivos valores
def ImprimirAutomata():
    print(f"\nEstados = ({ImprimirLista(Estados)})")
    print(f"Alfabeto = ({ImprimirLista(Alfabeto)})")
    print(f"Estado_inicial = {edo_inicial}")
    print(f"Estados_finales = ({ImprimirLista(Edos_finales)})")

    # Impresion de la tabla de Transiciones
    data = []
    aux = []
    cabecera = Alfabeto[:]
    cabecera.insert(0, "Estado")

    for i in range(len(Transiciones)):
        aux.append(Estados[i])
        for j in range(len(Transiciones[i])):
            aux.append(Transiciones[i][j])
        data.append(aux[:])
        aux.clear()

    print("Tabla de Transiciones: \n")
    print(tabulate(data, headers = cabecera))


## FUNCION GENERAR ARBOL DE RESULTADOS
# Genera un arbol que representa cada una de las transiciones de estado que se generen a partir de la evaluacionde una cadena
# Este arbol servira posteriormente para evaluar la cadena
# Asi mismo se identifican los simbolos no pertenecientes al Alfabeto que puedan venir en la cadena para manejarlos como error
def GenerarArbolResultados():
    # Variables auxiliares de la funcion
    PilaNodos = []
    pilaAux = []
    id = 1

    # Se crea el nodo raíz del Arbol de Resultados usando el estado inicial
    root = Node(edo_inicial)
    # El nodo se guarda dentro de un diccionario de Nodos, que guardara todos los nodos que conformen el arbol de Resultados
    # Cada nodo sera guardado con un nodo unico ascendente el cual sera de utilidad al momento de recorrer el arbol para
    # evaluar la cadena
    Nodos[0] = (root)
    PilaNodos.append(root)

    for i in cadena:
        # En caso de que el simbolo a evaluar no forme parte del alfabeto se omititira y se pasara al siguiente simbolo
        # Se guardara el simbolo omitido dentro de una lista de errores para enlistarlos al final de la evaluacion
        if not(i in Alfabeto):
            for edo in PilaNodos:
                print(f"-- ERROR en el estado {edo.name}: Valor {i} no pertenece al Alfabeto del automata, por lo que se ha omitido")
            errores.append(i)
        # Si el simbolo a evaluar forma parte del alfabeto, este se usara para generar el arbol
        else:
            # Se obtiene la ubicacion de la columna de la tabla de transiciones donde se encuentra la transicion del estado,
            # usando como referencia el simbolo obtenido
            columna = Alfabeto.index(i)
            cont = len(PilaNodos)

            # Este ciclo servira para obtener todos los estados resultantes de una transicion
            for j in range(cont):
                edo_actual = PilaNodos.pop()
                # Se obtiene la la ubicacion de la fila de la tabla de transiciones donde se encuentra la transicion de un estado,
                # usando como referencia el estado actual en donde nos encontramos
                fila = Estados.index(edo_actual.name)

                # Para evitar que se repita el estado de error una vez una transicion ha llegado a este por primera vez, los
                # estados resultantes de una transicion solo se contaran dentro de el arbol si es que no son stados derivados
                # del error
                if not(edo_actual.name == "_err"):
                    # Se obtienen todos los estados resultantes de una transicion
                    for k in Transiciones[fila][columna]:
                        Nodos[id] = (Node(k, parent = edo_actual))
                        pilaAux.append(Nodos[id])
                        id += 1

            PilaNodos = pilaAux[:]
            pilaAux.clear()

    #print(RenderTree(root).by_attr()) # --- Descomentar para ver la genereacion de la cadena
    # print(Nodos)
    # print(errores)

# FUNCION VALIDAR CADENA
# Realiza la validacion de la cadena insertada por medio de un recorrido PostOrden en el arbol
# Si un nodo estado final sin hijos es encontrado en el arbol, la cadena sera valida y se registra el recorrido. Se devuelve True
# Si un nodo estado final sin hijos no es encontrado en el arbol, la cadena no sera valida. Se devuelve False
def ValidarCadena():
    r = []
    bandera = False

    # Realiza la busqueda de un nodo estado final, por medio de una busqueda en PostOrden
    for node in PostOrderIter(Nodos[0]):
        #print(f"{node.name}", end = ", ")

        # Para el caso que se encuentre un nodo de estado final en el arbol que no tenga hijos
        if (node.name in Edos_finales) and node.is_leaf:
            # Se realiza la obtencion de la llave del diccionario en donde esta almacenado el nodo del estado final
            for key, value in Nodos.items():
                if node == value:
                    EdoFinal_key = key
                    break
            # print(f"{EdoFinal_key}")

            # Creamos un Walker para hacer recorridos entre los nodos del arbol
            w = Walker()
            # Realizamos el recorrido desde el nodo raiz hasta el nodo del estado final
            tuplaAux = w.walk(Nodos[0], Nodos[EdoFinal_key])
            # Añadimos el nodo raiz al recorrido auxiliar
            r.append(Nodos[0].name)

            # Añadimos el resto de nodos al recorrido auxiliar
            for i in tuplaAux[2]:
                r.append(i.name)

            # Añadimos el recorrido a la lista de recorridos global
            recorrido.append(r[:])
            r.clear()
            # print(recorrido)
            # Al haberse encontrado un nodo de Estado Final sin hijos, la cadena es valida, por lo que se devuelve bandera en True
            bandera = True

    # Al no haberse encontrado un nodo de Estado Final sin hijos, la cadena no es valida, por lo que se devuelve False
    return bandera

def main():
    GenerarAutomata()
    CompletarAutomata()
    ImprimirAutomata()

    c = input("\n-> Digite la cadena a ser validada: ")
    for i in c:
        cadena.append(i)
    print("")
    #print(cadena)

    GenerarArbolResultados()
    validacion = ValidarCadena()

    # Si la cadena es valida se imprime el recorrido de estados dentro del AFN de dicha cadena
    if validacion:
        print("\n\t* Cadena Valida :)")
        print(f"\t* Recorridos de estados validos: ")

        for i in range(len(recorrido)):
            c = ' -> '.join(recorrido[i])
            print(f"\t\t Recorrido #{i+1}. ({c})")
            c = ""
    else:
        print("\n\t* Cadena No Valida >:(")

    # Si se encontraron errores de simbolos no pertenecientes al alfabeto del AFN durante la eveluacion de la cadena, se mostraran
    if len(errores) > 0:
        print(f"\t* Simbolos omitiddos: ({ImprimirLista(errores)})")

# Ejecutamos la funcion main
if __name__ == '__main__':
    main()