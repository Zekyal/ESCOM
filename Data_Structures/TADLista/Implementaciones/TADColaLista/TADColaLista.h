/*
LIBRERIA: Cabecera de el TADCOLALISTA
por Mauro Sampayo Hern�ndez :)  
*/

//DEFINICIONES DE CONSTANTES
#define TRUE	1
#define FALSE	0

//DEFINICI�N DE LIBRER�AS
#include "TADListaDoblementeLigada.h"

//DEFINICIONES DE TIPOS DE DATO

//Definir un boolean (Se modela con un "char")
typedef unsigned char boolean;

//Definir una cola (Se modela con una estructura que incluye lista l)
typedef struct cola
{
	lista *l;
} cola;

//DECLARACIÓN DE FUNCIONES
void InitializeQueue(cola *c);			//Inicializar cola (Initialize): Recibe una cola y la inicializa para su trabajo normal.
void Queue(cola *c, elemento e);	//Encolar (Queue): Recibe una cola y agrega un elemento al final de ella. 
elemento Dequeue(cola *c);			//Desencolar (Dequeue): Recibe una cola y remueve el elemento del frente retornándolo.
boolean EmptyQueue(cola *c);				//Es vacía (Empty): Recibe la cola y devuelve verdadero si esta esta vacía.
elemento Front(cola *c);			//Frente (Front): Recibe una cola y retorna el elemento del frente.	
elemento FinalQueue(cola *c);			//Final (Final): Recibe una cola y retorna el elemento del final.
elemento ElementQueue(cola *c, int i); 	// Recibe una cola y un número de elemento de 1 al tamaño de la cola y retorna el elemento de esa posición.
int SizeQueue(cola *c);					//Tamaño (Size): Retorna el tamaño de la cola 	
void DestroyQueue(cola *c);				//Eliminar cola (Destroy): Recibe una cola y la libera completamente.
