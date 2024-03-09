#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
    float pre, desc, pre2;
    printf("Introduzca el precio de la medicina: $");
    scanf("%f", &pre);
    desc=(pre*35)/100.0;
    pre2=pre-desc;
    printf("El precio con el descuento de 35%c aplicado es $%f", 37, pre2);
	return 0;
}
