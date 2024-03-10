/*
	----- ESTRUCTURA DE DATOS PARA UNA TABLA DE SIMBOLOS -----

	-> DESCRIPCION: Estructura de datos basada en una Lista Doblemente Ligada, la cual
	consiste en un arreglo lineal de nodos, dentro de los cuales se almacenan los datos
	de las variables (nombre de la variable, tipo de dato y valor ya sea entero, 
	flotante o string) que sean declaradas en un Intèrprete simulando asi cada una de 
	las filas que conforman la Tabla de SImbolos. Adicionaklmente cada nodo cuenta con
	dos apuntadores hacia los elementos posteriores y anteriores a cada uno de los nodos
	para facilitar la consulta de los mismos.

		    ********    ********    ********           ********    
	NULL <- *	   * <- *	   * <- *	   * <-     <- *	  * 
			* VAR1 *	* VAR2 *	* VAR3 *    ...    * VARn *
			*	   * -> *	   * -> *	   * ->     -> *	  * -> NULL
			********	********	********	       ********
*/

/* ----- DEFINICIONES DE CONSTANTES ----- */
#define TRUE 1
#define FALSE 0

/* ----- DEFINICIONES DE TIPOS DE DATO ----- */

// Definicion de boolean (modelado con un "char")
typedef unsigned char boolean;

/* 	
	Estructura para almacenar el valor de una variable, independientemente del tipo
	de dato aceptado por el Interprete de la variable.
*/
typedef struct valor{
	int entero;		// Almacena un valor entero para la variable
	double decimal;	// Almacena un valor decimal para la variable
	char* cadena_texto;	// Almacena una cadena de texto para la variable
}valor;

/* 	
	Estructura para almacenar los datos de una variable. Dichos datos son el nombre de
	la variable, el tipo de dato de la variable y el valor almacenado en la variable.
*/
typedef struct variable{
	char* id;		// Nombre de la Variable
	/*
		1. Tipo de dato Entero
		2. Tipo de dato Double
		3. Tipo de dato String
	*/
	int tipo_dato;	// Tipo de Dato
	valor val;
}variable;

/* 	
	Estructura de un nodo de la Tabla de Simbolos. Dentro de esta se almacena la
	estructura que guarda los datos de una variable y dos apuntadores hacia el nodo 
	siguiente y previo de la lista.
*/
typedef struct nodo{
	variable var;
	struct nodo *next;
	struct nodo *previous;
}nodo;

// Definicion de fila como un apuntador a nodo (Un nodo representa una fila de la Tabla)
typedef nodo* fila;

/* 
	Estructura de la Tabla de Simbolos. Contiene un apuntados al primer y ultimo nodo de 
	la tabla (o la primera y ultima fila de la misma), y un contador que indica cuantos 
	nodosa o filas tiene la misma
*/
typedef struct tabla{
	int size_tabla;
	fila fila_inicial;
	fila fila_final;
}tabla;

/* ----- DECLARACION DE FUNCIONES  ----- */
void Inicializar_Tabla(tabla *t);
void Destruir_Tabla(tabla *t);
void Declaracion_variable(tabla *t, char *nombre, int tipo, char* valor);
void Asignacion_variable(tabla *t, char *variable, int tipo, char* valor);
fila Busqueda_Variable(tabla *t, char *variable);
int Tipo_Dato(tabla *t, char *variable);
//struct fila * Expresion_Variable (tabla *t, char *variable);
//char* Imprimir_Variable(tabla *t, struct fila *fila_variable);
void Imprimir_Tabla(tabla *t);