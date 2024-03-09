#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	float acre, hect;
	printf("Conversor de acres a hect%creas\n\n", 160);
	printf("Inserte la medida de la extensi%cn del %crea en acres:", 162, 160);
	scanf("%f", &acre);
	hect=acre*0.404686;
	printf("\n%f hect%creas", hect, 160);
	return 0;
}
