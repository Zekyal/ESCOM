#include<stdio.h>
#define TAM 50

int main()
{
	int num[TAM], i=0, suma;
	printf("Suma de todos los n%cmeros m%cltiplos de 3:\n\n", 163, 163);
	
	for(int n=9; n<21; n++)
	{
		num[i]=n;
		
		if(num[i]%3==0)
		{
			printf("%d+", num[i]);
			suma=suma+num[i];
		}
		i++;
	}
	
	for(int n=28; n<=45; n++)
	{
		num[i]=n;
		
		if(num[i]%3==0)
		{
			printf("%d", num[i]);
			suma=suma+num[i];
			
			if(num[i]<45)
			{
				printf("+");
			}
		}
		
		i++;
	}
	
	printf("=%d\n\n*No incluye los n%cmeros comprendidos entre el 21 al 27", suma, 163);
}
