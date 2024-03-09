#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float sal, desc,  total;
	printf("Introduzca su salario: $");
    scanf("%f", &sal);
    desc=(sal*20)/100;
    total=sal-desc;
    printf("Usted ha tenido un descuento del 20%c, por lo que su salario ahora es: $%f", 37, total);
    return 0;
}
