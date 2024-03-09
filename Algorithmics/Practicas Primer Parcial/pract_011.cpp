#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float sal, incr, desc, sal2;
	printf("Introduzca su salario: $");
    scanf("%f", &sal);
    incr=(sal*8)/100.0;
    desc=(sal*2.5)/100.0;
    sal2=sal+incr-desc;
    printf("Usted ha tenido un incremento del 8%c y un descuento de 2.5%c, por lo que su salario ahora es: $%f", 37, 37, sal2);
    return 0;
}
