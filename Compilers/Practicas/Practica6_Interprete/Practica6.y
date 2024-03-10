/* 
	Compilacion:
		-flex Practica6.l
		-bison Practica6.y -d
		-gcc lex.yy.c Practica6.tab.c Tabla_Simbolos.c-lm
*/

/* --- Declaracion de Bibliotecas de C +++ */
%{
	#include <stdio.h>
	#include <stdlib.h>
	#include <math.h>
	#include <string.h>
	#include "Tabla_Simbolos.h"

	/* Variables auxiliares */
	tabla t;	// Declaracion de la tabla de Simbolos
	char buffer[50];	// Auxiliar para almacenar vcalores de variables
	int tipo;	//AUciliar para almacenar el tipo de dato de variables

	/* Mensajes de error */
	char* err_int_string = "Variable de tipo \"int\" requiere de valor de tipo entero, pero esta recibiendo un valor de tipo \"string\"\n";
	char* err_double_string = "Variable de tipo \"double\" requiere de valor de tipo decimal, pero esta recibiendo un valor de tipo \"string\"\n";
	char* err_string_int = "Variable de tipo \"string\" requiere de una cadena de texto, pero esta recibiendo un valor de tipo \"int\"\n";
	char* err_string_double = "Variable de tipo \"string\" requiere de una cadena de texto, pero esta recibiendo un valor de tipo \"double\"\n";
	char* err_opint_string = "Operacion de tipo \"int\" requiere de valores enteros, pero esta recibiendo un valor de tipo \"string\"\n";
	char* err_opdouble_string = "Operacion de tipo \"doubke\" requiere de valores enteros o decimales, pero esta recibiendo un valor de tipo \"string\"\n";
	char* err_pow_string = "Operacion POW con valo de tipo \"string\", requieren de un valor de tipo \"int\" como expoente\n";

	/* Declaracion de Funciones */
	char* Potencia_Cadena(char*, int);
	char* Invertir_Cadena(char*);
%}

/* --- Declaraciones de BISON ---*/
%union{
	int entero;
	double decimal;
	char* cadena;
}

/* Definicion de Tokens */
%token <entero> ENTERO
%token <decimal> DECIMAL 
%token <cadena> CADENA
%token <cadena> VARIABLE
%token INT DOUBLE STRING
%token POW

/* Definicion de No Terminales */
%type <entero> ent
%type <entero> expe
%type <decimal> dec
%type <decimal> expd
%type <cadena> expc

/* Precedencia de Operaciones */
%right '='
%left '+' '-'
%left '*' '/' '%'
%left NEGATIVO POSITIVO 	// Para Numeros enteros y decimales con signo
%left POW

/* --- Gramatica ---*/
%%

input:	/* Cadena Vacia*/
		| input line
;

