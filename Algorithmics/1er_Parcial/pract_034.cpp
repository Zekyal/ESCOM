#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float su1, su2, su3, au1, au2, au3;
	printf("Sueldo del primer trabajador: $");
	scanf("%f", &su1);
	printf("Sueldo del segundo trabajador: $");
	scanf("%f", &su2);
	printf("Sueldo del tercer trabajador: $");
	scanf("%f", &su3);
	au1=su1+((su1*10)/100.0);
	au2=su2+((su2*12)/100.0);
	au3=su3+((su3*15)/100.0);
	printf("\nSueldo del primer trabajador con aumento: $%f \nSueldo del segundo trabajador con aumento: $%f \nSueldo del tercer trabajador con aumento: $%f", au1, au2, au3);
	return 0;
}
