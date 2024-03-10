#include <stdio.h>

void TituloAlgoritmo();
void InversoMultiplicativo(int, int);
int AlgoritmoExtendidoEuclides(int, int, int*, int*);

int main()
{
    int n, m;
    
    for(;;)
    {
    	TituloAlgoritmo();
		printf("Modulo m = ");
    	scanf("%d", &m);
    	printf("Numero n = ");
    	scanf("%d", &n);
    	InversoMultiplicativo(n, m);
	}
    
    return 0;
}

/*	Función Ttulo Algoritmo
	Uso: Aplica un formato para el tpitulo del algoritmo	*/
void TituloAlgoritmo()
{
	printf("%c", 201);
	for(int i=0; i<=35; i++)
		printf("%c", 205);
	printf("%c\n", 187);	
	
	printf("%c   +++ Inverso Multiplicativo +++   %c\n", 186, 186);
	
	printf("%c", 200);
	for(int i=0; i<=35; i++)
		printf("%c", 205);
	printf("%c\n\n", 188);	
}

/*	Función Inverso Multiplicativo
	Uso: Obtiene los inversos multiplicativos de dos números a partir del Algoritmo Extendido de Euclides
	Recibe: Modulo m y Número n
	Retorna: Inverso multiplicativo inv	*/
void InversoMultiplicativo(int n, int m)
{
    int x, y;
    int g = AlgoritmoExtendidoEuclides(n, m, &x, &y);
    
    if (g != 1)
        printf ("\nEl numero no tiene Inverso Multiplicativo\n");
    else
    {
        // Convierte el resultado del Algortimo Extendido de Euclides a positivo
        int inv = (x % m + m) % m;
        printf("\nInverso Multiplicativo = %d\n", inv);;
    }
}

/*	Función AlgoritmoExtendidoEuclides
	Uso: Obtiene el mcd de dos números a partir del Algoritmo Extendido de Euclides
	Recibe: Modulo b, Número n, y apuntadores a las variabkles x e y
	Retorna: Minimo Común Divisor mcd	*/
int AlgoritmoExtendidoEuclides(int a, int b, int* x, int* y)
{
    if (a == 0)
    {
        *x = 0, *y = 1;
        return b;
    }
     
    // Llamada recursiva para almacenar los resultados
    int x1, y1;
    int mcd = AlgoritmoExtendidoEuclides(b % a, a, &x1, &y1);
 
    // Actualiza los valores de x e y
    *x = y1 - (b / a) * x1;
    *y = x1;
 
    return mcd;
}
 


