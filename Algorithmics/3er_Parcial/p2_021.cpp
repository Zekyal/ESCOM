#include <stdio.h>
#include <stdlib.h>

int main()
{
	int  lic, color, edad;
	char model;
	float precio, incr, incr2, pref;
	printf("Introduzca el modelo de su coche (A o B): ");
	scanf("%c", &model);
	printf("\nSeleccione el color de el coche: \n\n 1.Blanco\n\n 2.Metalizado\n\n 3.Otro");
	scanf("%d", &color);
	printf("\nIntroduzca su edad: ");
	scanf("%d", &edad);
	printf("\n¿Cu%cntos a%cos tiene con licencia de conducir? ");
	scanf("%d", &lic);
	
	if(model=='A')
	{
		if(color==1)
		{
			precio=240.41;
		}
		if(color==2)
		{
			precio=330;
		}
		if(color==3)
		{
			precio=270.5;
		}
	}
	if(model='B')
	{
		if(color==1)
		{
			precio=300;
		}
		if(color==2)
		{
			precio=360.5;
		}
		if(color==3)
		{
			precio=330;
		}
	}
	
	if(lic<2)
	{
		incr=(precio*25)/100+0.0;
	}

	
	if(edad>=26)
	{
		if(edad<=30)
		{
			incr2=(precio*10)/100+0.0;
		}
		else
		{
			if(edad<=65)
			{
    			incr2=0;	
			}
			else
			{
				incr2=(precio*10)/100+0.0;
			}
		}
	}
	else
	{
		incr2=(precio*25)/100+0.0;
	}
	
	pref=precio+incr+incr2;
	printf("\nPrecio: $%f", pref);
	return 0;
}
