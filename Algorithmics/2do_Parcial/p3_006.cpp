#include<stdio.h>

int main()
{
	int num, fact=1, a;
	printf("FACTORIAL DE UN N%cMERO\n\n", 233);
	printf("Inserte un n%cmero comprendido del 3 al 9: ", 163);
	scanf("%d", &num);
	a=num;
	
	if(num<=9 && num>=3)
	{
		do
		{
			fact=fact*num;
			num--;
		}while(num>0);
		
		printf("\n%d!=%d", a, fact);
	}
	
	else
	{
		printf("\nEl n%cmero no est%c en el rango", 163, 160);
	}
}
