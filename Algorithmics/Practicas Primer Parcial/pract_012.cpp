#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float pres, urg, ped, trau;
	printf("Monto presupuestal: $");
	scanf("%f", &pres);
	urg=(pres*37)/100.0;
	ped=(pres*42)/100.0;
	trau=(pres*21)/100.0;
	printf("El monto presupuestal destinado a cada departamento es: \n\n Urgencias: $%f \n Pediatr%ca: $%f \n Traumatolog%ca: $%f", urg, 161, ped, 161, trau);
	return 0;
}
