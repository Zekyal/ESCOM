#include <stdio.h>
#include <stdlib.h>
#include "Tabla_Simbolos.h"


int main(){
	tabla t;
	Inicializar_Tabla(&t);
	Declaracion_variable(&t, "entero", 1, "34");
	Declaracion_variable(&t, "decimal", 2, "6.6666");
	Declaracion_variable(&t, "cadena", 3, "Argentina es un pais de Australia");
	Declaracion_variable(&t, "valor", 1, "74");
	Declaracion_variable(&t, "g", 2, "89.7564857");
	Declaracion_variable(&t, "txt", 3, "Ucrania");
	Imprimir_Tabla(&t);
	printf("%d\n", Tipo_Dato(&t, "valor"));
	printf("%d\n", Tipo_Dato(&t, "txt"));
	printf("%d\n", Tipo_Dato(&t, "decimal"));
	printf("%d\n", Tipo_Dato(&t, "var"));
	Asignacion_variable(&t, "valor", 1, "2");
	Asignacion_variable(&t, "g", 2, "3.4");
	Asignacion_variable(&t, "txt", 3, "Albania");
	Imprimir_Tabla(&t);
	Destruir_Tabla(&t);
	Imprimir_Tabla(&t);
	Declaracion_variable(&t, "valor", 1, "74");
	Imprimir_Tabla(&t);
}