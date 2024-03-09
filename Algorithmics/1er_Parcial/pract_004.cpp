//Prímetro Rectángulo
#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float b,h,P;
	printf("Per%cmetro Rect%cngulo \n", 161, 160);
	printf("\nIntroduzca la medida de la base de su rect%cngulo:", 160);
	scanf("%f", &b);
	printf("Introduzca la medida de la altura de su rect%cngulo:", 160);
	scanf("%f", &h);
	P=2*b+2*h;
	printf("\nEl Per%cmetro Rect%cngulo es: %f", 161, 160, P);
	return 0;
}
