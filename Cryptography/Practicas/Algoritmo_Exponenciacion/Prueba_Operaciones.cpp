#include<stdio.h>
#include<stdlib.h>
#include<gmpxx.h>

void Menu();
int* Suma(int*, int*, int, int);
int* Resta(int*, int*, int, int);
int* Multiplicacion(int*, int*, int, int);
void Modulo(int*, int*, int, int);

int main(){
	int i, aux, TAM;
	int* a;
	int* b;
	int *r;
	int tamA, tamB, opcion;
	
	for(;;){
		Menu();
		printf("\nSeleccione una opcion: ");
		scanf("%d", &opcion);
		printf("\nNumero de digitos del valor de a = ");
		scanf("%d", &tamA);
		a = (int*)calloc(tamA, sizeof(int));
		printf("Valor a = ");
	
		for(i = 0; i<tamA; i++){
    		scanf("%d", &aux);
    		a[i] = aux;
		}
	
		/*for(i = 0; i<tamA; i++){
    		printf("%d, ", a[i]);
		}*/
	
		printf("\nNumero de digitos del valor de b = ");
		scanf("%d", &tamB);
		b = (int*)calloc(tamB, sizeof(int));
		printf("Valor b = ");
	
		for(i = 0; i<tamB; i++){
    		scanf("%d", &aux);
    		b[i] = aux;
		}
	
		/*for(i = 0; i<tamB; i++)
	    	printf("%d, ", b[i]);
		}*/
	
		switch(opcion){
			case 1: 
				if (tamA >= tamB)
					TAM = tamA + 1;
				else
					TAM = tamB + 1;
					
				r = (int*)calloc(TAM+1, sizeof(int));
				r = Suma(a, b, tamA, tamB); 
				printf("\nResultado = ");
				
				for(i = 0; i<TAM; i++)
	    			printf("%d", r[i]);
	    			
				getchar(); getchar(); 
				break;
			case 2: 
				r = (int*)calloc(tamA, sizeof(int));
				r = Resta(a, b, tamA, tamB);
				
				if(r[0] == -1)
					printf("\n **ERROR: El valor de a debe de ser mayor al de b");
				else{
					printf("\nResultado = ");
					for(i = 0; i<tamA; i++)
	    				printf("%d", r[i]);
				}
				
				getchar(); getchar(); 
				break;
			case 3: 
				TAM = tamA + tamB + 1;
				r = (int*)calloc(TAM, sizeof(int));
				r = Multiplicacion(a, b, tamA, tamB);
				
				printf("\nResultado = ");
				
				for(i = 0; i<TAM; i++)
	    			printf("%d", r[i]);
	    		
				getchar(); getchar(); 
				break;
			case 4:
				Modulo(a, b, tamA, tamB); 
				getchar(); getchar(); 
				break;
			case 5: 
				getchar(); getchar(); 
				break;
			default: printf("Opcion invalida\n"); getchar(); getchar(); break;
		}
	}
	
	return 0;
}

void Menu(){
	printf("\n");
	printf("_____________________________________________\n");
	printf("|           -OPERACIONES VALIDAS-           |\n");
	printf("| 1. Suma: a + b                            |\n");
	printf("| 2. Resta: a - b                           |\n");
	printf("| 3. Multiplicacion: a * b                  |\n");
	printf("| 4. Modulo: a MOD b                        |\n");
	printf("| 5. Potencia: a ^(b)                       |\n");
	printf("|___________________________________________|\n");
}

int* Suma(int* a, int* b, int tamA, int tamB){
	int carry = 0, aux = 0;
	int TAM = 0;
	
	if (tamA >= tamB)
		TAM = tamA + 1;
	else
		TAM = tamB + 1;
		
	int* res = (int*)calloc(TAM, sizeof(int));
		
	for(int i=1; i<TAM; i++){	
		if(i > tamA)
			aux = b[tamB-i] + carry;
		else if(i > tamB)
			aux = a[tamA-i] + carry;
		else
			aux = a[tamA-i] + b[tamB-i] + carry;
			
				
		res[TAM-i] = aux % 10;
		carry = aux / 10;
	}
	
	res[0] = carry;
	
	/*printf("\n Resultado: ");
	for(int j=0; j<TAM; j++){
    	printf("%d", res[j]);
	}*/
	
	return res;
}

