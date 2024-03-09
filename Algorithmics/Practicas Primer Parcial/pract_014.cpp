#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float h, sal, ht, hex, salt1, salt2;
	printf("Introduzca la cantidad de horas con las que debe cumplir: ");
	scanf("%f", &h);
	printf("Escriba el salario recibido por hora de trabajo: $");
	scanf("%f", &sal);
	printf("Escriba el n%cmero de horas que trabaj%c: ", 163, 162);
	scanf("%f", &ht);
	
	if(ht>h)
	{
		hex=ht-h;
		salt1=(hex*2*sal)+h*sal;
		printf("Su salario total es: $%f", salt1);
	} 
	
	else
	{
		salt2=ht*sal;
		printf("Su salario total es: $%f", salt2);
	}
	return 0;
}
