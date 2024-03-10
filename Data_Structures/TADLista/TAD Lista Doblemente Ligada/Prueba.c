#include "TADListaDoblementeLigada.h"
#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#define TAM 10

void ImprimirLista(lista *l);
void ImprimirEncabezado(int);

int main()
{
	int i, opcion, pos, b, ciclo=1;
	lista prueba;
	elemento e;
	posicion p, p2;
	Initialize(&prueba);
	
	
	printf("***************************************************************************************************\n");
	printf("*            PROGRAMA DE PRUEBA PARA LAS FUNCIONES DEL <<TAD LISTA DOBLEMENTE LIGADA>>            *\n");
	printf("***************************************************************************************************\n");	
	Destroy(&prueba);
	
	for(i=1; i<=TAM; i++)
	{
		e.c='A'+(i-1);
		Add(&prueba, e);
	}
	
	do{
		ImprimirLista(&prueba);
		printf("\n\nSeleccione la funci%cn que quiera probar sobre la lista:(Nota: No tadas las funciones est%cn incluidas en el men%c, debido a que ya se hayan presentes dentro del c%cdigo del programa)\n\n", 162, 160, 163, 162);
		printf("1. void Destroy (lista *l)\n2. posicion Final (lista *l)\n3. posicion First (lista *l)\n4. posicion Following (lista *l,posicion p)\n5. posicion Previous (lista *l)\n6. posicion Search (lista *l,elemento e)\n");
		printf("7. elemento Position (lista *l,posicion p)\n8. boolean ValidatePosition (lista *l,posicion p)\n9. elemento Element(lista *l, int n)\n10. void Insert (lista * l, posicion p, elemento e, boolean b)\n");
		printf("11. void Add (lista *l,elemento e)\n12. void Remove (lista *l,posicion p)\n13. void Replace (lista *l,posicion p, elemento e)\n14. void VerLigasLista(lista *l)");
		scanf("%d", &opcion);
	
		system("cls");
		ImprimirEncabezado(opcion);
		printf("Lista Original:\n");
		ImprimirLista(&prueba);

		switch(opcion)
		{
			case 1:
				Destroy(&prueba);//Destruimos lista
				printf("\n\nLista despu%cs de Destruirla:\n", 130);
				ImprimirLista(&prueba);
				exit(1);
			case 2:
				p=Final(&prueba);//Posición de último elemento de la lista
				e=Position(&prueba, p);//Último elemento de la lista
				printf("\n\nLa posici%cn final de esta lista es: %d; y su elemento es %c", 162, p, e.c);
				break;
			case 3:
				p=First(&prueba);//Posición deL primer elemento de la lista
				e=Position(&prueba, p);//Primer elemento de la lista
				printf("\n\nLa posici%cn inicial de esta lista es: %d; y su elemento es %c", 162, p, e.c);
				break;
			case 4:
				printf("\n\nPosici%cn: ", 162);
				scanf("%d", &pos);
				p=ElementPosition(&prueba, pos);//Obtenemos la dirección de memoria de el elemento número "pos"
				p2=Following(&prueba, p);//Con la dirección de memoria ya obtenida, se procede a obtener la posición siguiente al elemento "pos"
				e=Position(&prueba, p2);//Elemento de la posición siguiente al elemento "pos"
				printf("La posici%cn siguiente es: %d; y su elemento es %c", 162, p2, e.c);	
				break;	
			case 5:
				printf("\n\nPosici%cn: ", 162);
				scanf("%d", &pos);
				p=ElementPosition(&prueba, pos);//Obtenemos la dirección de memoria de el elemento número "pos"
				p2=Previous(&prueba, p);//Con la dirección de memoria ya obtenida, se procede a obtener la posición anterior al elemento "pos"
				e=Position(&prueba, p2);//Elemento de la posición anterior al elemento "pos"
				printf("La posici%cn anterior es: %d; y su elemento es %c", 162, p2, e.c);
		    	break;
			case 6:
				printf("\n\nElemento: ");
				scanf(" %c", &e.c);
				p=Search(&prueba, e);//Bucamos la posición del elemento e si existe
				printf("La posici%cn donde se ubica el elemento %c es: %d", 162, e.c, p);
	    		break;
			case 7:
				printf("\n\nPosici%cn: ", 162);
				scanf("%d", &pos);
				p=ElementPosition(&prueba, pos);//Obtenemos la dirección de memoria de el elemento número "pos"
				e=Position(&prueba, p);	//Obtenemos el elemento de el número "pos"
				printf("El elemento en la posici%cn %d es: %c", 162, pos, e.c);
				break;	
			case 8:
				printf("\n\nPosici%cn: ", 162);
				scanf("%d", &pos);
				p=ElementPosition(&prueba, pos);
			
				if(!ValidatePosition(&prueba, p))
				{
					printf("Posici%cn inv%clida", 162, 160);
				}
				else
				{
					printf("Posici%cn v%clida", 162, 160);
				}
			
				break;
			case 9:
				printf("\n\nPosici%cn: ", 162);
				scanf("%d", &pos);
				e=Element(&prueba, pos);//Obtenemos el elemento "pos"
				printf("El elemento de la posici%cn %d es: %c", 162, pos, e.c);
				break;
			case 10:
				printf("\n\nPosici%cn: ", 162);
				scanf("%d", &pos);
				p=ElementPosition(&prueba, pos);//Obtenemos la dirección de memoria de el elemento número "pos"
				printf("Elemento a introducir(char): ");
				scanf(" %c", &e.c);
				printf("TRUE(1) o FALSE(0): ");
				scanf("%d", &b);
				Insert(&prueba, p, e, b);
				printf("\n\nLista Nueva:\n");
				ImprimirLista(&prueba);
				break;
			case 11:
				printf("Elemento a introducir(char): ");
				scanf(" %c", &e.c);
				Add(&prueba, e);
				printf("\n\nLista Nueva:\n");
				ImprimirLista(&prueba);
				break;
			case 12:
				printf("\n\nPosici%cn: ", 162);
				scanf("%d", &pos);
				p=ElementPosition(&prueba, pos);//Obtenemos la dirección de memoria de el elemento número "pos"
				Remove(&prueba, p);
				printf("\n\nLista Nueva:\n");
				ImprimirLista(&prueba);
				break;
			case 13:
				printf("\n\nPosici%cn: ", 162);
				scanf("%d", &pos);
				p=ElementPosition(&prueba, pos);//Obtenemos la dirección de memoria de el elemento número "pos"
				printf("\n\nElemento a introducir(char): ");
				scanf(" %c", &e.c);
				Replace(&prueba, p, e);
				printf("\n\nLista Nueva:\n");
				ImprimirLista(&prueba);
				break;
			case 14:
				printf("\n");
				VerLigasLista(&prueba);
				break;
			default:
				printf("Comando no v%clido", 160);
				break;
		}
		
		printf("\n");
		system("pause");
		system("cls");
	}while(ciclo=1);
		
	return 0;
}

