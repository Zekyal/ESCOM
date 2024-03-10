/*Comiplacion: gcc -o curva2 curva2.c TADPilaDin.c -lm*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include "TADPilaDin.h"

void TituloAlgoritmo();
bool DeterminarNumPrimo(long long int);
bool MillerRabinTest(long long int, long long int);
long long int Modulo(long long int, unsigned long long int, long long int);
long long int Exponenciacion(long long int, long long int, long long int);
void ConvertirBinario(long long int);
void ElementoGenerador(long long int, long long int, long long int, long long int);
void Comprobacion(long long int);
long long int InversoMultiplicativo(long long int, long long int);
long long int AlgoritmoExtendidoEuclides(long long int, long long int, long long int*, long long int*);

elemento e, e2, e3;
pila stack, stack2, stack3;
int i;

int main()
{
	long long int a, b, x, y, p, q, k;
	long long int c, aux;
	int bandera, bandera2;
	
    for(;;)
    {
    	TituloAlgoritmo();
    	bandera = 0;
    	
    	/*------Proposicion de los vaklores de "a" y "b"------*/
    	
    	printf("Proponga un numero numero impar a > 3:\n");
    	printf("\ta = ");
    	scanf("%lld", &a);
    	
    	if(a<=3){
    		printf("--ERROR: Valor de a es menor a 3");
    		break;
		}
    	
    	printf("Proponga un numero numero par b >= 2:\n");
    	printf("\tb = ");
    	scanf("%lld", &b);
    	
    	if(b<2){
    		printf("--ERROR: Valor de b es menor a 2");
    		break;
		}
    	
    	/*------Obtención del valor de "p"------*/
    	
		p = pow(a,2) + pow(b,2);
		c = a + b;
		//printf("p = %lld\n", p);
		
		/*------Comprobación de que "p" es un número primo impar válido------*/
		
		while(bandera == 0){
			if(DeterminarNumPrimo(p) && Modulo(p, 1, 4)==1 && Modulo(c, 1, 4)==1){
				bandera = 1;
				
				/*------Calculo del valor de "q"------*/
				q = (p + 1 + (2 * a)) / 4;
				printf("Inserte un valor para q-1:\n");
    			printf("\tq - 1 = ");
    			scanf("%lld", &q);
			}
			else
				b = b + 2;
		}
		
		/*------Comprobacion de que "q" es un número primo------*/
		
		//if(DeterminarNumPrimo(q)){
			/*------Insertamos valores de a = (x0, y0), 1 < x0,y0 < p-1------*/
			
			printf("\nInserte los valores de alfa = (x0, y0):\n");
	    	printf("\tx0 = ");
    		scanf("%lld", &x);
    	
    		if(x<1 || x>(p-1)){
    			printf("ERROR: Valor de x0 no valido");
	    		break;
			}
    	
	    	printf("\ty0 = ");
    		scanf("%lld", &y);
    		
			if(y<1 || y>(p-1)){
    			printf("ERROR: Valor de y0 no valido");
	    		break;
			}
			
			/*------Obtencion del valor de k------*/
			
			//Obtencion del valor (x0)^-1
			aux = Modulo(x, 1, p);
			aux = InversoMultiplicativo(aux, p);
			//Obtencion de k = (x0^3 - y0^2)*(x0)^-1 mod p
			k = (pow(x, 3) - pow(y, 2)) * aux;
			k = Modulo(k, 1, p);
			//k = 68445;
			
			/*------Impresion de datos------*/
			
			printf("______________________________________________\n");
			printf("\tValor de p = %lld\n", p);
			printf("\tValor de q = %lld\n", q);
			printf("\talfa = (x0, y0) = (%lld , %lld)\n", x, y);
			printf("\tValor de k = %lld\n", k);
			printf("______________________________________________\n");
			
			/*------CURVA ELIPTICA------*/
			ConvertirBinario(q);
			ElementoGenerador(x, y, p, k);
			
			e3 = Pop(&stack3);	
			/*if(e3.x==x && e3.y==(p-y)){
				printf("Se cumple que:\n");
				printf("\tx1 = x0 && y1 = (p-y0)\n");
			}
			else{
				printf("ERROR. (alfa) = (x0, y0) no es un elemento generador\n");
				exit(1);
			}*/
			
			printf("\nLa suma de los puntos con 1 binario es:");
			printf("\t%lld(%lld, %lld) = (%lld, %lld)\n\n", q, x, y, e3.x, e3.y);
			
			/*printf("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n");
			printf("\tCURVA ELIPTICA = y^(3) = x^(3) - %lldx mod %lld\n", k, p);
			printf("\tELEMENTO GENERADOR = (%lld, %lld)\n", x, y);
			printf("\tORDEN = %lld\n", q);
			printf("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n\n");
		}
		else
			printf("--ERROR: Valor de q no es primo");*/
			
		Destroy(&stack);
		Destroy(&stack2);
		Destroy(&stack3);
	}
 
    return 1;
}

/*	Función Ttulo Algoritmo
	Uso: Aplica un formato para el tpitulo del algoritmo	*/
void TituloAlgoritmo()
{
	printf("%c", 201);
	for(i=0; i<=35; i++)
		printf("%c", 205);
	printf("%c\n", 187);	
	
	printf("%c       +++ Curva Eliptica +++       %c\n", 186, 186);
	
	printf("%c", 200);
	for(i=0; i<=35; i++)
		printf("%c", 205);
	printf("%c\n\n", 188);	
}

/*	Función Modulo
	Uso: Realiza el cálculo de la operación a^m mod n
	Recibe: Elementos a, m y numero n necesarias para llevara a cabo ala operacion
	Retorna: Resultado de la operacion	*/
