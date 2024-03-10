#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// Estructura de la Tabla de Simbolos
typedef struct{
	char* id;		// Nombre de la Variable
	/*
		1. Tipo de dato Entero
		2. Tipo de dato Double
		3. Tipo de dato String
	*/
	int tipo_dato;	// Tipo de Dato
	int entero;		// Almacena un valor entero para la variable
	double decimal;	// Almacena un valor decimal para la variable
	char* cadena_texto;	// Almacena una cadena de texto para la variable
}Tabla;

Tabla t[150];
int size_tabla = 0;	// Tamaño de la Tabla de Simbolos (total de variables en la Tabla)

void Declaracion_entero(char*, int);
void Declaracion_decimal(char*, double);
void Declaracion_cadena(char*, char*);
bool Busqueda_variable(char*);
void Imprimir_Tabla();

void Declaracion_entero(char* variable, int valor){
	if(!Busqueda_variable(variable)){
		t[size_tabla].id = strdup(variable);
		t[size_tabla].tipo_dato = 1;
		t[size_tabla].entero = valor;
		t[size_tabla].decimal = 0.0;
		t[size_tabla].cadena_texto = "";
		size_tabla++;
	}

}

void Declaracion_decimal(char* variable, double valor){
	if(!Busqueda_variable(variable)){
		t[size_tabla].id = strdup(variable);
		t[size_tabla].tipo_dato = 2;
		t[size_tabla].entero = 0;
		t[size_tabla].decimal = valor;
		t[size_tabla].cadena_texto = "";
		size_tabla++;
	}
}

void Declaracion_cadena(char* variable, char* valor){
	if(!Busqueda_variable(variable)){
		t[size_tabla].id = strdup(variable);
		t[size_tabla].tipo_dato = 3;
		t[size_tabla].entero = 0;
		t[size_tabla].decimal = 0.0;
		t[size_tabla].cadena_texto = strdup(valor);
		size_tabla++;
	}
}

bool Busqueda_variable(char* variable){
	if(size_tabla != 0){
		for(int i = 0; i <= size_tabla-1; i++){
			if(strcmp(t[i].id, variable) == 0)
				return true;	
			return false;
		}
	}
	else{
		return false;
	}
}

void Imprimir_Tabla(){
	int i = 0, j = 0;

	for(i = 0; i < 39; i++){
		printf("=");
	}
	printf("=\n");

	printf("|          TABLA DE SIMBOLOS           |\n");

	for(i = 0; i < 39; i++){
		printf("=");
	}
	printf("=\n");

	for(i = 0; i <= size_tabla-1; i++){
		printf("| NOMBRE       | %s", t[i].id);

		for(j=0; j < 21-strlen(t[i].id); j++)
			printf(" ");
		printf(" |\n");

		printf("| TIPO DE DATO | ");

		if(t[i].tipo_dato == 1){
			char aux [50];
			
			printf("int                   | \n");
			printf("| VALOR        | %d", t[i].entero);
			sprintf(aux, "%d", t[i].entero);

			for(j=0; j < 21-strlen(aux); j++)
				printf(" ");
			printf(" |\n");
		}
		else if(t[i].tipo_dato == 2){
			printf("double                | \n");
			printf("| VALOR        | %f", t[i].decimal);

			for(j=0; j < 21-sizeof(t[i].decimal); j++)
				printf(" ");
			printf(" |\n");
		}
		else if(t[i].tipo_dato == 3){
			printf("char                  | \n");
			printf("| VALOR        | %s", t[i].cadena_texto);

			for(j=0; j < 21-strlen(t[i].cadena_texto); j++)
				printf(" ");
			printf(" |\n");
		}

		for(j = 0; j < 39; j++){
			printf("-");
		}
		printf("-\n");
	}
}

int main(){
	Declaracion_entero("entero", 64);
	Declaracion_decimal("decimal", 6.6666);
	Declaracion_cadena("cadena", "Corea del Sur owo");
	Imprimir_Tabla();
}