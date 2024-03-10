########## PRACTICA 2. Conversión de AFN-epsilon a AFD ##########
### Elaborado por: Mauro Sampayo Hernandez
### Compiladores Grupo 3CV17

## IMPORTACION DE LIBRERIAS
import string
from tabulate import tabulate

## DEFINICION VARIALES GLOBALES ##
# Varaibles para la generacion del AFN-epsilon
EstadosAFN = []
AlfabetoAFN = []
edo_inicialAFN = ""
edo_finalAFN = ""
TransicionesAFN = []
#Variables para la generacion del AFD
EstadosAFD = {}
AlfabetoAFD = []
edo_inicialAFD = ""
Edos_finalesAFD = []
TransicionesAFD= []

## FUNCION GENERAR LISTA
# Genera una lista de los elementos de la tupla del AFN a partir de las primeras lineas del archivo
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
                    if not(aux in EstadosAFN):
                        print(" !! ERROR: Estado no valido en tabla de Transiciones")
                        exit(1)
                    else:
                        fila_edo = EstadosAFN.index(aux)
                # Si se encontro la segunda coma de una línea significa que se termino de leer el simbolo de transicion.
                # Comprueba que el simbolo sea parte del alfabeto del AFN. Se añade la excepcion del simbolo epsiclon E
                elif cont_comas == 2:
                    if not(aux in AlfabetoAFN):
                        # En caso de que se encuentre una transicion epsilon y esta aun no se encuentre listada en el alfabeto del AFN, automaticamente
                        # se añadira a este y se continuara de manera normal el proceso
                        if aux == "E":
                            AlfabetoAFN.append(aux)
                        else:
                            print(" !! ERROR: Simbolo no valido en tabla de Transiciones")
                            exit(1)

                    col_simb = AlfabetoAFN.index(aux)
                # Como solo pueden haber 2 comas por linea de texto, cualquier otro caso dara error y finalizara el programa
                else:
                    print("ERROR: Hay un error en el formato del archivo")
                    exit(1)

                aux = "" # Se libera la funcion aux para leer el siguienre atributo de la ytabla sigma de la linea
            # Para el caso en que se encuentre un salto de linea, significa que la lectura del ultimo atributo de la tabla sigma de la tabla
            # sigma de una transicion termino de leerse
            ## --NOTA: Debido a que la ultima linea del archivo no cuenta con un salto de linea, se debe añadir una linea vacia extra al final
            ## el archivo para que el prohgrama funcione correctamente.
            elif i == "\n":
                # Para el caso de que ya exista la lista de estados resultantes de una transicion de un estado determinado, simplemente se
                # añadiran los demas resultantes de dicha transicion en la misma
                if fila_edo < len(TransicionesAFN):
                    # En caso de que ya exista la lista de estados destinos de una transicion, simplemente se añadiran el resto de estados en
                    # la misma
                    if col_simb < len(TransicionesAFN[fila_edo]):
                        # Para el caso de que la lista de estados destinos de una transicion haya sido rellenada provisionalmente con un error, este se quita
                        if "_err" in TransicionesAFN[fila_edo][col_simb]:
                            TransicionesAFN[fila_edo][col_simb].remove("_err")

                        TransicionesAFN[fila_edo][col_simb].append(aux)
                    # Para el caso de que no se haya creado la lista de estados destinos de una transiciono, se realizara la creacion de dicha lista
                    else:
                        # Para el caso de que se quiera incializar una lista insertando un elemento en una posicion mayor a la de la longitud de la lista,
                        # Phyton automaticamente colocara el item despues del ultimo elemento agregado a la misma para evitar dejar espacios sin información.
                        # Por lo tanto, todos los espacios que esten entre la posicion del último item añadido a la lista y la posicion en la que se desea
                        # colocar el nuevo item se relleneran con un estado de error provisionalmente
                        if col_simb > len(TransicionesAFN[fila_edo]):
                            listaAux2.append("_err") # _err sera el estado de error del AFN
                            for x in range(len(TransicionesAFN[fila_edo]),col_simb):
                                TransicionesAFN[fila_edo].insert(x, listaAux2[:])

                        listaAux2.clear()
                        listaAux2.append(aux)
                        TransicionesAFN[fila_edo].append(listaAux2[:]) # Envia una copia de la listaAux2, para evitar que se modifique dentro de la lista Transiciones
                        listaAux2.clear()

                    # Se realiza el ordenamiento de los estados destino, con el objetivo de llevar un mejor orden y sea mas entendible
                    ##Transiciones[fila_edo][col_simb].sort() ###!!!!!
                    ######print(TransicionesAFN)
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
                    TransicionesAFN.append(listaAux1[:]) # Envia una copia de la listaAux1, para evitar que se modifique dentro de la lista Transiciones
                    listaAux2.clear()
                    listaAux1.clear()
                    ######print(TransicionesAFN)

                # Se resetean las variables utilizadas en el proceso para las transiciones de los estados siguientes
                fila_edo = 0
                col_simb = 0
                aux = ""
                cont_comas = 0
            # En caso de que no se encuente una coma o salto de linea, significa que se esta leyendo un atributo de la tabla de Transiciones
            else:
                aux = aux + i
                #######print(aux)
    # print(TransicionesAFN)