long long int Modulo(long long int x, unsigned long long int y, long long int n)
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
    long long int b = Modulo(a, m, n);
 
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
    for (i = 0; i < k; i++)
         if (!MillerRabinTest(m, n))
            	return false;
 
    return true;
}

void ElementoGenerador(long long int x, long long int y, long long int p, long long int k){
	long long int x0, y0, x1, y1, lambda, aux;
	int aux2 = 1;
	x0 = x;
	y0 = y;
	
	Initialize(&stack2);
	
	/*------COMPROBACION DE QUE ALFA ES UN ELEMENTO GENERADOR------*/
	
	for(int j=0; j<Size(&stack); j++){
		if(j == 0){
			e.x = x0;
			e.y = y0;
			Push(&stack2, e);
			printf("\tx%d.	%d(alfa) = (%lld, %lld)\n", j, aux2, x, y);
		}
		else{
			//lambda = (3*x0-a)*(2*y0)^-1 mod p
			aux = 2*y0;//Para (2*y0)^-1
			aux = Modulo(aux, 1, p);
			aux = InversoMultiplicativo(aux, p);
			
			lambda = ((3*(x0 * x0))-k) * aux;
			lambda = Modulo(lambda, 1, p);
			e.l = lambda;
			
			//x1 = (lambda)^2-(2*x0) mod p
			x1 = (lambda * lambda) - (2 * x0);
			x1 = Modulo(x1, 1, p);
			e.x = x1;
			
			//y1 = lambda(x0-x1)-y0 mod p
			y1 = (lambda * (x0 - x1)) - y0 ;
			
			if(y1 < 0){
				while(y1 < 0)
					y1 = y1 + p;
			}
			else
				y1 = Modulo (y1, 1, p);
			e.y = y1;
			
			Push(&stack2, e);
			aux2 = pow(2, j);
			printf("\tx%d.	%d(alfa) = (%lld, %lld)		Lambda = %lld\n", j, aux2, x1, y1, lambda);
			x0 = x1;
			y0 = y1;
		}
	}
	
	printf("______________________________________________\n");
	Comprobacion(p);
}

void Comprobacion(long long int p){
	long long int x1, y1, lambda, aux;
	int tam = Size(&stack);
	int j = 0, cont = 0;
	
	Initialize(&stack3);
	
	for(j=0; j<tam; j++){
		e = Pop(&stack);
		e2 = Pop(&stack2);
		
		if(e.d==1){
			Push(&stack3, e2);
			cont++;
		}
	}
	
	while(Size(&stack3) > 1){
		e = Pop(&stack3);//P(x1, y1)
		e2 = Pop(&stack3);//Q(x2, y2)
		
		//lambda = (y2-y1)*(x2-x1)^-1 mod p
		aux = e2.x - e.x;//Para (x2-x1)^-1 
		if(aux < 0){
			while(aux < 0)
				aux = aux + p;
		}
		else
			aux = Modulo (aux, 1, p);
		aux = InversoMultiplicativo(aux, p);
			
		lambda = (e2.y - e.y) * aux;
		lambda = Modulo(lambda, 1, p);
		e3.l = lambda;
			
		//x1 = (lambda)^2-(x1+x2) mod p
		x1 = (lambda * lambda) - (e.x + e2.x);
		x1 = Modulo(x1, 1, p);
		e3.x = x1;
			
		//y1 = lambda(x0-x1)-y0 mod p
		y1 = (lambda * (e.x - x1)) - e.y ;
			
		if(y1 < 0){
			while(y1 < 0)
				y1 = y1 + p;
		}
		else
			y1 = Modulo (y1, 1, p);
		e3.y = y1;
			
		Push(&stack3, e3);
	}
	
	if(cont <= 0){
		printf("ERROR. (alfa) = (x0, y0) no es un elemento generador\n");
		exit(1);
	}
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
	
	/*printf("---%d---\n", Size(&stack));
	int aux2 = Size(&stack);
	printf("\n\n%d a Binario: ", a);
	for(int i=0; i<aux2; i++)
		printf("%d", Pop(&stack));
	printf("\n", a);*/
}

/*	Función Inverso Multiplicativo
	Uso: Obtiene los inversos multiplicativos de dos números a partir del Algoritmo Extendido de Euclides
	Recibe: Modulo m y Número n
	Retorna: Inverso multiplicativo inv	*/
long long int InversoMultiplicativo(long long int n, long long int m)
{
    long long int x, y;
    long long int g = AlgoritmoExtendidoEuclides(n, m, &x, &y);
    
    if (g != 1){ 
		printf("\nERROR. El numero no tiene Inverso Multiplicativo\n");
	}
    else
    {
        // Convierte el resultado del Algortimo Extendido de Euclides a positivo
        long long int inv = (x % m + m) % m;
        return inv;
    }
}

/*	Función AlgoritmoExtendidoEuclides
	Uso: Obtiene el mcd de dos números a partir del Algoritmo Extendido de Euclides
	Recibe: Modulo b, Número n, y apuntadores a las variabkles x e y
	Retorna: Minimo Común Divisor mcd	*/
long long int AlgoritmoExtendidoEuclides(long long int a, long long int b, long long int* x, long long int* y)
{
    if (a == 0)
    {
        *x = 0, *y = 1;
        return b;
    }
     
    // Llamada recursiva para almacenar los resultados
    long long int x1, y1;
    long long int mcd = AlgoritmoExtendidoEuclides(b % a, a, &x1, &y1);
 
    // Actualiza los valores de x e y
    *x = y1 - (b / a) * x1;
    *y = x1;
 
    return mcd;
}
