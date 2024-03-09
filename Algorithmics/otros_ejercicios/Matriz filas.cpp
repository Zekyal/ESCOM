#include<stdio.h>
#include<stdlib.h>
#define MAX 100

void Matriz(int dim, int M[MAX][MAX])
{
	printf("Inserte un valor para:\n\n");
		
	for(int i=0; i<dim; i++)
	{
		for(int j=0; j<dim; j++)
		{
			printf("Posici%cn (%d, %d): ", 162, i, j);
			scanf("%d", &M[i][j]);
		}
	}
	
}

void imprimirMatriz(int i, int j,int dim, int M[MAX][MAX])
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
	int dim;
	int M[MAX][MAX];
	int i, j;
	printf("Dimensi%cn de la matriz: ", 162);
    scanf("%d", &dim);
	printf("\nMatriz de %d%c%d por filas\n\n", dim, 158, dim);
	Matriz(dim, M);
	system("cls");
	printf("Matriz:\n\n");
	imprimirMatriz(i, j, dim, M);
}