## FUNCION GENERAR AUTOMATA
# Abrirá el archivo de texto que contiene la informacion necesaria para la construccion de un AFN y
# a partir de los datos contenidos en esta generara el AFN
def GenerarAFN():
    global edo_inicialAFN
    global edo_finalAFN

    # Se abre el archivo de texto para su lectura
    f = open("Thompson2.txt", "r")

    # De la primera linea se obtiene la lista de estados que conforman al AFN
    GenerarLista(f.readline(), EstadosAFN)
    # De la segunda linea se obtiene los simbolos que conforman el alfabeto del AFN
    GenerarLista(f.readline(), AlfabetoAFN)

    # De la tercera linea se obtiene el estado incial del AFN
    for i in f.readline():
        if i != "\n":
            edo_inicialAFN = edo_inicialAFN + i
    # Comprobamos que el estado inicial sea un estado valido
    if not (edo_inicialAFN in EstadosAFN):
        print(" !! ERROR: Estado inicial no está en la lista de Estados definida para el AFN")
        exit(1)

    # De la cuarta linea se obtiene el estado final del AFN
    for i in f.readline():
        if i != "\n":
            edo_finalAFN = edo_finalAFN + i
    # Comprobamos que el estado inicial sea un estado valido
    if not (edo_finalAFN in EstadosAFN):
        print(" !! ERROR: Estado final no está en la lista de Estados definida para el AFN")
        exit(1)

    # Del resto de lineas se obtiene la tabla de Transiciones delta
    GenerarTransiciones(f.readlines())

## FUNCION COMPLETAR AUTOMATA
# Genera las transiciones de error faltantes en la tabla de Transiciones, y añade el estado de error a la lista de Estados
# junto a sus respectivas transiciones (todas van a resulktar en estado de error)
def CompletarAFN():
    listaAux = ["_err"]
    listaAux2 = []

    # Bucle que completa las transiciones que van a error en cada estado
    for i in TransicionesAFN:
        if len(i) < len(AlfabetoAFN):
            for j in range(len(i), len(AlfabetoAFN)):
                i.append(listaAux[:])
        else:
            continue

    # Bucle para generar todos los Estados de error para el estado final, en caso de que este no haya sido creado previamenre
    if len(TransicionesAFN) < len(EstadosAFN):
        for i in range (0, len(AlfabetoAFN)):
            listaAux2.append(listaAux)

        TransicionesAFN.append(listaAux2)
        EstadosAFN.append("_err")

    # Para el caso de que se halla añadido un estado de error se añaden sus transiciones
    if len(TransicionesAFN) < len(EstadosAFN):
        TransicionesAFN.append(listaAux2)
    #print(TransicionesAFN)

## FUNCION IMPRIMIR LISTA
# Da formato a la impresion de los elementos de una lista determinada
# Devuelve una cadena con la impresion de los elementos de la lista en dicho formato
def ImprimirLista(lista):
    c = ', '.join(lista)
    return c

## FUNCION IMPRIMIR AUTOMATA
# Imprime cada uno de los elementos de la tupla de un Automata con sus respectivos valores
# Debido a la diferencia en el tipo de dato de la variable de estado final del AFN con respecto a su contraparte en el AFD,
# se incluyo una bandera, que si es True indica que esta imprimiendo el estado final de un AFN, y si es False indica la
# impresion de los estados finales de un AFD
def ImprimirAutomata(estados, alfabeto, edo_inicial, edo_final, transiciones, bandera):
    print(f"\nEstados = ({ImprimirLista(estados)})")
    print(f"Alfabeto = ({ImprimirLista(alfabeto)})")
    print(f"Estado inicial = {edo_inicial}")

    # Para el caso de impresion del estado final del AFN
    if bandera:
        print(f"Estado finale = {edo_final}")
    # Para el caso de impresion de lOS estadoS finalES del AFD
    else:
        print(f"Estados finales = ({ImprimirLista(edo_final)})")

    # Impresion de la tabla de Transiciones
    data = []
    aux = []
    cabecera = alfabeto[:]
    cabecera.insert(0, "Estado")

    for i in range(len(transiciones)):
        aux.append(estados[i])
        for j in range(len(transiciones[i])):
            aux.append(transiciones[i][j])
        data.append(aux[:])
        aux.clear()

    print("Tabla de Transiciones: \n")
    print(tabulate(data, headers = cabecera))

