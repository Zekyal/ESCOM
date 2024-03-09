//Sueldos
#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float su1,su2,su3,su4,su5,su6,ST,SP;
	printf("Sueldos Semestrales ($)");
	printf("\nIntroduzca los valores monetarios de sus 6 sueldos separados por coma(,)");
	scanf("%f, %f, %f, %f, %f, %f", &su1, &su2, &su3, &su4, &su5, &su6);
	ST=su1+su2+su3+su4+su5+su6;
	printf("\nLa suma total de sus sueldos es: %f", ST);
	SP=ST/6+0.0;
	printf("\nSu promedio semestral es: %f", SP);
	return 0;
}
