%{
	#include "Practica5.tab.h"
%}

DIGITO [0-9]
MODULO [mM][oO][dD]
REAL [+-]?({DIGITO}+|{DIGITO}+"."{DIGITO}+)

%%
{DIGITO}+ 							{
										printf("Numero Entero %s\n",yytext);
										yylval.entero = atoi(yytext);
										return (ENTERO);
									}
{DIGITO}*"."{DIGITO}+				{
										printf("Numero Decimal %s\n",yytext);
										yylval.decimal = atof(yytext);
										return (DECIMAL);
									}
{MODULO}					 		{
										printf("Modulo\n");
										return (MOD);
									}								
"+"|"-"|"*"|"/"						{
										printf("Operador %s\n",yytext);
										return (yytext[0]);
									}
"("|")"|","							{
										printf("Simbolo %s\n",yytext);
										return (yytext[0]);
									}
"\n"								{
										printf("Salto de linea\n");
										return (yytext[0]);
									}
%%