# FUNCION CERRADURA EPSILON
# Realiza la operación de Cerradura epsilon
# Recibe una lista de estados a partir de los cuales se realizara la operacion Cerradura epsilon
def CerraduraEpsilon(edos):
    # Lista de estados resultantes de la operación Cerradura epsilon
    C_epsilon = []
    # Pila de estado auxiliar
    pilaAux = []
    # Se guardan los estados recibidos en una pila auxiliar
    pilaAux = edos.copy()
    # Se guardan los estados recibidos en la lista de estados resultantes en la Cerradura Epsilon
    C_epsilon = edos.copy()

    while len(pilaAux) != 0:
        # Se extrae un estado de la pila auxiliar
        q = pilaAux.pop()

        # Si el estado obtenido de la pila auxiliar no esta en la lista de la Cerradura Epsilon, se agrega a esta
        if not(q in C_epsilon):
            C_epsilon.append(q)
        # Si los estados resultantes de la transicion del estado obtenido de la pila auxiliar con epsilon no es un estado error,
        # se añade a la pila auxiliar para su posterior evaluacion
        if not('_err' in TransicionesAFN[EstadosAFN.index(q)][AlfabetoAFN.index('E')]):
            pilaAux = pilaAux + TransicionesAFN[EstadosAFN.index(q)][AlfabetoAFN.index('E')]

    # Se ordena y retorna la lista de estados resultantes de la operacion Cerradura epsilon
    C_epsilon.sort()
    return C_epsilon

# FUNCION MOVER
# Realiza la operación de Mover
# Recibe una lista de estados a partir de los cuales se realizara la operacion Mover, y el simbolo con el que debe cumplirse
# la transicion
def Mover(edos, simbolo):
    # Lista de estados resultantes de la operación Mover
    mover = []
    # Pila de estado auxiliar
    pilaAux = []
    # Se guardan los estados recibidos en una pila auxiliar
    pilaAux = edos.copy()

    while len(pilaAux) != 0:
        # Se extrae un estado de la pila auxiliar
        q = pilaAux.pop()

        # Si el estado resultante de la transicion del estado obtenido de la pila auxiliar con el simbolo a evaluar
        # no es un estado error, se añade a la lista de la operación Mover
        if not ('_err' in TransicionesAFN[EstadosAFN.index(q)][AlfabetoAFN.index(simbolo)]):
            mover = mover + TransicionesAFN[EstadosAFN.index(q)][AlfabetoAFN.index(simbolo)]

    # Se odena y retorna la lista de estados resultantes de la operacion Mover
    mover.sort()
    return mover

