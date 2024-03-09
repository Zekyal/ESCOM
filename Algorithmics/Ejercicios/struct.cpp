#include<stdio.h>

int main()
{
	struct paises
	{
		long double poblacion;
		char *capital;
	}Chile, Kenia, NuevaZelanda;
	
	Chile.poblacion=17574003;
	Chile.capital="Santiago";
	Chile=NuevaZelanda;
	
	printf("%s", Chile.poblacion);
	
	return 0;
}
