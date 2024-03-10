/*
IMPLEMENTACION TAD LISTA DOBLEMENTE LIGADA (TADListaDoblementeLigada.h)

DESCRIPCIÓN: Estructura de datos en donde se cumple: Los elementos se consultan, añaden y se remueven con base en posiciones dentro de un arreglo lineal el cual cuenta con un frente o cabeza y un final o cola.

        Frente                                                       Final
             ******    ******    ******    ******    ******    ******
     NULL <- *    * <- *    * <- *    * <- *    * <- *    * <- *    *
             * N1 *    * N2 *    * N3 *    * N4 *    * N5 *    * N6 *
             *    * -> *    * -> *    * -> *    * -> *    * -> *    * -> NULL
             ******    ******    ******    ******    ******    ******    

*/

//LIBRERAS
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include "TADListaDoblementeLigada.h" 

//FUNCIONES

/*
void Initialize(lista *l)
Descripción: Inicializa una lista 
Recibe: lista *l 
Devuelve: --
Observaciones: El usuario a creado una lista y l tiene la referencia a ella, si esto no ha pasado se ocasionara un error.
*/
void Initialize (lista *l)
{
	l->frente=NULL;
	l->final=NULL;
	l->tamanio=0;
	return;
}


/*
void Destroy(lista *l)
Descripción: Destruir una lista (Recibe una lista l y la libera completamente)
Recibe: lista *l (Referencia a la lista "l" a operar)
Devuelve: --
Observaciones: El usuario a creado una lista y l tiene la referencia a ella, si esto no ha pasado se ocasionara un error.
*/
void Destroy (lista *l)	
{
	nodo *aux;//Apuntador auxiliar a nodo
	
	while(l->frente!=NULL)
	{
		aux=l->frente;
		l->frente=l->frente->siguiente;//El nuevo frente es el siguiente
		free(aux);//Liberar el antiguo frente de memoria
	}

	l->final = NULL;
	l->tamanio = 0;
	
	return;
}

/*
posicion Final(lista *l)
Descripción: Recibe una lista l y regresa la posición del elemento al final de la lista 
Recibe: lista *l
Devuelve: Posición del nodo que contiene al elemeto final de la lista
Observaciones: El usuario a creado una lista y l tiene la referencia a ella, si esto no ha pasado se ocasionara un error.
*/
posicion Final (lista *l)
{
	return l->final;
}

/*
posicion First(lista *l)
Descripción: Recibe una lista l y regresa la posición del elemento al frente de la lista.
Recibe: lista *l 
Devuelve: 	Posición del nodo que contiene al elemento del frente de la lista
Observaciones: El usuario a creado una lista y l tiene la referencia a ella, si esto no ha pasado se ocasionara un error.
*/
posicion First (lista *l)
{
	return l->frente;
}

/*
posicion Following(lista *l, posicion p)
Descripción: Recibe una lista l, una posición p y devuelve la posición del elemento siguiente de p
Recibe: lista *l y posicion p 
Devuelve: Posición del nodo siguiente a la posicion dada
Observaciones: El usuario a creado una lista y l tiene la referencia a ella, p es una posicion valida de la lista, si esto no ha pasado se ocasionara un error.
*/
posicion Following (lista *l,posicion p)
{
	posicion aux;
	if(ValidatePosition(l,p))
	{
		aux=p->siguiente;
		return aux;
	}	
	else
	{
		printf("ERROR(Following): Posici%cn p es invalida", 162);
		exit(1);
	}
}


/*
posicion Previous(lista *l, posicion p)
Descripción: Recibe una lista L, una posición P y devuelve la posición del elemento anterior de P
Recibe: lista *l y posicion p 
Devuelve: Posición del nodo anterior a la posicion dada
Observaciones: El usuario a creado una lista y l tiene la referencia a ella, p es una posicion valida de la lista, si esto no ha pasado se ocasionara un error.
*/
posicion Previous (lista *l,posicion p)
{
	posicion aux;
	if(ValidatePosition(l,p))
	{
		aux=p->anterior;
		return aux;
	}	
	else
	{
		printf("ERROR(Previous): Posici%cn p es invalida", 162);
		exit(1);
	}	
}


