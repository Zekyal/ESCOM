//SIMULADOR DE SUPERMERCADO
//EQUIPO: SALCHIPAPAS
//FECHA: 28/FEB/2018
#include "TADColaLista.h" // libreria para la implementacion de la cola lista
#include <stdio.h>
#include <stdlib.h>

#include <string.h>
#include <time.h>
#include <windows.h> // la usamos para la funcion sleep

// Deficinion de las constantes
#define Tiempo_Base 100 //Tiempo base en ms

int main(void)
{
	char nombre_supermercado[200]; // el nombre del mercado recorando que va sin espacios
	int numero_cajas; // el  numero de cajas  que  se encontraran abiertas
	int tiempo_atencion[10]; // el  tiempo  que se tardara cada caja en atender un cliente	 	
	int tiempo_llegada; // el tiempo en el que los clientes van llegando a las cajas 
	int i,j,k,cajas_totales,cliente,tiempo,fila;
	elemento e;
	cliente =0;
	tiempo =0;
	int suma_cajas;
	cola cajera[10]; //iniciasslizamos las  10 cajas
	srand (time(NULL));	//Inicializar la funcion rand
	printf ("Bienvenido Usuario \n favor de  ingresar el nombre del supermercado \n Recuerda que el nombre no debe de llevar espacios \n"); //el nombre del supermercado 
	gets(nombre_supermercado);
	printf ("¿cuantas cajas  estaran abiertas?\n");
	scanf ("%d",&numero_cajas);
	for (i=0;i<numero_cajas;i++) //for para crear las colas, inicializarlas y ponerles el tiempo de atencion a cada una 
	{
		(&cajera[i]);
		printf("¿cual es el tiempo de  atencion del cajero que esta en la caja no. %d \n  " , i+1); 
		scanf ("%d",&tiempo_atencion[i]);
	}
	printf ("¿cual es el tiempo de llegada de los clientes ?\n");
	scanf ("%d",&tiempo_llegada);
	
	
	while ((cliente<100) || (suma_cajas!=0))
	{
		Sleep(Tiempo_Base); //Esperar el tiempo boase
		tiempo++;				//Incrementar el contador de tiempo
		suma_cajas++;
		for (i=0;i<numero_cajas;i ++) //for para recorrer cada una de las cajas
		{
		//Si el tiempo es multiplo del tiempo de atencion
		if (tiempo % tiempo_atencion[i] == 0)
		{
			suma_cajas=suma_cajas-2;
			
		      	if (!EmptyQueue(&cajera[i]))
		        {
			       	e = Dequeue(&cajera[i]);
				    printf("\n\n\nAtendi a: %d en la caja  %d", e.n,i);
			    }
		        else
		        {
			         	printf("\n\n\nNo hay alguien por atender en caja %d",i);
		        }  


		}
		//Si el tiempo es multiplo del de llegada de los clientes
		if (tiempo % tiempo_llegada == 0)
		{
			suma_cajas=suma_cajas+1;
			cliente++;				//Incrementar el numero de clientes
			e.n = cliente;			//Dar el numero que identifica al cliente
			fila=rand()%numero_cajas;			//Escoger la fila para formarse aleatoriamente					
			Queue(&cajera[fila], e);//Formarse en la fila seleccionada
			printf("\n\n\nLlego el cliente: %d a la cola de la caja %d", e.n,fila);
		}
				//Mostrar los clientes en cada cola
		         printf("\n\n%d clientes en cola %d : [",SizeQueue(&cajera[i]),i);
		         for (k=1;k<=SizeQueue(&cajera[i]);k++)
		         {
					e=ElementQueue(&cajera[i],k);
					printf("%d\t", e.n);
				}
				printf("]");
		
	    }

	
	}
	return 0;	
	}
	

