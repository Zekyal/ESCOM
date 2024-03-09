#include<stdio.h>
#include<stdlib.h>

int main()
{
	int gl, gv;
	printf("Goles del equipo local: ");
	scanf("%d", &gl);
	printf("Goles del equipo visitante: ");
	scanf("%d", &gv);
	
	if(gl>0)
	{
		if(gv>0)
		{
			if(gl<gv)
         	{
        		printf("\nGana el equipo visitante");
        	}
        	else if(gl>gv)
         	{
        		printf("\nGana el equipo local");
        	}
        	else
        	{
            		printf("\nEmpate");
          	}
    	}
    	else
    	{
			printf("Error");
		}
	}
	
	else
	{
		printf("Error");
	}
   
	return 0;
}