/*
posicion Search(lista *l, elemento e)
Descripción: Recibe una lista l y un elemento e, regresa la posición que coincida exactamente con el elemento e.
Recibe: lista *l y un elemento e 
Devuelve: Posición del elemento en caso de ser encontrado, si no se encuentra se devuelve una posicion invalida
Observaciones: El usuario a creado una lista y l tiene la referencia a ella el elemento a buscar se compara directamente a nivel de bytes. 
*/
posicion Search (lista *l,elemento e)
{	
	posicion aux=l->frente;
	posicion aux2=l->final;
	
	while(aux!=NULL && aux2!=NULL)
	{
		if(memcmp(&aux->e,&e,sizeof(elemento))==0)
		{
			return aux;			
		}
		aux=aux->siguiente;
		
		if(memcmp(&aux2->e,&e,sizeof(elemento))==0)
		{
			return aux;			
		}
		aux2=aux2->anterior;
	}
	return NULL;
}

/*
elemento Position(lista *l, posicion p)
Descripción: Recibe una lista l, una posición p y devuelve el elemento en dicha posición. 
Recibe: lista *l y una posicion p
Devuelve: Elemento en la posicion dada, si la posicion es invalida se genera error.
Observaciones: La lista l es no vacía y la posicó³n p es una posición valida.
*/
elemento Position (lista *l,posicion p)
{
	elemento e;
	if(ValidatePosition(l,p))
		return p->e;
	else
	{
		printf("\nERROR (Position): Posicion p es invalida");
		exit(1);
	}
}

/*
boolean ValidatePosition(lista *l, posicion p)
Descripción: Recibe una lista l, una posición p y devuelve TRUE si la posición es una posición p valida en la lista l y FALSE en caso contrario.
Recibe: lista *l y una posicion p(Referencia a la lista "l" a operar y una posicion)
Devuelve: Booleano 
Observaciones:
*/
boolean ValidatePosition (lista *l,posicion p)
{
	posicion aux=l->frente;
	posicion aux2=l->final;
	
	while(aux!=NULL)
	{		
		if(aux==p) 
		{
			return TRUE;
		}	
		aux=aux->siguiente;	
		
		if(aux2==p)
		{
			return TRUE;
		}
		aux2=aux2->anterior;	
	}	
	return FALSE;	
}

/*
elemento Element(lista *l, int n)
Descripción: Recibe una lista y un índice (entre 1 y el tamaño de la lista) y devuelve el elemento que se encuentra en la lista en ese índice partiendo del frente de este =1 hacia atrás.
Recibe: lista *l y una entero
Devuelve: elemento 
Observaciones: Si la cola esta vacía o el índice se encuentra fuera del tamaño de la lista se produce error.
*/
elemento Element(lista *l, int n)
{
	elemento r;
	nodo *aux;
	int i;
	
	if (n>0&&n<=Size(l))//Si el elemento solicitado esta entre 1 y el tamaño de la lista
	{
		aux=l->frente;
		
		for(i=2;i<=n;i++)
		{
			aux=aux->siguiente;
		}
			
		r=aux->e;
	}
	else
	{
		printf("\nERROR (Element): Se intenta acceder a elemento %d inexistente",n);
		exit(1);		
	}
	return r;	
}

/*
posicion ElementPosition(lista *l, int n)
Descripción: Recibe una lista y un índice (entre 1 y el tamaño de la lista) y devuelve la posicián del elemento que se encuentra en la lista en ese índice partiendo del frente de este =1 hacia atrás.
Recibe: lista *l y una entero
Devuelve: posicion 
Observaciones: Si la cola esta vacÃ­a o el índice se encuentra fuera del tamaño de la lista se produce error.
*/
posicion ElementPosition(lista *l, int n)
{
	posicion aux=NULL;
	int i;
	
	if (n>0&&n<=Size(l))//Si el elemento solicitado esta entre 1 y el tamaño de la lista
	{
		aux=l->frente;
		for(i=2;i<=n;i++)
		{
			aux=aux->siguiente;
		}	
	}
	return aux;		
}

