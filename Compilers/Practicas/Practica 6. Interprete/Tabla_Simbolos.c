/* ----- LIBRERIAS ----- */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Tabla_Simbolos.h"

/* ----- DEFINICION DE FUNCIONES ----- */

/*
	FUNCION INCIALIZAR TABLA
	
	-> Descripcion: Inicializa una Tabla de Simbolos.
	-> Recibe: Un apuntador a una tabla *t
*/
void Inicializar_Tabla(tabla *t){
	t->fila_inicial = NULL;
	t->fila_final = NULL;
	t->size_tabla = 0;
	//printf("Tabla Incializada...\n");
}


/*
	FUNCION DESTRUIR TABLA
	
	-> Descripcion: Destruye una Tabla de Simbolos eliminando todos los nodos de variables 
	contenidos.
	-> Recibe: Un apuntador a una tabla *t
*/
void Destruir_Tabla(tabla *t){
	nodo *aux; 	// Apuntador auxiliar a un nodo

	// Mientras el nodo inicial de la tabla no sea NULL
	while(t->fila_inicial != NULL){
		aux = t->fila_inicial;	// Se obtiene la memoria del primer nodo de la tabla
		// Se establece el siguiente nodo al primero, como el primer nodo
		t->fila_inicial = t->fila_inicial->next;
		free(aux);	// Se libera la memoria del primer nodo de la tabla
	}

	t->fila_final = NULL;
	t->size_tabla = 0;
	//printf("Tabla Destruida...\n");
}

/*
	FUNCION DECLARACION VARIABLE

	-> Descripcion: Realiza la creacion de una nueva variable, la cual ha sido declarada en
	el Intèrprete, para realizar posteriormente su guardado en la Tabla de Simbolos.
	-> Recibe: Un apuntador a una tabla *t, una cadena de texto con el nombre de la nueva 
	variable, un entero que indica el tipo de dato de la variable y una cadena de texto 
	con el valor que sera almacenada en la variable.
*/
void Declaracion_variable(tabla *t, char *nombre, int tipo, char* valor){
	variable var;
	// Se almacena el nombre y tipo de la variable dentro de su respectiva estructura de datos
	var.id = strdup(nombre);
	var.tipo_dato = tipo;

	// Dependiendo del tipo de dato de la variable, se determina si el valor a almacenar sera
	// guardado como entero, flotante o string   
	if(tipo == 1)	// En caso de que la variable sea de tipo entero
		var.val.entero = atoi(valor);
	if(tipo == 2)	// En caso de que la variable sea de tipo flotante
		var.val.decimal = strtod(valor, NULL);
	if(tipo == 3)	// En caso de que la variable sea de tipo string
		var.val.cadena_texto = strdup(valor);

	// Verifica que la funcion no haya sido declarada anteriormente buscandola en la tabla
	if(Busqueda_Variable(t, nombre) == NULL){	// En caso de que la variable no este en la tabla
		// Se crea un nuevo nodo para el almacenamiento de la nueva variable en la Tabla de Simbolos
		fila aux;	
		aux = malloc(sizeof(nodo));

		// En caso de que no se pueda reservar memoria para el nuevo nodo se manda un error
		if(aux == NULL){
			printf("\n\n***ERROR: No se puede crear un nuevo espacio en la Tabla de Simbolos");
			exit(1);
		}

		aux->var = var;	// Se almacena la variable dentro del nodo creado

		// En caso de que la tabla este vacia la momento de la creacion del nuevo nodo
		if(t->size_tabla == 0){
			// Se generan los apuntadores hacia el nodo previo y siguiente al del nuevo nodo
			// En este casio, al ser que la tabla esta vaccia ambos apuntan a NULL
			aux->next = NULL;
			aux->previous = NULL;
			// Se establece el nuevo nodo como la fila tanto inicial como final de la tabla
			t->fila_inicial = aux;
			t->fila_final = aux;
		}
		// En caso de que la tabla NO este vacia la momento de la creacion del nuevo nodo
		else{
			// Se establece el neuvo nodo, como el nodo siguiente al ultimo nodo que haya sido
			// agregado en la Tabla de Simbolos
			t->fila_final->next = aux;
			// Se generan los apuntadores hacia el nodo previo y siguiente al del nuevo nodo
			aux->previous = t->fila_final;
			aux->next = NULL;
			// Se establece el nuevo nodo como la fila final de la tabla
			t->fila_final = aux;
		}

		t->size_tabla++;	// Se incrementa en uno el tamaño de la tabla
	}
	else{	// En caso de que la varibale sea encontrada en la tabla
		printf("ERROR: Variable %s ya ha sido declarada previamente\n", var.id);
	}
}

