#include<stdio.h>
#include<stdlib.h>

int main()
{
	int num, res;
	printf("Inserte un n%cmero: ", 163);
	scanf("%d", &num);
	
	if(num%2==0)
	{
		printf("Es par");
	}
	else printf("Es impar");
	
	return 0;
}
