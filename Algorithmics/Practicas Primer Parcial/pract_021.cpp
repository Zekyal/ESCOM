#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float sueldo, nocom, dicom, sueldot;
	printf("Ingrese su sueldo mensual: $");
	scanf("%f", &sueldo);
	printf("Coloque el n%cmero de comisiones realizada: ", 163);
	scanf("%f", &nocom);
	dicom=((sueldo*10)/100.0)*nocom;
	sueldot=dicom+sueldo;
	printf("El dinero obtenido por las comisiones ser%c $%f y su sueldo total ser%c de $%f", 160, dicom, 160, sueldot);
	return 0;
}
