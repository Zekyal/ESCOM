%{
	#include <string.h>
	#include "Practica6.tab.h"

	/* Declaracion de Funciones */
	/*
		FUNCION QUITAR COMILLAS

		-> Descripcion: Quita las comillas de una cadena de texto
		-> Recibe: La cadena de texto a la cual se le quitaran comillas
		-> Devuelve: Cadena de texto sin Quitar_Comillas
		-> Observaciones: Se quitan las comillas cuando se recibe una cadena de texto, 
		para que asi no sea guardada con todo y comillas al tokenizarse.
	*/
	char* Quitar_Comillas(char*);
%}

VARIABLE [A-Za-z0-9_][A-Za-z0-9_]*
CADENA ([^\\\"]|\\.)*
DIGITO [0-9]
POTENCIA [pP][oO][wW]

%%
{DIGITO}+ 							{
										printf("->Numero Entero %s\n",yytext);
										yylval.entero = atoi(yytext);
										return (ENTERO);
									}
{DIGITO}*"."{DIGITO}+				{
										printf("->Numero Decimal %s\n",yytext);
										yylval.decimal = atof(yytext);
										return (DECIMAL);
									}
{POTENCIA}					 		{
										printf("->Potencia\n");
										return (POW);
									}								
"+"|"-"|"*"|"/"|"%"|"="				{
										printf("->Operador %s\n",yytext);
										return (yytext[0]);
									}
"int"								{	
										printf("->Tipo de dato entero\n");
										return (INT);
									}
"double"							{	
										printf("->Tipo de dato flotante double\n");
										return (DOUBLE);
									}
"string"							{	
										printf("->Tipo de dato cadena de texto\n");
										return (STRING);
									}
{VARIABLE} 							{	
										printf("->Variable %s\n",yytext);
										yylval.cadena = strdup(yytext);
										return (VARIABLE);
									}
\"{CADENA}\" 						{	
										char* cadena_texto = Quitar_Comillas(yytext);
										printf("->Cadena %s\n",cadena_texto);
										yylval.cadena = strdup(cadena_texto);
										return (CADENA);
									}
"("|")"|","|";"						{
										printf("->Simbolo %s\n",yytext);
										return (yytext[0]);
									}
"\n"								{
										printf("->Salto de linea\n");
										return (yytext[0]);
									}
%%

char* Quitar_Comillas(char* cadena){
	int size = strlen(cadena) - 2;;
	char* resultado = (char*) malloc(size * sizeof(char));

	for(int i=1; i<=size; i++){
		char aux = cadena[i];
		resultado = strncat(resultado, &aux, 1);
	}

	return resultado;
}