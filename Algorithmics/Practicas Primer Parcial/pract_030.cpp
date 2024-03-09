#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float pp, cp, IVA, tot1, tot2;
	printf("Introduzca el precio del art%cculo que va a comprar: $", 161);
	scanf("%f", &pp);
	printf("Introduzca la cantidad: ");
	scanf("%f", &cp);
	tot1=pp*cp;
	IVA=(tot1*16)/100.0;
	tot2=tot1+IVA;
	printf("El total a pagar es $%f", tot2);
	return 0;
}
