#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float in, yd, ft, cm, m;
	printf("Conversor de medidas\n\n");
	printf("Introduzca una medida en pies(ft):");
	scanf("%f", &ft);
	yd=(1/3.0)*ft;
	in=12*ft;
	cm=in*2.54;
	m=cm/100.0;
	printf("%fyd \t %fin \t %fcm \t %fm \t", yd, in, cm, m);
	return 0;
}
