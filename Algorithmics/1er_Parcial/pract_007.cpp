#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float km, pb;
	printf("Precio de boletos de viaje: \n\n");
	printf("Coloque la cantidad de kil%cmetros(km) que recorrer%c en su viaje:", 162, 160);
	scanf("%f", &km);
	pb=6.50*km;
	printf("El precio del boleto ser%c de $%f", 160, pb);
	return 0;
}
