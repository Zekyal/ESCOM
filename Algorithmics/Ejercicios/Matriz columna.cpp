#include<stdio.h>
#include<stdlib.h>
#define MAX 100

void Matriz(int dim, int M[MAX][MAX])
{
	printf("Inserte un valor para:\n\n");
	int i=0;
		
	while(i<dim)
	{
		for(int j=0; j<dim; j++)
		{
			printf("Posici%cn (%d, %d): ", 162, j, i);
			scanf("%d", &M[i][j]);
		}
		
		i++;
	}	
}

void imprimirMatriz(int dim, int M[MAX][MAX])
{
	int i=0;
	
	while(i<dim)
	{
		printf("%c ", 179);
		
		for(int j=0; j<dim; j++)
		{
			printf("%d ", M[j][i]);
		}
		
		printf("%c\n", 179);
		i++;
	}
}

int main()
{
	int dim;
	int M[MAX][MAX];
	printf("Dimensi%cn de la matriz: ", 162);
    scanf("%d", &dim);
	printf("\nMatriz de %d%c%d por columnas\n\n", dim, 158, dim);
	Matriz(dim, M);
	system("cls");
	printf("Matriz:\n\n");
	imprimirMatriz(dim, M);
}

