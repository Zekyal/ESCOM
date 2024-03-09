#include<stdio.h>

int main()
{
	int n, m, multi, a;
	printf("MULTIPLICAI%cN\n\n", 224);
	printf("Ingrese 2 n%cmeros (n%cm): ", 163, 158);
	scanf("%d, %d", &n, &m);
	a=n;
	
	do
	{
		multi=multi+m;
		n--;
	}while(n>0);
	
	printf("\n%d%c%d=%d", a, 158, m, multi);
	return 0;
}
