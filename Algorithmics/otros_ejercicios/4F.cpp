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
	gets(palabra2);//Lee toda la cadena de caracteres sin importar la introducción de espacio o enters que se puedan contar como vacíos(\0) en el scanf 
	strcpy(palabra3,strcat(palabra,palabra2));
	puts(palabra3);//Coloca la cadena de caracteres pero solo tiene un parámetros (no puede imprimir ningún otro elemento) y coloca un salto de línea
}

//strcat(,) --> Concatendor de string de dos parámetos 
//strcpy(,) --> Copiador de string de dos parámetos (destino, fuente)