/*
	FUNCION DECLARACION VARIABLE

	-> Descripcion: Realiza la asigncion de un valor a alguna de las variables existentes 
	contenidas en la Tabla de Simbolos.
	-> Recibe: Un apuntador a una tabla *t, una cadena de texto con el nombre de la 
	variable a la cual se le sera asignada el valor en cuestion, un entero que indica el 
	tipo de dato de la variable y una cadena de texto con el valor que sera almacenado.
*/
void Asignacion_variable(tabla *t, char *variable, int tipo, char* valor){
	// Se realiza la busqueda del nodo donde se encuentra guardada la variable a la cual
	// le serà asignada un valor. El apuntador a dicho nodo se guardara en aux
	fila aux = Busqueda_Variable(t, variable);

	// EN caso de que la variable haya sido encontrada en la Tabla de Simbolos
	if(aux != NULL){	
		// Dependiendo del tipo de dato de la variable, se determina si el valor a
	    // almacenar sera guardado como entero, flotante o string  
		if(tipo == 1)	// En caso de que la variable sea de tipo entero
			aux->var.val.entero = atoi(valor);
		if(tipo == 2)	// En caso de que la variable sea de tipo flotante
			aux->var.val.decimal = strtod(valor, NULL);
		if(tipo == 3)	// En caso de que la variable sea de tipo string
			aux->var.val.cadena_texto = strdup(valor);
	}
	// En caso de que la variable NO haya sido encontrada en la Tabla de Simbolos
	else{
		printf("ERROR: Variable %s no ha sido inicializada\n", variable);
	}
}

/*
	FUNCION BUSQUEDA VARIABLE

	-> Descripcion: Realiza la busqueda de alguna variable dentro de la Tabla de Simbolos,
	y en caso de ser encontrada, la devuelve.
	-> Recibe: Un apuntador a una tabla *t y una cadena de texto con el nombre de la
	variable a buscar.
	-> Devuelve:
		NULL -> Si la variable NO esta dentro de la Tabla.
		Un apuntador aux hacia el nodo en donde se encuentra la variable -> Si la variable
		esta dentro de la Tabla.
*/
fila Busqueda_Variable(tabla *t, char *variable){
	// Auxiliares que se emplearan para realizar el recorrido de cada uno de los nodos de
	// la Tabla de Simbolos.
	fila aux1 = t->fila_inicial;	// Recorre iniciando en el primer nodo de la tabla
	fila aux2 = t->fila_final;		// Recorre iniciando en el ultimo nodo de la tabla
	// Operacion para determinar cuantas iteraciones se haran para recorrer todos los
	// nodos almacenados en la tabla
	int aux = (t->size_tabla/2) + (t->size_tabla %2);

	// Si la tabla no està vacìa
	if(t->size_tabla !=0){
		for(int i=0; i<aux; i++){
			// Si la variable es encontrada por el auxiliar, se devuelve dicho auxiliar
			if(strcmp(aux1->var.id, variable)==0)
				return aux1;
			// En caso contrario se accede al nodo siguiente del auxiliar
			aux1 = aux1->next;

			// Si la variable es encontrada por el auxiliar, se devuelve dicho auxiliar
			if(strcmp(aux2->var.id, variable)==0)
				return aux2;
			// En caso contrario se accede al nodo anterior del auxiliar
			aux2 = aux2->previous;
		}
	}

	// Si no se encuentrala variable dentro de la tabla, se devuelve NULO
	return NULL;
}