int* Resta(int* a, int* b, int tamA, int tamB){
	int aux = 0, i = 1;
	int contA = 0, contB = 0;
	int TAM = tamA;
	int* res = (int*)calloc(TAM, sizeof(int));
	
	if (tamB > tamA){
		res[0] = -1;
		return res;
	}
	
	while(a[i]==0){
		i++; contA++;
	}
	i=1;
	
	while(b[i]==0){
		i++; contB++;
	}
	i=1;	
	
	if (contA > contB){
		res[0] = -1;
		return res;
	}
		
	for(i=1; i<=TAM; i++){	
		if(i > tamB){
			if(a[tamA-i] < 0){
				res[TAM-i] = a[tamA-i]+10;				
				a[tamA-i-1] = a[tamA-i-1] - 1; 
			}
			else
				res[TAM-i] = a[tamA-i];	
		}
		else{
			if(b[tamB-i] > a[tamA-i])
			{
				res[TAM-i] = (a[tamA-i] + 10) - b[tamB-i];
				
				if((tamA-i-1)<0){
					res[0] = -1;
					return res;
				}
				else if(a[tamA-i-1] == 0){
					a[tamA-i-1] = 9;
					a[tamA-i-2] = a[tamA-i-2] - 1;
				}
				else
					a[tamA-i-1] = a[tamA-i-1] - 1;
			}
			else
				res[TAM-i] = a[tamA-i] - b[tamB-i];
		}
	}
	
	/*printf("\n Resultado: ");
	for(int j=0; j<TAM; j++){
    	printf("%d", res[j]);
	}*/
	
	return res;
}

int* Multiplicacion(int* a, int* b, int tamA, int tamB){
	int carry = 0, aux = 0;
	int i, j, k;
	int TAM = tamA+tamB+1;
	int mtrz[tamB][TAM];
	
	for(i=1; i<=tamB; i++)
		for(j=1; j<=TAM; j++){
			if(j > tamA){
				aux = carry;
				carry = 0;
			}
			else
				aux = b[tamB-i] * a[tamA-j] + carry;
				
			mtrz[i][TAM-(j-1)] = aux % 10;//mtrz[tamB-(i-1)][TAM-(j-1)] = aux % 10;
			carry = aux / 10;
		}
	
	for(i=1; i<=tamB; i++)
		for(k=1; k<i; k++){
			for(j=1; j<TAM; j++)
				mtrz[i][j] = mtrz[i][j+1];	
			
			mtrz[i][TAM] = 0;
		}
		
	int* res = (int*)calloc(TAM, sizeof(int));
	carry = 0; aux = 0;
	
	for(i=1; i<=tamB; i++){
		for(j=1; j<=TAM; j++){
			printf("%d, ", mtrz[i][j]);
		}
		printf("\n");
	}
	
	for(j=0; j<TAM; j++){
		for(i=1; i<=tamB; i++){
			aux = aux + mtrz[i][TAM-j] + carry;
			carry = 0;
		}
		
		res[TAM-(j+1)] = aux % 10;
		carry = aux / 10;
		aux = 0;
	}
	
	return res;
}

void Modulo(int* a, int* b, int tamA, int tamB){
	if(tamB > tamA){
		
	}
	else{
		int* residuo = (int*)calloc(tamA, sizeof(int));
		int* aux = (int*)calloc(tamA, sizeof(int));
		int i;
		
		for(i=0; i<tamA; i++){
			residuo[i] = a[i];
			aux[i] = a[i];
		}
		
		for(;;){
			aux = Resta(aux, b, tamA, tamB);
			for(i=0; i<tamA; i++)
				printf("%d", aux[i]);
			printf("\n");
			
			if(aux[0] == -1)
				break;
			else{
				for(i=0; i<tamA; i++)
					residuo[i] = aux[i];
			}
		}
		
		for(i=0; i<tamA; i++)
    		printf("%d", residuo[i]);
	}
}

