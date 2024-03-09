 #include<stdio.h>
#include<stdlib.h>

int main()
{
	char let1, let2, let3;
	printf("Inserte 3 letras separadas por coma (,): ");
	scanf("%c, %c, %c", &let1, &let2, &let3);
	
	if(let2>let1)
	{
		if(let3>let1)
		{
			printf("%c viene primero en el alfabeto", let1);
		}
		else if(let3<let1)
		{
			printf("%c viene primero en el alfabeto", let3);
		}
	}
	else if(let1>let2)
	{
		if(let2<let3)
		{
			printf("%c viene primero en el alfabeto", let2);
		}
		else if(let2>let3)
		{
			printf("%c viene primero en el alfabeto", let3);
		}
	}
	else
	{
		printf("2 o m%cs son iguales", 160);
	}
	
	return 0;
}
