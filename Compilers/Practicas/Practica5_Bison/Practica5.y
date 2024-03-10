/* 
	Compilacion:
		-flex Practica5.l
		-bison Practica5.y -d
		-gcc lex.yy.c Practica5.tab.c -lm
*/

/* --- Declaracion de Bibliotecas de C +++ */
%{
	#include <stdio.h>
	#include <math.h>
%}

/* --- Declaraciones de BISON ---*/
%union{
	int entero;
	float decimal;
}

/* Definicion de Tokens */
%token <entero> ENTERO
%token <decimal> DECIMAL 
%token MOD

/* Definicion de No Terminales */
%type <entero> ent
%type <entero> expe
%type <decimal> dec
%type <decimal> expd

/* Precedencia de Operaciones */
%left '+' '-'
%left '*' '/'
%left NEGATIVO POSITIVO 	// Para Numeros enteros y decimales con signo
%left MOD

/* --- Gramatica ---*/
%%

input:	/* Cadena Vacia*/
		| input line
;

line: 	'\n' 	{printf("Salto de Linea");}
	/* --- Definicion de expresiones --- */
		| expe '\n'	{printf("\n\t->Resultado: %d\n\n", $1);}
		| expd '\n'	{printf("\n\t->Resultado: %f\n\n", $1);}
;

/* --- OPERACIONES CON NUMEROS ENTEROS --- */
expe:	ent	{$$ = $1;}
		| expe '+' expe 	{$$ = $1 + $3;}
		| expe '-' expe 	{$$ = $1 - $3;}
		| expe '*' expe 	{$$ = $1 * $3;}
		| expe '/' expe 	{$$ = $1 / $3;}
	/* --- Definicion de Numeros Enteros con signo --- */
		| '-' expe %prec NEGATIVO	{$$ = -$2;}
		| '+' expe %prec POSITIVO	{$$ = +$2;}
	/* --- Definicion de funcion Modulo --- */
		| MOD '(' expe ',' expe ')'	{$$ = $3 % $5;}

/* --- OPERACIONES CON NUMEROS DECIMALES --- */
expd:	dec	{$$ = $1;}
		| expd '+' expd 	{$$ = $1 + $3;}
		| expd '-' expd 	{$$ = $1 - $3;}
		| expd '*' expd 	{$$ = $1 * $3;}
		| expd '/' expd 	{$$ = $1 / $3;}
		| expd '+' expe 	{$$ = $1 + $3;}
		| expd '-' expe 	{$$ = $1 - $3;}
		| expd '*' expe 	{$$ = $1 * $3;}
		| expd '/' expe 	{$$ = $1 / $3;}
		| expe '+' expd 	{$$ = $1 + $3;}
		| expe '-' expd 	{$$ = $1 - $3;}
		| expe '*' expd 	{$$ = $1 * $3;}
		| expe '/' expd 	{$$ = $1 / $3;}
	/* --- Definicion de Numeros Decimales con signo --- */
		| '-' expd %prec NEGATIVO	{$$ = -$2;}
		| '+' expd %prec POSITIVO	{$$ = +$2;}
	/* --- Definicion de funcion Modulo --- */
		// Se hace uso de 'fmod' ya que '%' solo funciona con enteros
		| MOD '(' expd ',' expd ')'	{$$ = fmod($3, $5);}
		| MOD '(' expd ',' expe ')'	{$$ = fmod($3, $5);}
		| MOD '(' expe ',' expd ')'	{$$ = fmod($3, $5);}
;

dec:	DECIMAL	{$$ = $1;}
; 

ent:	ENTERO	{$$ = $1;}
;

%%

int main(){
	yyparse();
}

yyerror (char *s){
	printf("ERROR: %s\n", s);
}

int yywrap(){
	return 1;
}