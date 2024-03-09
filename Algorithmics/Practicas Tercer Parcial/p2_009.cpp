#include<stdio.h>
#include<stdlib.h>

int main()
{
	int num1, num2, num3;
	printf("Ingrese 3 n%cmeros separados por coma (,): ", 163);
	scanf("%d, %d, %d", &num1, &num2, &num3);
	
	if(num1<num2)
	{
		if(num2<num3)
		{
			printf("Esta orden num%crico", 130);  
		}
		else
		{
			printf("No estan en orden num%crico", 130);
		}
	}
	else
	{
		printf("No estan en orden num%crico", 130);
	}
	return 0;
}

