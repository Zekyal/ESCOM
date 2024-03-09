#include<stdio.h>

int main()
{
	char c[6]; //Se debe especificar el número de caractreres dentro del []
	c[0]='H'; //Siempre se inicializa en 0
	c[1]='o';
	c[2]='l';
	c[3]='a';
	c[4]=':';
	c[5]='D'; //No se toma en cuenta el último numero (En este caso el 6)
	
	for(int i=0; i<6; i++) //Se usa estructura "for" para imprimir la cadena de caracteres
	{
		printf("%c", c[i]);
	}
}


