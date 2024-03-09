#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define X 4 //Años
#define Y 5 //Carrera
#define Z 3 //Semestre
#define W 2 //Grupo(no. alumnos)

int P1(int al, int dato[X][Y][Z][W]);
int P2(int al, int dato[X][Y][Z][W]);
int P3(int al, int dato[X][Y][Z][W]);
int P4(int al, int dato[X][Y][Z][W]);

int main()
{
	int dato[X][Y][Z][W], i, j, k, l, op;
	int al;
	srand(time(NULL));
	printf("Seleccione una pegunta:\n\n%cCu%cntos alumnos hay?\n\n1.En x a%co\n2.En n carrera, m semestre, x grupo\n3.En n carrera, m semestre, todos sus grupos\n4.En n carrera, m semestre, x a%co, z grupo\n", 168, 160, 164, 164);
	scanf("%d", &op);
	
	for(i=1; i<X; i++)//Datos random
	{
		for(j=1; j<Y; j++)
		{
			for(k=1; k<Z; k++)
			{
				for(l=1; l<W; l++)
				{
					dato[i][j][k][l]=15+rand()%(31-15);
					//printf("%d, %d, %d, %d, %d\n", i, j, k, l, dato[i][j][k][l]);
				}
			}
		}
	}
	
	switch(op)//Preguntas
	{
		case 1:
		{
			system("cls");
			printf("%cCu%cntos alumnos hay en x a%co?", 168, 160, 164);
		    P1(al, dato);
			break;
		}
		case 2:
		{
			system("cls");
			printf("%cCu%cntos alumnos hay en n carrera, m semestre, x grupo?", 168, 160);
			P2(al, dato);
			break;
		}
		case 3:
		{
			system("cls");
			printf("%cCu%cntos alumnos hay en n carrera, m semestre, todos sus grupos?", 168, 160);
			P3(al, dato);
			break;
		}
		case 4:
		{
			system("cls");
			printf("%cCu%cntos alumnos hay en n carrera, m semestre, x a%co, z grupo?", 168, 160, 164);
			P4(al, dato);
			break;
		}
		default:
      	{
      		system("cls");
		  	printf("Valor inv%clido", 162);
		   	break;
    	}
	}
}

int P1(int al, int dato[X][Y][Z][W])
{
	int x, i;
	printf("\n\nx= ");
	scanf("%d", &x);
	i=x;
	
	if(x>=1 && x<=3)
	{	
      	for(int j=1; j<Y; j++)
        {
	    	for(int k=1; k<Z; k++)
	    	{
	     		for(int l=1; l<W; l++)
	     		{
	     			al=al+dato[i][j][k][l];
	    		}
    		}
    	}
    	
        printf("\n%d", al);
	}
	
	else
	{
		printf("Valor inv%clido", 160);
	}
}

int P2(int al, int dato[X][Y][Z][W])
{
	int n, m, x, j, k, l;
	printf("\n\nn= ");
	scanf("%d", &n);
	j=n;	
	printf("m= ");
	scanf("%d", &m);
	k=m;
	printf("x= ");
	scanf("%d", &x);
	l=x;
	
	if(n>=1 && n<=5)
	{
		if(m>=1 && m<=3)
		{
			if(x==1)
			{
				for(int i=1; i<X; i++)
				{
					al=al+dato[i][j][k][l];
				}
				
				printf("\n%d", al);
			}
			
			else
        	{
        		printf("Valor inv%clido", 160);
        	}
		}
		
		else
      	{
        	printf("Valor inv%clido", 160);
        }
	}
	
	else
    {
       	printf("Valor inv%clido", 160);
    }
}

int P3(int al, int dato[X][Y][Z][W])
{
	int n, m, j, k; 
	printf("\n\nn= ");
	scanf("%d", &n);
	j=n;	
	printf("m= ");
	scanf("%d", &m);
	k=m;
	
	if(n>=1 && n<=5)
	{
		if(m>=1 && m<=3)
		{
			for(int i=1; i<X; i++)
			{
				for(int l=1; l<W; l++)
				{
					al=al+dato[i][j][k][l];
				}
			}
			
			printf("\n%d", al);
		}
		
		else
      	{
        	printf("Valor inv%clido", 160);
        }
	}
	
	else
    {
       	printf("Valor inv%clido", 160);
    }
}

int P4(int al, int dato[X][Y][Z][W])
{
	int n, m, x, z, j, k, l, i;
	printf("\n\nn= ");
	scanf("%d", &n);
	j=n;	
	printf("m= ");
	scanf("%d", &m);
	k=m;
	printf("x= ");
	scanf("%d", &x);
	i=x;
	printf("z= ");
	scanf("%d", &z);
	l=z;
	
	if(n>=1 && n<=5)
	{
		if(m>=1 && m<=3)
		{
			if(x>=1 && x<=3)
			{
				if(z==1)
				{
					al=al+dato[i][j][k][l];
					printf("\n%d", al);
				}
				
				else
            	{
             		printf("Valor inv%clido", 160);
             	}
			}
			
			else
        	{
        		printf("Valor inv%clido", 160);
        	}
		}
		
		else
      	{
        	printf("Valor inv%clido", 160);
        }
	}
	
	else
    {
       	printf("Valor inv%clido", 160);
    }
}	
