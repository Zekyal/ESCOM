#include<stdio.h>
#include<stdlib.h>

int main()
{
	float num1, num2, num3;
	printf("Inserte 3 n%cmeros separadas por coma (,): ", 163);
	scanf("%f, %f, %f", &num1, &num2, &num3);
	
	if(num2>num1)
	{
		if(num2>num3)
		{
			printf("%f es mayor", num2);
		}
		else if(num3>num2)
		{
			printf("%f es mayor", num3);
		}
	}
	else if(num1>num2)
	{
		if(num1>num3)
		{
			printf("%f es mayor", num1);
		}
		else if(num3>num1)
		{
			printf("%f es mayor", num3);
		}
	}
	else
	{
		printf("Error");
	}
	
	return 0;
}
