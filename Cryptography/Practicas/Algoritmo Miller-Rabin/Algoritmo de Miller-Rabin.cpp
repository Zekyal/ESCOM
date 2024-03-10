#include <stdio.h>
#include <stdlib.h>
#include <time.h> 

void TituloAlgoritmo();
bool DeterminarNumPrimo(long long int);
bool MillerRabinTest(long long int, long long int);
long long int CalculoModulo(long long int, unsigned long long int, long long int);

int main()
{
	long long int num;
	
    for(;;)
    {
    	TituloAlgoritmo();
    	printf("Numero n = ");
    	scanf("%lld", &num);
    	
    	if (DeterminarNumPrimo(num))
    		printf("\n%lld es un numero Primo\n", num);
    	else
    		printf("\n%lld no es un numero Primo\n", num);
	}
 
    return 0;
}

/*	Función Ttulo Algoritmo
	Uso: Aplica un formato para el tpitulo del algoritmo	*/
void TituloAlgoritmo()
{
	printf("%c", 201);
	for(int i=0; i<=38; i++)
		printf("%c", 205);
	printf("%c\n", 187);	
	
	printf("%c   +++ Algoritmo de Miller-Rabin +++   %c\n", 186, 186);
	
	printf("%c", 200);
	for(int i=0; i<=38; i++)
		printf("%c", 205);
	printf("%c\n\n", 188);	
}

/*	Función CalculoModulo
	Uso: Realiza el cálculo de la operación a^m mod n
	Recibe: Elementos a, m y numero n necesarias para llevara a cabo ala operacion
	Retorna: Resultado de la operacion	*/
long long int CalculoModulo(long long int x, unsigned long long int y, long long int n)
{
    long long int res = 1;
    x = x % n; 
                
    while (y > 0)
    {
        // Deetermina si y es odd por medio de una operación binaria AND con 1
        if (y & 1)
            res = (res*x) % n;
 
 		// Ls valores de x e y se actualizan
        y = y>>1; //Realiza un corrimiento a al derecha sobre m
        x = (x*x) % n;
    }
    
    return res;
}

/*	Función MillerRabinTest
	Uso: Aplica el algoritmo de Miller-Rabin 
	Recibe: m y Número n
	Retorna: False si el numero es un compuesto y true si el numero es un primo	*/
bool MillerRabinTest(long long int m, long long int n)
{
    //Generar un nnúmero aleatoriuo entre 1<=a<=n-1
    long long int a = 1 + rand() % (n - 1);
 
    // Realizar el cálculo de b = a^m mod n
    long long int b = CalculoModulo(a, m, n);
 
    if (b == 1  || b == n-1)
       return true;
 
    //Ciclo a realizar en caso de que ninguna condición se haya cumplido aún
    while (m != n-1)
    {
        b = (b * b) % n;
        m *= 2;
 
        if (b == 1)      
			return false;
        if (b == n-1)    
			return true;
    }
 
    return false;
}
 
/*	FunciónDeterminarNumPrimo
	Uso: Determina si un npumero es primo o no por medio del uso del Algoritmo deMiller-Rabin
	Recibe: Número n
	Retorna: False si el numero es un compuesto y true si el numero es un primo	*/
bool DeterminarNumPrimo(long long int n)
{
    // Casos especiales
    if (n <= 1 || n == 4)  
		return false;
    if (n <= 3) 
		return true;
 
    long long int m = n - 1;
    //Se inicializa por defecto k con 100 para asegurar una mayor precisión al omento de determinar si un numero es primo o compuesto
    long long int k = 10000;
    
    //Obteniendo los valores de k y m
    while (m % 2 == 0)
	{
		m /= 2;
		k++;
	}
 
    // Iterar k numero de veces
    for (int i = 0; i < k; i++)
         if (!MillerRabinTest(m, n))
              return false;
 
    return true;
}