/*
int Size(lista * l);
Descripción: Recibe una lista y devuelve el número de elemento que se encuentran en esta.
Recibe: lista *l (Referencia a la lista "l")
Devuelve: int (Tamaño de la lista)
Observaciones: El usuario a creado una lista,la lista fue correctamente inicializada.
*/
int Size (lista *l)
{
	return l->tamanio;
}

/*
int Size(lista * l);
Descripción: Recibe una lista l y devuelve TRUE en caso de que la lista este vacía y FALSE en caso contrario.
Recibe: lista *l
Devuelve: boolean (TRUE o FALSE)
Observaciones: El usuario a creado una lista,la lista fue correctamente inicializada.
*/
boolean Empty (lista *l)
{
	return (l->tamanio==0) ? TRUE:FALSE;
}

/*
void Insert (lista * l, posicion p, elemento e, boolean b);
Descripción: Inserta un elemento e en la lista este deberá agregarse al frente de p si b es verdadero y atrás de p en caso contrario. Si p es invalida se insertará al frente de la lista
Recibe: lista *l, posición p, elemento e (Elemento a insertar en la lista), boolean b (Indicador de inserción antes de p=TRUE o despues de p =FALSE)
Devuelve: 
Observaciones: El usuario a creado una lista,la lista fue correctamente inicializada, si P es no valida o NULL, se insertará a e al frente de la lista.
*/
void Insert (lista * l, posicion p, elemento e, boolean b)
{
	nodo *aux,*aux2; //posicion aux;
	aux=malloc(sizeof(nodo));//Crear el nodo e insertar e
	
	if(aux==NULL)//Si no se puede reservar memoria para el nuevo nodo (ERROR de lista) 
	{
		printf("\nERROR (Insert): No se puede crear un nuevo nodo");
		exit(1);
		
	}
	
	aux->e=e;//Introducir a e en el nuevo nodo
	
	if(!ValidatePosition(l,p))//Si es invalida insertar al frente de la lista
	{
		if(l->final!=NULL) //Si la lista no esta vacia
		{
			aux->siguiente=l->frente;
			aux->anterior=NULL;//No hay elemento anterior, dado que nuestro auxiliar será el primer elemento de la lista
			l->frente->anterior=aux;//El apuntador "anterior" de el primer elemento se reconecta con aux
			l->frente=aux;
		}
		else//Si esta vacia
		{
			aux->siguiente=l->frente;//Cuando está vacía l->frente=NULL (aux->siguiente=NULL)
			aux->anterior=NULL;//No hay elemento anterior porque la lista estaba vacía
			l->frente=aux;
			l->final=aux;
			
		}
	}
	else//Si p es valida
	{
		if(b==FALSE)//Si p es FALSE deberá agregarse despues de la posicion p
		{
			if(p!=l->final)//Si p no es el final de la lista
			{
				aux->siguiente=p->siguiente;
				aux->anterior=p;
				p->siguiente->anterior=aux;//El apuntador "anterior" del elemento siguiente a p se conecta con aux
				p->siguiente=aux;//El apuntador "siguiente" del elemento p se conecta con aux
			}
			else //Si p es el final de la lista
			{
				aux->siguiente=p->siguiente;//Cuando está al final, p->siguiente, es decir l->final->siguiente va hacia un NULL (aux->siguiente=NULL)
				aux->anterior=p;//Donde la posición p es l->final (aux->anterior=l->final)
				p->siguiente=aux;//p es l->final
				l->final=aux;//No hay reconexión de el apuntador "anterior" del elemento siguiente, dado a que en este caso no existe dicho elemento
			}
		}
		else//Si p es TRUE deberá agregarse antes de la posicion p
		{
			aux2=Previous(l,p);//Si aux2 no existe (p es el frente)
	
			if(aux2==NULL)
			{
				aux->siguiente=l->frente;
				aux->anterior=NULL;//No hay elemento anterior, dado que nuestro auxiliar será el primer elemento de la lista
				l->frente->anterior=aux;//El apuntador "anterior" de el primer elemento se reconecta con aux
				l->frente=aux;					
			}
			else
			{
				aux2->siguiente=aux;
				aux->anterior=aux2;
				aux->siguiente=p;
				p->anterior=aux;				
			}
		}
	}
	
	l->tamanio++;//Aumentar el tamaño de la lista
	return;
}