/*
	FUNCION TIPO DATO

	-> Descripcion: Realiza la busqueda de alguna variable dentro de la Tabla de Simbolos,
	y en caso de ser encontrada, devuelve el tipo de dato de la variable.
	-> Recibe: Un apuntador a una tabla *t y una cadena de texto con el nombre de la
	variable de la que se desee conocer su tipo de dato.
	-> Devuelve:
		0 -> Si la variable NO esta dentro de la Tabla.
		Tipo de dato de la variable -> Si la variable esta dentro de la Tabla.
*/
int Tipo_Dato(tabla *t, char *variable){
	// Se realiza la busqueda del nodo donde se encuentra guardada la variable de la cual
	// se desea conocer su tipo de dato. El apuntador a dicho nodo se guardara en aux
	fila aux = Busqueda_Variable(t, variable);

	// En caso de que la variable sea encontrada, se devuelve el tipo de dato de la misma
	if(aux != NULL){
		return aux->var.tipo_dato;
	}
	// En caso contrario se devuelve 0
	else{
		printf("ERROR: Variable %s no ha sido inicializada\n", variable);
		return 0;
	}
}

/*
	FUNCION IMPRIMIR TABLA

	-> Descripcion: Imprime la Tabla de Simbolos para su visualizacion graficamente.
	-> Recibe: Un apuntador a una tabla *t.
*/
void Imprimir_Tabla(tabla *t){
	/* ----- Declaracion de Variables Auxiliares ----- */
	int i = 0;
	fila aux = t->fila_inicial;
	char buffer[50];

	/* ----- Impresion de la Cabecera ----- */
	for(i = 0; i < 49; i++){
		printf("=");
	}
	printf("=\n");

	printf("|               TABLA DE SIMBOLOS                |\n");

	for(i = 0; i < 49; i++){
		printf("=");
	}
	printf("=\n");

	/* ----- Impresion de los Elementos de la Tabla  ----- */
	// Siempre y cuando el apuntador auxiliar no apunte a un nulo
	while(aux != NULL){
		/* --- Impresion del Nombre de la variable --- */
		printf("| NOMBRE       | %s", aux->var.id);

		for(i=0; i < 31-strlen(aux->var.id); i++)
			printf(" ");
		printf(" |\n");

		/* --- Impresion del Tipo de Dato y Valor de la variable --- */
		printf("| TIPO DE DATO | ");
		
		if(aux->var.tipo_dato == 1){	// En caso de que la variable sea de tipo int
			sprintf(buffer, "%d", aux->var.val.entero);
			printf("int                             | \n");
			printf("| VALOR        | %d", aux->var.val.entero);

			for(i=0; i < 31-strlen(buffer); i++)
				printf(" ");
			printf(" |\n");
		}
		if(aux->var.tipo_dato == 2){	// En caso de que la variable sea de tipo double
			sprintf(buffer, "%lf", aux->var.val.decimal);
			printf("double                          | \n");
			printf("| VALOR        | %lf", aux->var.val.decimal);

			for(i=0; i < 31-strlen(buffer); i++)
				printf(" ");
			printf(" |\n");
		}
		if(aux->var.tipo_dato == 3){	// En caso de que la variable sea de tipo string
			printf("char                            | \n");
			
			if(strlen(aux->var.val.cadena_texto) > 31){
				printf("| VALOR        | %s |\n", aux->var.val.cadena_texto);
			}
			else{
				printf("| VALOR        | %s", aux->var.val.cadena_texto);

				for(i=0; i < 31-strlen(aux->var.val.cadena_texto); i++)
					printf(" ");
				printf(" |\n");
			}
		}

		for(i = 0; i < 49; i++){
			printf("-");
		}
		printf("-\n");

		// El apuntador auxiliar, apunta la nodo siguiente
		aux = aux->next;
	}
}