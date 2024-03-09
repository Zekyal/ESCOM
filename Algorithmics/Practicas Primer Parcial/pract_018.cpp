#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<math.h>

int main()
{
	float a, b, op1, op2;
	printf("Introduza un valor para a");
	scanf("%f", &a);
	printf("Introduza un valor para b");
	scanf("%f", &b);
	op1=2*a+pow(b,2);
	op2=(pow(a,3)+pow(b,3))/2.0;
	printf("La suma del doble del primero m%cs el cuadrado del segundo es %f.\nEl promedio de sus cubos es %f", 160, op1, op2);
	return 0;
}
