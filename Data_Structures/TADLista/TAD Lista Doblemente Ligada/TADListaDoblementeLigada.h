/*
IMPLEMENTACION TAD LISTA DOBLEMENTE LIGADO (TADListaDoblementeLigada.h)
por MAURO SAMPAYO HERNÁNDEZ
Grupo: 1CM7
*/

#ifndef __TADLista_H
#define __TADLista_H

#define TRUE 1
#define FALSE 0

typedef unsigned char boolean;

typedef struct elemento
{
	//Lo que gustes	
	int n, num, tiempo, tejecucion;
	char nombre[45], actividad[200], ID[45];
	char c;
}elemento;

//Estructura de un NODO DOBLEMENTE LIGADO
typedef struct nodo
{
	elemento e;
	struct nodo *siguiente;	
	struct nodo *anterior;	
} nodo;

//Se define una posicion como un apuntador a nodo
typedef nodo* posicion;

//Estructura de una LISTA
typedef struct lista
{
	int tamanio;
	posicion frente;
	posicion final;
}lista;

//Efecto: Recibe una lista l y la inicializa.
void Initialize (lista *l);

//Efecto: Recibe una lista l y la destruye completamente.
void Destroy (lista *l);

//Efecto: Recibe una lista l y retorna la posición del elemento al final de la lista.
posicion Final (lista *l);

//Efecto: Recibe una lista l y retorna la posición del elemento al frente de la lista.
posicion First (lista *l);

//Efecto: Recibe una lista l y una posición p y devuelve la posición del elemento siguiente de p.
posicion Following (lista *l,posicion p);

//Efecto: Recibe una lista l y una posición p; y devuelve la posición del elemento anterior a p.
posicion Previous (lista *l,posicion p);

//Efecto: Recibe una lista l y un elemento e; y devuelve la posición del elemento que coincida exactamente con el elemento e.
posicion Search (lista *l,elemento e);

//Efecto: Recibe una lista l y una posición p; y devuelve el elemento en dicha posición. 
elemento Position (lista *l,posicion p);

//Efecto: Recibe una lista l y una posición p; y devuelve TRUE si la posición válida en la lista l y FALSE en caso contrario.
boolean ValidatePosition (lista *l,posicion p);

//Efecto: Recibe una lista l y un entero n; y devuelve el elemento que se haya en la posicón n de la lista.
elemento Element(lista *l, int n);

//Efecto: Recibe una lista l y un entero n; y devuelve la posición del elemento que se haya en la posicón n de la lista.
posicion ElementPosition(lista *l, int n);

//Efecto: Recibe una lista l y devuelve el tamaño de la lista.
int Size (lista *l);

//Efecto: Recibe una lista l y devuelve TRUE en caso de que la lista este vacía y FALSE en caso contrario
boolean Empty (lista *l);

//Efecto: Recibe una lista l, una posición p, un elemento e y un valor booleano; el elemento e debera agregarse al frente de p si b es verdadero y atras de p en caso contrario.
void Insert (lista * l, posicion p, elemento e, boolean b);

//Efecto: Recibe una lista l y un elemento e ; el elemento e deberá agregarse al final de la lista
void Add (lista *l,elemento e);

//Efecto: Recibe una lista l y una posición p; el elemento en dicha posición será removido.
void Remove (lista *l,posicion p);

//Efecto: Recibe una lista l, una posición p y un elemento e; el elemento en dicha posición p será sustituido por e
void Replace (lista *l,posicion p, elemento e);

//FUNCIÓN PARA DEPURACIÓN, la cuál imprime las direcciones de memoria de los nodos y sus apuntadores a el siguiente y anterior a este.
void VerLigasLista(lista *l);

#endif    // __TADLista_H
