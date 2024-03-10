/*
IMPLEMENTACION DE LA LIBRERIA DEL TAD COLA LISTA (TADColaLista.h)
por Mauro Sampayo Hernández :)
*/

//LIBRERAS
#include "TADColaLista.h"
#include "TADListaDoblementeLigada.h"
#include <stdio.h>
#include <stdlib.h>

/*
void InitializeQueue(cola *c);
Descripción: Inicializar cola 
Recibe: Una cola por referancia c
Devuelve:
Observaciones: El usuario a creado una cola y c tiene la referencia a ella, si esto no ha pasado se ocasionara un error.
*/
void InitializeQueue(cola * c)
{
	Initialize(c->l);
	return;
}

/*
void Queue(cola * c, elemento e);
Descripción: Recibe una cola  y agrega un elemento al final de ella.
Recibe: por referancia c y elemento e (Elemento a encolar)
Devuelve:
Observaciones: El usuario a creado una cola y ha sido inicializada y c tiene la referencia a ella, si esto no ha pasado se ocasionara un error.
*/
void Queue(cola * c, elemento e)
{
	Add(c->l, e);
	return;
}

/*
elemento Dequeue(cola * c);
Descripción: Recibe una cola y devuelve el elemento que se encuentra al frente de esta, quiá¡ndolo de la cola.
Recibe: Una cola por referencia c
Devuelve: Elemento desencolado
Observaciones: El usuario a creado una cola y la cola tiene elementos, si no se genera un error y se termina el programa.
*/
elemento Dequeue(cola * c)
{
	if(Empty(c->l))
	{
		printf("ERROR (Dequeue): Subdesbrodamiento de cola");
		exit(1);
	}
	else
	{
		posicion p;
		elemento e;
		p=Final(c->l);
		e=Position(c->l, p);
		free(p);
		return e;	
	}	
}	


/*
boolean EmptyQueue(cola * c);
Descripción: Recibe una cola y TRUE si la cola esta vacia y FALSE en caso contrario
Recibe: Una cola por referencia c
Devuelve: boolean TRUE O FALSE
Observaciones: El usuario a creado una cola y la cola fue correctamente inicializada
*/
boolean EmptyQueue(cola * c)
{
	return Empty(c->l) ? TRUE : FALSE;
}

/*
elemento Front(cola * c);
Descripción: Recibe una cola y devuelve el elemento que se encuentra al frente de esta.
Recibe: Una cola or referencia c
Devuelve: Elemento del frente de la cola
Observaciones: El usuario a creado una cola,la cola fue correctamente inicializada, esta tiene elementos de lo contrario devolvera ERROR. 
*/
elemento Front(cola * c)
{
	if(Empty(c->l))
	{
		printf("ERROR (Front):  Se intenta acceder a un elemento inexistente");
		exit(1);
	}
	else
	{
		posicion p;
		elemento e;
		p=First(c->l);
		e=Position(c->l, p);
		return e;
	}	
}

/*
elemento FinalQueue(cola * c);
Descripción: Recibe una cola y devuelve el elemento que se encuentra al final de esta.
Recibe: Una cola por referencia c
Devuelve: Elemento del final de la cola
Observaciones: El usuario a creado una cola,la cola fue correctamente inicializada, esta tiene elementos de lo contrario devolvera ERROR.
*/

elemento FinalQueue(cola * c)
{
		if(Empty(c->l))
	{
		printf("ERROR (FinalQueue):  Se intenta acceder a un elemento inexistente");
		exit(1);
	}
	else
	{
		posicion p;
		elemento e;
		p=Final(c->l);
		e=Position(c->l, p);
		return e;
	}	
}

/*
int SizeQueue(cola * c);
Descripción: Recibe una cola y devuelve el nÃºmero de elemento que se encuentran en esta.
Recibe: Una cola por referencia c
Devuelve: Tamaño de la cola
Observaciones: El usuario a creado una cola,la cola fue correctamente inicializada
*/
int SizeQueue(cola * c)
{
	return Size(c->l);
}

/*
void ElementQueue(cola * c, int i);
Descripción: Recibe una cola y un número de elemento de 1 al tamaño de la cola y retorna el elemento de esa posición.
Devuelve: Elemento en la posicion i de la cola
Observaciones: El número i debera estar entre 1 y el tamaño de la cola, si esta es vacia o mas pequeña se provoca un error.
*/
elemento ElementQueue(cola * c, int i)
{
	if(i>0 && i<=Size(c->l))
	{
		elemento e;
		e=Element(c->l, i);
		return e;	
	}
	else
	{
		printf("ERROR (ElementQueue): Se intenta acceder a elemento inexistente");
	}
}

/*
void DestroyQueue(cola * c);
Descripción: Recibe una cola y la libera completamente.
Recibe: Una cola por referencia c
Devuelve:
Observaciones: La cola se destruye y se inicializa.
*/
void DestroyQueue(cola * c)
{
	Destroy(c->l);
}