# FUNCION CONVERTIR AFN-epsilon a AFD
# Realiza la conversion de un AFN con transiciones epsilon en un AFD auxiliandose de la operacion Ir_A, impliciyta en la
# funcion, y que a su vez hace uso de las operaciones Cerradura epsilon y Mover. De igual manera genera los elementos del
# AFD resultante (Estados, Alfabeto, estado inicial, estados finales y Tarnsiciones)
def Convertir_AFNe_AFD():
    # Lista Auxiliar que servira para determinar si un estado se repite durante la generación de los estados del AFD
    Edos_CerrEpsilon = {}
    # Lista que almacena todas las letras en mayuscula de la A a la Z. Esta lista servira para poder asignar de manera
    # más rápida los nombres de cada uno de los estados generados para el AFD sin contar el estado de error
    Letras = list(string.ascii_uppercase)
    # Listas auxiliares para el guardado temporal de datos
    mover = []
    transiciones = []
    # Bandera que determina si algun estado del AFD generado apunta a un estado de error
    error = False
    # Bandera que determina si aun existen estados a evaluar durante el proceso de generacion del AFD o no
    hasNext = True
    # Contadores auxiliares
    keyNumber = 0
    cont = 0

    # Se copia cada uno de los simbolos del Alfabeto del AFN en el Alfabeto del AFD con la exceocion del epsilon (E)
    for i in AlfabetoAFN:
        if i == 'E':
            continue;
        else:
            AlfabetoAFD.append(i)

    # Se obtiene la Cerradura Epsilon del estado inicial del AFN, y el resultado de dicha operación se le asigna al estado A
    Edos_CerrEpsilon[Letras[0]] = [edo_inicialAFN]
    EstadosAFD[Letras[0]] = CerraduraEpsilon([edo_inicialAFN])

    # Si dentro de los estados resultantes de la Cerradura Epsilon del estado inicial del AFN, se encuentra el estado final
    # del mismo AFN, se agrega el estado A a la lista de estados finales del AFD
    if edo_finalAFN in EstadosAFD[Letras[0]]:
        Edos_finalesAFD.append(Letras[0])

    # print(Edos_CerrEpsilon)
    # print(EstadosAFD)

    # Este ciclo implicitamente es la operacion Ir_A, dentro del cual se evaluara cada uno de los estados que sean generados
    # para el AFD con cada uno de los simboplos presentes dentro del Alfabeto del AFD, obtenido previamenre en la funcion
    while hasNext:
        for i in AlfabetoAFD:
            # Se realiza la operacion Mover, mandando la lista de estados del AFN contenidos dentro de cada estado del AFD
            # para su evaluación con cada uno de los simbolos presentes en el Alfabeto del AFD
            mover = Mover(EstadosAFD[Letras[keyNumber]], i).copy()

            # En el caso de que la operación Mover devuelva una cadena vacía
            if len(mover) == 0:
                # La bandera de error pasa a tener un valor de True
                error = True
                # El resultado de la transicion del estado que este siendo evaluado con su respectivo simbolo sera un
                # estado vacio, representado dentro de este algoritmo como un estado de error
                transiciones.append('_err')
            # En el caso de que la operación Mover devuelva una cadena que ya haya sido previamente evaluada
            elif mover in Edos_CerrEpsilon.values():
                # En este caso, se debe determinar a cual de los estados que ya han sido generado con anterioridad para
                # el AFD le pertenece la cadena devuelta por la operación Mover. Esto se realiza buscando la llave (estado)
                # que contenga dicha cadena
                key_list = list(Edos_CerrEpsilon.keys())
                val_list = list(Edos_CerrEpsilon.values())
                posicion = val_list.index(mover)
                # El resultado de la transicion del estado que este siendo evaluado con su respectivo simbolo sera
                # el del estado obtenido en la busqueda previamente realizada.
                transiciones.append(key_list[posicion])
            # En el caso de que la operación Mover devuelva una cadena que aun no ha sido previamente evaluada
            else:
                # Se obtiene la Cerradura Epsilon de la cadena de estados resultante de la operación Mover, y el resultado
                # de dicha operación se le asigna a un nuevo estado para el AFD
                cont += 1
                Edos_CerrEpsilon[Letras[cont]] = mover
                EstadosAFD[Letras[cont]] = CerraduraEpsilon(mover)
                # El resultado de la transicion del estado que este siendo evaluado con su respectivo simbolo sera
                # el del nuevo estado generado para el AFD
                transiciones.append(Letras[cont])
                # print(Edos_CerrEpsilon)
                # print(EstadosAFD)

                # Si dentro de los estados resultantes de la Cerradura Epsilon de la cadena de estados resultante de la
                # operación Mover, se encuentra el estado final del AFN, se agrega el estado generado a la lista de estados finales del AFD
                if edo_finalAFN in EstadosAFD[Letras[cont]]:
                    Edos_finalesAFD.append(Letras[cont])

        TransicionesAFD.append(transiciones[:])
        transiciones.clear()

        if keyNumber == cont:
            hasNext = False
        keyNumber += 1

    # En caso de que la bandera de error sea True; lo cual indica que alguna transicion de los estados del AFD resulta en un estado vacio o de error
    if error:
        # Se añaden las transiciones del estado de error con cada uno de los simbolos del Alfabeto del AFD. El resultado de todas estas transiciones
        # resultan en el mismo estado de error
        for i in range (len(AlfabetoAFD)):
            transiciones.append('_err')

        # Se añade el estado de error a la lista de Estados del AFD. 
        EstadosAFD['err'] = None
        TransicionesAFD.append(transiciones[:])
        transiciones.clear()

def main():
    print("---------- AFN epsilon FORMALIZADO ----------")
    GenerarAFN()
    CompletarAFN()
    ImprimirAutomata(EstadosAFN, AlfabetoAFN, edo_inicialAFN, edo_finalAFN, TransicionesAFN,1)

    Convertir_AFNe_AFD()
    print("\n---------- AFD FORMALIZADO ----------")
    ImprimirAutomata(list(EstadosAFD.keys()), AlfabetoAFD, list(EstadosAFD.keys())[0], Edos_finalesAFD, TransicionesAFD, 0)

# Ejecutamos la funcion main
if __name__ == '__main__':
    main()