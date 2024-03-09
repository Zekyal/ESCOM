#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
int main()
{
	float x,V;
	printf("Medida de un lado del cubo");
	scanf("%fl",&x);
	V=x*x*x;
	printf("El volumen es %fl", V);
	getch();
}
