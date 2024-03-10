VARIABLE [A-Za-z_][A-Za-z0-9_]*
DIGITO [0-9]
REAL [+-]?({DIGITO}+|{DIGITO}+"."{DIGITO}+)
%%
{VARIABLE} {printf("Variable %s\n",yytext);}
[+-]?{DIGITO}+ {printf("Numero Entero %s\n",yytext);}
[+-]?{DIGITO}+"."{DIGITO}+ {printf("Numero Decimal %s\n",yytext);}
{REAL}"^"{REAL}  {printf("Potencia %s\n",yytext);}
{REAL}"+"{REAL} {printf("Suma %s\n",yytext);}
{REAL}"-"{REAL} {printf("Resta %s\n",yytext);}
{REAL}"*"{REAL} {printf("Multiplicacion %s\n",yytext);}
{REAL}"/"{REAL} {printf("Division %s\n",yytext);}
{REAL}"%"{REAL} {printf("Modulo %s\n",yytext);}

/*
[pP][oO][wW]"("{REAL}","{REAL}")" {printf("Potencia %s\n",yytext);}
[mM][oO][dD]"("{REAL}","{REAL}")" {printf("Modulo %s\n",yytext);}
*/