#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float est, h, m, ph, pm;
	printf("Introduzca el n%cmero total de estudiantes:", 163);
	scanf("%f", &est);
	printf("Introduzca el n%cmero total de estudiantes mujeres:", 163);
	scanf("%f", &m);
	printf("Introduzca el n%cmero total de estudiantes hombres:", 163);
	scanf("%f", &h);
	
	if(m+h==est)
	{
	    ph=(100*h)/est+0.0;
	    pm=(100*m)/est+0.0;
	    printf("El porcentaje de mujeres es %f%c y de hombres es %f%c", pm, 37, ph, 37);
	}
	else
	{
		printf("Alg%cn dato es err%cneo :/", 163, 162);
	}
	return 0;
}
