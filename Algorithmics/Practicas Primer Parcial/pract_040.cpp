#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	int x, y, r1, r2;
	printf("Introduce un valor para x:");
	scanf("%d", &x);
	printf("Introduce un valor para y:");
	scanf("%d", &y);
	r1=x/y+0.0;
	r2=x % y;
	printf("El resultado de x/y es %d y de x%y es %d", r1, r2);
	return 0;
}