void ImprimirEncabezado(int opcion)
{
	printf("***************************************************************************************************\n");

	switch(opcion)
	{
		case 1:
			printf("                                PRUEBA DE: void Destroy (lista *l)                                 \n");
			break;
		case 2:
			printf("                               PRUEBA DE: posicion Final (lista *l)                                \n");
			break;
		case 3:
			printf("                               PRUEBA DE: posicion First (lista *l)                                \n");
			break;
		case 4:
			printf("                             PRUEBA DE: posicion Following (lista *l)                              \n");
			break;
		case 5:
			printf("                             PRUEBA DE: posicion Previous (lista *l)                               \n");
			break;
		case 6:
			printf("                              PRUEBA DE: posicion Search (lista *l)                                \n");
			break;
		case 7:
			printf("                             PRUEBA DE: elemento Position (lista *l)                               \n");
			break;
		case 8:
			printf("                          PRUEBA DE: boolean ValidatePosition (lista *l)                           \n");
			break;
		case 9:
			printf("                              PRUEBA DE: elemento Element (lista *l)                               \n");
			break;
		case 10:
			printf("                                 PRUEBA DE: void Insert (lista *l)                                 \n");
			break;
		case 11:
			printf("                                  PRUEBA DE: void Add (lista *l)                                   \n");
			break;
		case 13:
			printf("                                PRUEBA DE: void Remove (lista *l)                                  \n");
			break;
		case 14:
			printf("                            PRUEBA DE: void VerLigasLista (lista *l)                               \n");
			break;
	}
	
	printf("***************************************************************************************************\n\n");
}

void ImprimirLista(lista *l)
{
	int j;
	elemento e;
	
	if(Empty(l))
	{
		printf("La Lista no contiene ning%cn elemento", 163);
	}
	else
	{
		for(j=1; j<=Size(l); j++)
		{
			e=Element(l, j);
			printf("\nElemento %i -> %c", j, e.c);
		}	
	}
}
