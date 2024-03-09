#include<stdio.h>
#include<stdlib.h>

int main()
{
	int x;
	printf("Inserte un valor entero:\n\nx=");
	scanf("%d", &x);
	
	if(x<0)
	{
		printf("x<0");
	}
	else if(x>=0)
	{
		if(x>100)
	    {
		    printf("x>100");
	    }
		else if(x<=100)	
		{
			printf("0<=x<=100");
		}
	}
	
	return 0;
}