/*
void Add (lista *l,elemento e);
Descripción: Recibe una lista l y un elemento e, se agrega a e al final de la lista l.
Recibe: lista *l, elemento e 
Devuelve: 
Observaciones: El usuario a creado una lista,la lista fue correctamente inicializada.
*/
void Add (lista *l,elemento e)
{
	posicion aux;	
	aux=malloc(sizeof(nodo));//Si no se puede reservar memoria para el nuevo nodo (ERROR de lista) 
	
	if(aux==NULL)
	{
		printf("\nERROR (Add): No se puede crear un nuevo nodo");
		exit(1);
	}
	
	aux->e=e;
	
	if(l->tamanio==0)//Si la lista esta vacia (l->final==NULL&&l->frente==NULL)
	{
		aux->siguiente=NULL;
		aux->anterior=NULL;
		l->frente=aux;
		l->final=aux;								
	}
	else//Si la lista no esta vacia
	{
		l->final->siguiente=aux;
		aux->anterior=l->final;
		aux->siguiente=NULL;
		l->final=aux;
	}

	l->tamanio++;
	return;
}

/*
void Remove (lista *l,posicion p);
Descripción: Recibe una lista l y una posición p, el elemento en la posición p serÃ¡ removido.
Recibe: lista *l, posicion p (posicion a eliminar en la lista)
Devuelve: 
Observaciones: El usuario a creado una lista,la lista fue correctamente inicializada, la posicion p es valida.
*/
void Remove (lista *l,posicion p)
{
	posicion aux;
	//Si p es valida
	if(ValidatePosition(l,p))
	{
		if(p==l->final&&p==l->frente)//Si la p es frente y final (Solo hay uno en la lista)
		{
			free(p);
			l->final=NULL;
			l->frente=NULL;
			l->tamanio=0;
		}		
		else if(p==l->final)//Si la p es el final
		{
			aux=l->final->anterior;//Previous(l,p)
			aux->siguiente=NULL;
			l->final=aux;
			l->tamanio--;
			free(p);
		}
		else if(p==l->frente)//Si la p es el frente
		{
			l->frente=l->frente->siguiente; //l->frente=p->siguiente;
			free(p);
			l->frente->anterior==NULL;
			l->tamanio--;
		}
		else//Si p esta en medio
		{
			aux=Previous(l,p);
			aux->siguiente=p->siguiente;//Reconecta el nodo "siguiente" de aux a el elemento siguiente a p
			p->siguiente->anterior=aux;//Reconecta el nodo "anterior" de el elemento siguiente a p, hacia aux
			free(p);
			l->tamanio--;
		}		
	}
	else
	{
		printf("\nERROR (Remove): Posici%cn p es invalida", 162);
		exit(1);
	}
	
	return;
}


/*
void Replace (lista *l,posicion p, elemento e);
Descripción: Recibe una lista l, una posición p y un elemento e, el elemento en la posición p será sustituido por e
Recibe: lista *l (Referencia a la lista "l"), posicion p (posicion a remplazar en la lista), elemento e (elemento que remplazara al existente en p)
Devuelve: 
Observaciones: El usuario a creado una lista,la lista fue correctamente inicializada, la posicion p es valida.
*/
void Replace (lista *l,posicion p, elemento e)
{
	if(ValidatePosition(l,p))//Si la posicion p existe
	{
		p->e=e; //Remplazar a e
	}
	else
	{
		printf("\nERROR (Replace): No se puede remplazar una posicion invalida");
		exit(1);
	}
	return;
}

/********************************************************************************
//FUNCION PARA DEPURACIÓN
********************************************************************************/
void VerLigasLista(lista *l)
{
	posicion aux;	
	aux=l->frente;	
	printf("\n*************************************************************");
	while(aux!=NULL)
	{
		printf("\nPosicion=%p\tSiguiente=%p\tAnterior=%p",aux, aux->siguiente, aux->anterior);
		aux=aux->siguiente;
	}
	printf("\n*************************************************************");

	return;
}
