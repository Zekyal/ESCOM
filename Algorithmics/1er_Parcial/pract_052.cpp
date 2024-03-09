#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<math.h>

int main()
{
	float yf, Viy, t, Vfy;
	const float yi=0, a=-9.8;
	printf("Introduzca los siguientes datos (recuerde que la posici%cn inicial siempre se toma como cero y aceleraci%cn del objeto es la gravedad negativa a=-9.8 m/s) \n\n", 162, 162);
	printf("Altura(yf):");
	scanf("%f", &yf);
	printf("Velocidad inicial del objeto(Viy):");
	scanf("%f", &Viy);
	Vfy=sqrt(pow(Viy,2)+2*a*(yf-yi));
	printf("Vfy=%f", Vfy);
	return 0;
}
