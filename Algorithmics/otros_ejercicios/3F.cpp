//TERCERA FORMA

#include<stdio.h>
#include<string.h>
#define TAM 30

int main()
{
	char palabra[TAM]="\0";
	printf("Introduce una palabra o frase: ");
	scanf("%s", &palabra);
	printf("Tu palabra es: %s", palabra);//Solo imprime la primara palabra :'v
}
