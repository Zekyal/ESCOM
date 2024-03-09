#include<stdio.h>
#define TAM 10

int main()
{
	float num[TAM], mayor=-9999.0;
	int cont=1;
	printf("Inserte 10 números: ");

    for(int i=0; i<TAM; i++)
    {
    	printf("%d: ", cont);
    	scanf("%f", &num[i]);
    	
    	if(num[i]>=mayor)
    	{
    		mayor=num[i];
		}
		
		cont++;
	}
	
	printf("El n%cmero mayor es %f", mayor);
}
