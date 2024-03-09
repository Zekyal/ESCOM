#include<stdio.h>
#include<stdlib.h>
#define MAX 100

void Matriz(int lim1, int lim2, int i, int j, int dim, int M[MAX][MAX])
{
	printf("Inserte un valor para:\n\n");
	
	while(M[j][i]<dim*dim)
	{
		i++;	
    	for(i; i<lim1; i++)
		{
			printf("Posici%cn (%d, %d): ", 162, j, i);
			scanf("%d", &M[j][i]);
		}
		lim1--;
		i--;
		j++;
	
		for(j; j<lim1; j++)
		{
			printf("Posici%cn (%d, %d): ", 162, j, i);
			scanf("%d", &M[j][i]);
		}
		lim2++;
	
		for(i; i>=lim2; i--)
		{
			printf("Posici%cn (%d, %d): ", 162, j, i);
			scanf("%d", &M[j][i]);
		}
	
		for(j; j>=lim2; j--)
		{
			printf("Posici%cn (%d, %d): ", 162, j, i);
			scanf("%d", &M[j][i]);
		}
		i--;
	}
}

void imprimirMatriz(int lim1, int lim2, int i, int j,int dim, int M[MAX][MAX])
{
	for(i=0; i<dim; i++)
	{
		printf("%c ", 179);
		
		for(j=0; j<dim; j++)
		{
			printf("%d ", M[i][j]);
		}
		
		printf("%c\n", 179);
	}			
}

int main()
{
	int dim, lim1, lim2=0;
	int M[MAX][MAX];
	int i, j;
	printf("Dimensi%cn de la matriz: ", 162);
    scanf("%d", &dim);
    lim1=dim;
	printf("\nMatriz de %d%c%d por filas\n\n", dim, 158, dim);
	Matriz(lim1, lim2, i, j, dim, M);
	system("cls");
	printf("Matriz:\n\n");
	imprimirMatriz(lim1, lim2, i, j, dim, M);
}


