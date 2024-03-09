#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float kg, g, lb, ton;
	printf("Introduzca su peso o el de alguien m%cs en kilos:", 140, 160);
	scanf("%f", &kg);
	g=kg*100;
	lb=kg*2.20462;
	ton=kg/1000.0;
	printf("\nSu peso: \n %fg \n %flb \n %fton", g, lb, ton);
	return 0;
}
