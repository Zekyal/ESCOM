//CUARTA FORMA

#include<stdio.h>
#include<string.h>
#define TAM 40

int main()
{
	char palabra[TAM]="Tu palabra es: ";
	char palabra2[TAM]="\0";
	char palabra3[TAM+TAM]="\0";
	printf("Introduce una palabra o frase: ");
	gets(palabra2);//Lee toda la cadena de caracteres sin importar la introducci�n de espacio o enters que se puedan contar como vac�os(\0) en el scanf 
	strcpy(palabra3,strcat(palabra,palabra2));
	puts(palabra3);//Coloca la cadena de caracteres pero solo tiene un par�metros (no puede imprimir ning�n otro elemento) y coloca un salto de l�nea
}

//strcat(,) --> Concatendor de string de dos par�metos 
//strcpy(,) --> Copiador de string de dos par�metos (destino, fuente)