line: 	'\n' 	{printf("Salto de Linea");}
	/* --- Definicion de expresiones --- */
		| expe '\n'	{printf("\n\t->Resultado: %d\n\n", $1);}
		| expd '\n'	{printf("\n\t->Resultado: %f\n\n", $1);}
		| expc '\n'	{printf("\n\t->Resultado: %s\n\n", $1);}
	/* --- Declaracion de variables nuevas SIN asignacion de valor --- */
		| INT VARIABLE ';' '\n'		{
										Declaracion_variable(&t, $2, 1, "0"); 
										Imprimir_Tabla(&t);
									}
		| DOUBLE VARIABLE ';' '\n'	{
										Declaracion_variable(&t, $2, 2, "0.0"); 
										Imprimir_Tabla(&t);
									}
		| STRING VARIABLE ';' '\n'	{
										Declaracion_variable(&t, $2, 3, "(null)"); 
										Imprimir_Tabla(&t);
									}
	/* --- Declaracion de variables nuevas CON asignacion de valor --- */
		/* --- Asignacion de Variables ENTERAS --- */
		| INT VARIABLE '=' expe ';'	'\n'	{
												sprintf(buffer, "%d", $4); 
												Declaracion_variable(&t, $2, 1, buffer);
												Imprimir_Tabla(&t);
											}
		| INT VARIABLE '=' expd ';'	'\n'	{
												sprintf(buffer, "%lf", $4);
												Declaracion_variable(&t, $2, 1, buffer);
												Imprimir_Tabla(&t);
											}
		/* --- Asignacion de Variables DECIMALES --- */
		| DOUBLE VARIABLE '=' expd ';' '\n'	{
												sprintf(buffer, "%lf", $4); 
												Declaracion_variable(&t, $2, 2, buffer); 
												Imprimir_Tabla(&t);
											}
		| DOUBLE VARIABLE '=' expe ';' '\n'	{
												sprintf(buffer, "%d", $4); 
												Declaracion_variable(&t, $2, 2, buffer); 
												Imprimir_Tabla(&t);
											}
		/* --- Asignacion de Variables STRING --- */									
		| STRING VARIABLE '=' expc ';' '\n'	{	
												Declaracion_variable(&t, $2, 3, $4); 
												Imprimir_Tabla(&t);
											}
		/* --- Errores de asignacion --- */
		| INT VARIABLE '=' expc ';'	'\n'	{	yyerror (err_int_string);	}
		| DOUBLE VARIABLE '=' expc ';' '\n'	{	yyerror (err_double_string);	}
		| STRING VARIABLE '=' expe ';' '\n'	{	yyerror (err_string_int);	}
		| STRING VARIABLE '=' expd ';' '\n'	{	yyerror (err_string_double);	}
	/* --- Asignacion de valores --- */
		| VARIABLE '=' expe ';' '\n'	{
											tipo = Tipo_Dato(&t, $1);
											if (tipo ==1 || tipo == 2){
												sprintf(buffer, "%d", $3);
												Asignacion_variable(&t, $1, tipo, buffer);
												Imprimir_Tabla(&t);
											}
											if (tipo == 3)
												yyerror(err_string_int);
										}
		| VARIABLE '=' expd ';' '\n'	{
											tipo = Tipo_Dato(&t, $1);
											if (tipo ==1 || tipo == 2){
												sprintf(buffer, "%lf", $3); 
												Asignacion_variable(&t, $1, tipo, buffer);
												Imprimir_Tabla(&t);
											}
											if (tipo == 3)
												yyerror(err_string_double);
										}
		| VARIABLE '=' expc ';' '\n'	{
											tipo = Tipo_Dato(&t, $1);
											if (tipo ==1)
												yyerror(err_int_string);
											if (tipo == 2)
												yyerror(err_double_string);
											if (tipo == 3){
												Asignacion_variable(&t, $1, tipo, $3);
												Imprimir_Tabla(&t);
											}
										}												
		// FALTA ASIGNAR VALORES DE OTRAS VARIABLES A UNA VARIABLE
;

/* --- OPERACIONES CON NUMEROS ENTEROS --- */
expe:	ent		{$$ = $1;}
		| expe '+' expe 	{$$ = $1 + $3;}
		| expe '-' expe 	{$$ = $1 - $3;}
		| expe '*' expe 	{$$ = $1 * $3;}
		| expe '/' expe 	{$$ = $1 / $3;}
		| expe '%' expe 	{$$ = $1 % $3;}
	/* --- Definicion de Numeros Enteros con signo --- */
		| '-' expe %prec NEGATIVO	{$$ = -$2;}
		| '+' expe %prec POSITIVO	{$$ = +$2;}
	/* --- Definicion de funcion Potencia --- */
		| POW '(' expe ',' expe ')'	{$$ = pow($3, $5);}
	/* --- Errores --- */
		| expe '+' expc 	{yyerror(err_opint_string);}
		| expe '-' expc 	{yyerror(err_opint_string);}
		| expe '*' expc 	{yyerror(err_opint_string);}
		| expe '/' expc 	{yyerror(err_opint_string);}
		| expe '%' expc 	{yyerror(err_opint_string);}
		| expc '+' expe 	{yyerror(err_opint_string);}
		| expc '-' expe 	{yyerror(err_opint_string);}
		| expc '*' expe 	{yyerror(err_opint_string);}
		| expc '/' expe 	{yyerror(err_opint_string);}
		| expc '%' expe 	{yyerror(err_opint_string);}
		| POW '(' expe ',' expc ')'	{yyerror(err_opint_string);}
;

