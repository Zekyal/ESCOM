#include <stdio.h>
#include <stdlib.h>

#define MAX 100

void Menu();
int Crear(int tabla[][MAX],int TAM,int TIPO);
int Dibujar(int tabla[][MAX], int TAM);

int main()
{
	int TAM, TIPO;
	printf("Elija el tamano de la tabla\n");
	scanf("%d",&TAM);
	int tabla[MAX][MAX]={0};
	do{
		Menu();
		scanf("%d",&TIPO);
		system("cls");
		if (TIPO<1||TIPO>3)
			printf("Respuesta no valida, favor de elegir una opcion correcta\n");
	}while(TIPO<1||TIPO>3);
	Crear(tabla,TAM,TIPO);
	Dibujar(tabla,TAM);
}

void Menu(){
		printf("Elija el tipo de la tabla\n1.-sucesion vertical\n2.-Sucesion vertical\n3.-sucesion espiral\n");
}
int Crear(int tabla[][MAX], int TAM,int TIPO){
	int i=-1, j=0, contador=0;
	int lim1=TAM, lim2=0;
	if(TIPO==1){
			for(i=0;i<TAM; i++){
				for(j=0;j<TAM;j++){
				contador++;	
				tabla[i][j]=contador;
				}
				printf("\n");
			}
		}
		if(TIPO==2){
			for(i=0;i<TAM; i++){
				for(j=0;j<TAM;j++){
				contador++;	
				tabla[j][i]=contador;
				}
				printf("\n");
			}
		}
		if(TIPO==3){
			while(tabla[j][i]<TAM*TAM){
				i++;
				for(i;i<lim1;i++){
					contador++;	
					tabla[j][i]=contador;
				}
				lim1--;
				i--;
				j++;
				for(j;j<lim1;j++){
					contador++;	
					tabla[j][i]=contador;
				}
				lim2++;
				for(i;i>=lim2;i--){
					contador++;	
					tabla[j][i]=contador;
				}
				
				;
				for(j;j>=lim2+1;j--){
					contador++;	
					tabla[j][i]=contador;
				}
				i--;
			}
			}
			Dibujar(tabla,TAM);
			system("cls");
	 }

int Dibujar(int tabla[][MAX],int TAM){
	int i=0,j=0;
	for(i=0;i<TAM; i++){
				for(j=0;j<TAM;j++){
					if(tabla[i][j]<10);
					printf("\t");
					if(tabla[i][j]<100);
					printf(" ");
					printf("%d ", tabla[i][j]);
				}
					printf("\n");
			}
}
