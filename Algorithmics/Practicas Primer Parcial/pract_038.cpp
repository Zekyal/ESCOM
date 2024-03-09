#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<math.h>

int main()
{
	float x1, x2, x3, y1, y2, y3, d12, d23, d31, P;
	printf("Inserte las coordenadas (x,y) de su tri%cngulo: \n\n P1:", 160);
	scanf("%f, %f", &x1, &y1);
	printf(" P2:");
	scanf("%f, %f", &x2, &y2);
	printf(" P3:");
	scanf("%f, %f", &x3, &y3);
	d12=sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
	d23=sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));
	d31=sqrt((x3-x1)*(x3-x1)+(y3-y1)*(y3-y1));
	P=d12+d23+d31;
	printf("El Per%cmetro es: %f", 161, P);
	return 0;
}
