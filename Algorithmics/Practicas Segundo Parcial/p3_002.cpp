#include<stdio.h>
#define TAM 11

int main()
{
	int num[TAM], i;
	num[0]=10;
	printf("N%cmeros pares comprendidos del 10 al 20:\n\n", 163);
	
	for(i=0; i<TAM; i++)
	{
		if(num[i]%2==0)
		{
			printf("%d\n", num[i]);
		}
		
		num[i+1]=num[i]+1;
	} 
}
