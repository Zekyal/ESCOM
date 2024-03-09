#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float m, ft, in;
	printf("Conversor de metros a pies y pulgadas \n\n");
	printf("Introduzca la medida (metros):");
	scanf("%f", &m);
	ft=3.28084;
	in=m*39.3701;
	printf("%fft \t %fin", ft, in);
	return 0;
}
