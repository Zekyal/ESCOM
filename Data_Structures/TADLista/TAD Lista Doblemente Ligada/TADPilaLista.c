/*
IMPLEMENTACION DE LA LIBRERIA DEL TAD PILA LISTA (TADPilaLista.h)
por Mauro Sampayo Hern�ndez :)
*/

//LIBRERAS
#include <stdio.h>
#include <stdlib.h>
#include "TADPilaLista.h"
#include "TADListaDoblementeLigada.h"

//DEFINICI�N DE FUNCIONES

/*
void InitializeStack(pila *s);
Descripci�n: Inicializa una pila
Recibe: Una pila por referencia s
Devuelve:
Observaciones: El usuario a creado una pila y s tiene la referencia a ella, si esto no ha pasado se ocasionara un error.
*/
void InitializeStack(pila *s)
{
	Initialize((s->l));
	return;
}

/*
void Push(pila *s, elemento e);
Descripci�n: Empilar un elemento a la pila
Recibe: Una pila por referencia s, y el elemento a empilar 
Devuelve:
Observaciones: El usuario a creado una pila y s tiene la referencia a ella; s ya ha sido inicializada.
*/
void Push(pila *s, elemento e)
{
	Add((s->l), e);
	return;
}


/*
void Pop(pila *s);
Descripción: Desempilar un elemento de la pila
Recibe: Unja pila por referencia s
Devuelve: Elemento e extraido de la pila
Observaciones: El usuario a creado una pila y s tiene la referencia a ella, s ya ha sido inicializada. Ademas no se valida si la pila esta vacia 
antes de desempilar.
*/
elemento Pop(pila *s)
{
	if(!Empty((s->l)))
	{
		elemento e;
		posicion p;
		p=Final((s->l));
		e=Position((s->l), p);
		Remove((s->l), p);
		return e;
	}	
	else
	{
		printf("ERROR(Pop): Subdesbordamiento de pila");
		exit(1);
	}
}

/*
boolean EmptyStack(pila *s);
Descripci�n: Validar si la pila est� vac�a
Recibe: Una pila por referencia s
Devuelve: boolean TRUE � FALSE depende de el caso
Observaciones: El usuario a creado una pila y s tiene la referencia a ella; s ya ha sido inicializada.
*/
boolean EmptyStack(pila *s)
{
	return Empty((s->l)) ? TRUE:FALSE;	
}

/*
elemento Top(pila *s);
Descripci�n: Obtener el "elemento" del tope de la pila
Recibe: Una pila por referencia s
Devuelve: Elemento del tope de la pila
Observaciones: El usuario a creado una pila y s tiene la referencia a ella, s ya ha sido inicializada. Ademas no se valida si la pila esta vacia antes de 
consultar al elemento del tope
*/
elemento Top(pila *s)
{
	if(!Empty((s->l)))
	{
		elemento e;
		posicion p;
		p=Final((s->l));
		e=Position((s->l), p);
		return e;
	}
	else
	{
		printf("ERROR(Top): Pila vac�a");
		exit(1);
	}
}

/*
int SizeStack(pila *s);
Descripción: Obtener el n�mero de elementos en la pila
Recibe: Una pila por referencia s
Devuelve: Tama�o de la pila 
Observaciones: El usuario a creado una pila y s tiene la referencia a ella; s ya ha sido inicializada.
*/
int SizeStack(pila *s)
{
	return Size((s->l));
}

/*
void DestroyStack(pila *s);
Descripci�n: Borra a todos los elementos en a la pila de memoria
Recibe: Una pila por referencia s
Devuelve: 
Observaciones: El usuario a creado una pila y s tiene la referencia a ella; s ya ha sido inicializada.
*/
void DestroyStack(pila *s)
{
	Destroy((s->l));
	return;
}
