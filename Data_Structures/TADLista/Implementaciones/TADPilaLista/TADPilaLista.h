//LIBRERIA: Cabecera de el TAD PILA implementado con el TAD LISTA

//DEFINICIONES DE CONSTANTES
#define TRUE	1
#define FALSE	0

//DEFINICION DE LIBRERÕAS
#include "TADListaDoblementeLigada.h"

//DEFINICIONES DE TIPOS DE DATO

//Definir un boolean (Se modela con un "char")
typedef unsigned char boolean;


//Definir una pila (Se modela con una estructura que unicamente incluye una lista l)
typedef struct pila
{		
	lista *l;
}pila;

//DECLARACI”N DE FUNCIONES
void InitializeStack(pila *s);			//Inicializar pila (Iniciar una pila para su uso)
void Push(pila *s, elemento e);		//Empilar (Introducir un elemento a la pila)
elemento Pop (pila *s);				//Desempilar (Extraer un elemento de la pila)
boolean EmptyStack(pila *s);				//Vacia (Preguntar si la pila esta vacia)
elemento Top(pila *s);				//Tope (Obtener el "elemento" del tope de la pila si extraerlo de la pila)
int SizeStack(pila *s);					//Tama√±o de la pila (Obtener el n√∫mero de elementos en la pila)
void DestroyStack(pila *s);				//Elimina pila (Borra a todos los elementos y a la pila de memoria)
