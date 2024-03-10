/*Comiplacion: gcc -o exp Exponenciacion.c TADPilaDin.c*/
#include<stdio.h>
#include<stdlib.h>
#include "TADPilaDin.h"

void TituloAlgoritmo();
long long int Exponenciacion(long long int, long long int, long long int);
void ConvertirBinario(long long int);

elemento e;
pila stack;

int main()
{
	long long int x, a, n;
	
    for(;;)
    {
    	TituloAlgoritmo();
    	printf("Inserte los numeros de acuerdo a la expresion x^(a) mod n:\n");
    	printf("\tx = ");
    	scanf("%lld", &x);
    	printf("\ta = ");
    	scanf("%lld", &a);
    	printf("\tn = ");
    	scanf("%lld", &n);
    	printf("\n\tz= %lld\n", Exponenciacion(x, a, n));
	}
 
    return 0;
}

/*	Función Ttulo Algoritmo
	Uso: Aplica un formato para el tpitulo del algoritmo	*/
void TituloAlgoritmo()
{
	printf("%c", 201);
	for(int i=0; i<=40; i++)
		printf("%c", 205);
	printf("%c\n", 187);	
	
	printf("%c   +++ Algoritmo de Exponenciacion +++   %c\n", 186, 186);
	
	printf("%c", 200);
	for(int i=0; i<=40; i++)
		printf("%c", 205);
	printf("%c\n\n", 188);	
}

/*	Función Exponenciacion
	Uso: Realiza el algoritmo de la exponenciación
	Recibe: Elementos x, a y n de la ecuación x^(a) mod n 
	Retorna: Resultado de la operacion x^(a) mod n	*/
long long int Exponenciacion(long long int x, long long int a, long long int n)
{
	long long int z=1;
	ConvertirBinario(a);
	
	do{
		z = (z*z)%n;
		
		if(Pop(&stack).d){
			z = (z*x)%n;
		}
	}while(!Empty(&stack));
	
	Destroy(&stack);
	return z;
}

/*	Función ConvertirBinario
	Uso: Realiza la cpnversión de un numero decimal a binario, almacenando cada uno de sus bits dentro de una pila
	Recibe: Numero decimal a convertir a binario	*/
void ConvertirBinario(long long int a)
{
	Initialize(&stack);
	long long int cociente = 0, aux = a;
		
	if(a==0){
		e.d = 0;
		Push(&stack, e);
	}
	else if(a==1)
	{
		e.d = 1;
		Push(&stack, e);	
	}
	else
	{
		while(cociente!=1)
		{
			cociente = aux/2;
			e.d = aux%2; //residuo
			aux = cociente;
			Push(&stack, e);
		}
		
		e.d = (int)cociente;
		Push(&stack, e);
	}
	
	/*
	int aux2 = Size(&stack);
	printf("\n\n%d a Binario: ", a);
	for(int i=0; i<aux2; i++)
		printf("%d", Pop(&stack));
	printf("\n", a);	
	*/
}
