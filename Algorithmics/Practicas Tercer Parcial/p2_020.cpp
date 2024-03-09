#include<stdio.h>
#include<stdlib.h>

int main()
{
	int a;
	printf("Inserte un a%co: ", 164);
	scanf("%d", &a);
	
	if(a%100==0)
	{
		if(a%400==0)
		{
			printf("Es a%co bisiesto", 164);
		}
		else
		{
			printf("No es a%co bisiesto", 164);
		}
	}
	
	else if(a%4==0)
    {
    	printf("Es a%co bisiesto", 164);
   	}
    
	else
    {
    	printf("No es a%co bisiesto", 164);
    }
    
    return 0;
}
