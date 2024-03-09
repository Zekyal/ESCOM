#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float p1, p2, p3, cal1, cal2, cal3, calt;
	printf("Calificaci%cn Algoritmia: \n\n", 162);
	printf("Introduzca el porcentaje de total de la calificaci%cn(100%c) que vale su primer parcial:", 162, 37);
	scanf("%f", &p1);
	printf("Introduzca el porcentaje de total de la calificaci%cn(100%c) que vale su segundo parcial:", 162, 37);
	scanf("%f", &p2);
	printf("Introduzca el porcentaje de total de la calificaci%cn(100%c) que vale su tercer parcial:", 162, 37);
	scanf("%f", &p3);
	
	if(p1+p2+p3==100)
	{
		printf("\n\nIntroduzca su calificaci%cn del primer parcial:", 162);
		scanf("%f", &cal1);
		printf("Introduzca su calificaci%cn del segundo parcial:", 162);
		scanf("%f", &cal2);
		printf("Introduzca su calificaci%cn del tercer parcial:", 162);
		scanf("%f", &cal3);
		calt=((cal1*p1)/100.0)+((cal2*p2)/100.0)+((cal3*p3)/100.0);
		printf("\n\nSu calificaci%cn final es:%f", 162, calt);
	}
	
    else
	{
		printf("\nLos porcentajes no cumplen con el 100%c", 37);
	}
	return 0;
}