/* --- OPERACIONES CON NUMEROS DECIMALES --- */
expd:	dec 	{$$ = $1;}
		| expd '+' expd 	{$$ = $1 + $3;}
		| expd '-' expd 	{$$ = $1 - $3;}
		| expd '*' expd 	{$$ = $1 * $3;}
		| expd '/' expd 	{$$ = $1 / $3;}
		| expd '%' expd 	{$$ = fmod($1, $3);}
		| expd '+' expe 	{$$ = $1 + $3;}
		| expd '-' expe 	{$$ = $1 - $3;}
		| expd '*' expe 	{$$ = $1 * $3;}
		| expd '/' expe 	{$$ = $1 / $3;}
		| expd '%' expe 	{$$ = fmod($1, $3);}
		| expe '+' expd 	{$$ = $1 + $3;}
		| expe '-' expd 	{$$ = $1 - $3;}
		| expe '*' expd 	{$$ = $1 * $3;}
		| expe '/' expd 	{$$ = $1 / $3;}
		| expe '%' expd 	{$$ = fmod($1, $3);}
	/* --- Definicion de Numeros Decimales con signo --- */
		| '-' expd %prec NEGATIVO	{$$ = -$2;}
		| '+' expd %prec POSITIVO	{$$ = +$2;}
	/* --- Definicion de funcion Potencia --- */
		| POW '(' expd ',' expd ')'	{$$ = pow($3, $5);}
		| POW '(' expd ',' expe ')'	{$$ = pow($3, $5);}
		| POW '(' expe ',' expd ')'	{$$ = pow($3, $5);}
	/* --- Errores --- */
		| expd '+' expc 	{yyerror(err_opdouble_string);}
		| expd '-' expc 	{yyerror(err_opdouble_string);}
		| expd '*' expc 	{yyerror(err_opdouble_string);}
		| expd '/' expc 	{yyerror(err_opdouble_string);}
		| expd '%' expc 	{yyerror(err_opdouble_string);}
		| expc '+' expd 	{yyerror(err_opdouble_string);}
		| expc '-' expd 	{yyerror(err_opdouble_string);}
		| expc '*' expd 	{yyerror(err_opdouble_string);}
		| expc '/' expd 	{yyerror(err_opdouble_string);}
		| expc '%' expd 	{yyerror(err_opdouble_string);}
		| POW '(' expd ',' expc ')'	{yyerror(err_opdouble_string);}
;

expc: 	CADENA	{$$ = $1;}
		| '(' expc ')'	{$$ = $2;}
	/* --- Definicion de funcion Potencia --- */
		| POW '(' expc ',' expe ')'	{$$ = Potencia_Cadena($3, $5);}
	/* --- Errores --- */
		| POW '(' expc ',' expc ')'	{yyerror(err_pow_string);}
		| POW '(' expc ',' expd ')'	{yyerror(err_pow_string);}
;

dec:	DECIMAL	{$$ = $1;}
; 

ent:	ENTERO	{$$ = $1;}
;


%%

int main(){
	Inicializar_Tabla(&t);
	yyparse();
	Destruir_Tabla(&t);
}

yyerror (char *s){
	printf("ERROR: %s\n", s);
}

int yywrap(){
	return 1;
}

/*
	FUNCION POTENCIA CADENA

	-> Descripcion: Realiza la Opreacion POW con cadenas de texto
	-> Recibe: La cadena de texto a potenciar
	-> Devuelve: Cadena de texto potenciada
*/
char* Potencia_Cadena(char* cadena, int exponente){
	int size = strlen(cadena) * abs(exponente);
	char* resultado = (char*) malloc(size * sizeof(char));

	// Si el exponente es igual a cero, se devuelve una cadena vacia
	if(exponente == 0)
		resultado = "";
	// Si el exponente es mayor a cero, se devuelve la cadena replicada tantas
	// veces como lo indique el exponente
	if (exponente > 0){
		for(int i=0; i<exponente; i++)
			resultado = strcat(resultado, cadena);
	}
	// Si el exponente es menor a cero, se devuelve la cadena invertida replicada 
	// tantas veces como lo indique el exponente
	if (exponente < 0){
		char* cadena_invertida = Invertir_Cadena(cadena);

		for(int i=0; i<abs(exponente); i++)
			resultado = strcat(resultado, cadena_invertida);
	}

	return resultado;
}

/*
	FUNCION INVERTIR CADENA

	-> Descripcion: Invierte una Cadena
	-> Recibe: La cadena de texto a invertir
	-> Devuelve: Cadena de texto invertida
*/
char* Invertir_Cadena(char* cadena){
	int size = strlen(cadena);
	int j = size - 1;
	char* resultado = (char*) malloc(strlen(cadena) * sizeof(char));

	for(int i=0; i<size; i++){
		resultado[i] = cadena[j];
		j--;
	}

	return resultado;
}