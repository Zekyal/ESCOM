//Simulación 2 (Implementación Estática)
//EQUIPO: SALCHIPAPAS
//FECHA DE ENTREGA: 4/Abril/2018

#include "TADColaLista.h" 
#include <string.h> //Para utilizar fflush()
#include <stdio.h>
#include <stdlib.h>
#include <windows.h> //Para utilizar Sleep()
#include <time.h> //Para utilizar clock() y clock_t

int main()
{
	elemento e, a, b;//Declaración de un elemento e
	int cantprocesos, i, tiempo, k=0;//Declaración de variables enteras
	cola listos, finalizados;//Declaración de las colas
	InitializeQueue(&listos);//Inicialización de la cola "Listos"
	InitializeQueue(&finalizados);//Inicialización de la cola "Finalizados"
	
	printf("%cCu%cntos procesos desea realizar?", 168, 160);
	scanf("%d", &cantprocesos);//El usuario introduce la cantidad de procesos que desee que sean ejecutados
	
	for(i=0; i<cantprocesos; i++)//Ciclo donde se realizara la introducción de los datos de los elementos que serán introducidos a la cola "Listos"
	{
		fflush( stdin );
		printf("\nNombre del Proceso %d: ", i+1);//Se introduce el nombre del Proceso i+1
		gets(e.nombre);
		fflush( stdin );
		printf("Actividad del Proceso %d: ", i+1);//Se introduce la actividad que realiza el Proceso i+1
		gets(e.actividad);
		fflush( stdin );
		printf("ID del Proceso %d: ", i+1);//Se introduce la ID del Proceso i+1
		gets(e.ID);
		printf("Tiempo de ejecuci%cn del Proceso %d: ", 162, i+1);//Se introduce el tiempo en segundos que el usuario desee que sea ejecutado el Proceso i+1
		scanf("%d", &e.tiempo);	
		
		Queue(&listos, e);//Se encola el elemento i en la cola "Listos"
	}

	clock_t t, tejecucion;//Declaración de variables de tipo clock
	t=clock();//t se iguala al tiempo en el que se inicializan los procesos de ejecución de los elementos. 
	
	while(!EmptyQueue(&listos))
		{
			printf("\n");
			e=Dequeue(&listos);//Se desencola el elemento e de la cola de "Listos"
			
			if(!EmptyQueue(&listos) && k!=0)
			/*Proceso que muestra el proceso anterior que se ejecutó y su ID. No se ejecuta si es la primera vez que se desencola un elemento o si la cola
			"listos está vacía*/
			{
				a=FinalQueue(&listos);
				printf("\nProceso anterior en ser ejecutado: %s ID: %s", a.nombre, a.ID);	
			}
			
			printf("\nEl proceso %s con actividad %s y ID %s se est%c ejecutando. Tiempo restante: %d segundos", e.nombre, e.actividad, e.ID, 160, e.tiempo);
			
			if(!EmptyQueue(&listos))
			/*Proceso que muestra el proceso siguiente que se va a ejecutar y su ID. No se ejecuta si la cola "listos" está vacía*/
			{
				a=Front(&listos);
				printf("\nProceso siguiente a ejecutarse: %s ID: %s", a.nombre, a.ID);	
			}
			
			if(e.tiempo==0)
			{
				e.tejecucion=clock()-t;//Se le resta el tiempo t(Tiempo en el que inicio el proceso de ejecucion de los elementos) a el tiempo actual.
				Queue(&finalizados, e);//Se encola el elemento e, en la cola "Finalizados"
			}
			
			else//Si el tiempo de ejecución es distinto de 0
			{
				e.tiempo--;//Se le resta 1 segundo al tiempo de ejecución que el usuario introdujo previamente
				Sleep(1000);//Espera 1 segundo
				Queue(&listos, e);//Se encola el elemento e, en la cola "Listos"
			}
			
			k++;
		}
	
	printf("\n\n\n");
	
	while(!EmptyQueue(&finalizados))//Muestra los elementos ya finalizados
	{
		e=Dequeue(&finalizados);
		printf("%c%c %s ha finalizado despues de %f segundos\n", 175, 175, e.nombre, ((float)e.tejecucion)/CLOCKS_PER_SEC);
		/*Se muestra el tiempo total, que tardó el elemento e en ser procesado*/
	}
}
