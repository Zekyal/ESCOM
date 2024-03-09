#include<stdio.h>
#include<stdlib.h>

int main()
{
	int p;
	printf("Inserte el n%cmero de serie de su producto: ", 163);
	scanf("%d", &p);
	
	if(p>=14681)
	{
		if(p<=15681)
		{
			printf("El producto est%c defectuoso", 160);
		} 
		else if(p>=70001)
     	{
    		if(p<=79999)
    		{
    			printf("El producto est%c defectuoso", 160);
    		}
    		else if(p>=88888)
           	{
           		if(p<=111111)
           		{
           			printf("El producto est%c defectuoso", 160);
				}
				else
              	{
            		printf("No est%c defectuoso", 160);
            	}
            }
            else
            {
            	printf("No est%c defectuoso", 160);
            }
    	}
    	else
       	{
         	printf("No est%c defectuoso", 160);
       	}
	}
	
	else
    {
       	printf("No est%c defectuoso", 160);
    }
	
	return 0;
}
