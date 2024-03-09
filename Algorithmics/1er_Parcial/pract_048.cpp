#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<math.h>

int main()
{
	float CO, CA, h, sen, cos, tan;
	printf("Introduzca la medida del cateto opuesto:");
	scanf("%f", &CO);
	printf("Introduzca la medida del cateto adyacente:");
	scanf("%f", &CA);
	h=sqrt(pow(CO,2)+pow(CA,2));
	sen=CO/h+0.0;
	cos=CA/h+0.0;
	tan=CO/CA+0.0;
	printf("h=%f \t sen=%f%c \t cos=%f%c \t tan=%f%c", h, sen, 248, cos, 248, tan, 248);
	return 0;
}
