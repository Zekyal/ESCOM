#include <sys/socket.h>
#include <sys/types.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h> //exit()
#include <string.h>
#include <errno.h>
#include <netdb.h> //getaddrinfo() getnameinfo() freeaddrinfo()
#include <unistd.h>//read
#include <fcntl.h>
#include <resolv.h>
#include <pthread.h>
#define ARRAY_LENGTH 3500//Tamaño del arreglo de números aleatorios
#define NUM_MAX 1000

/*Estructura de datos que se pasará al hilo*/
typedef struct
{
	char host_name [10];//Dirección del servidor que recibirá la cubeta
	int host_port;//Puerto de la aplicación servidor que recibirá la cubeta
	int *bucket;//Apuntador a cubeta
	int size_bucket;//Tamaño de la cubeta
}datos;

/*Genera numeros aleatorios para ser posteriorimente guardados en el arreglo de enteros aleatorios*/
void GenerarNumeros();
/*Inicializa las estructuras datos y las cubetas*/
void CrearCubeta (datos *Estructuras, int num_cubetas);
/*LLena cada una de las cubetas con los numeros del arreglo de enteros aleatorios*/
void LlenarCubeta (datos *Estructuras, int numBucket, int limInf, int limSup);
/*Realiza el envío de cada una de los hilos para las cubetas al servidor, para posteriorimente recibirlas ya ordenadas, y almacenarlas en el arreglo de resultado*/
void *Cliente (datos *Estructura);

int resultado[ARRAY_LENGTH], numeros[ARRAY_LENGTH];
int j= 0;

int main ()
{
	int i, num_cubetas;
	printf ("Número de cubetas: ");
	scanf("%d", &num_cubetas);//Obtenermos el numero de cubetas
	GenerarNumeros();//Generamos el arreglo de numeros
	printf ("\nARREGLO INICIALIZADO\n");
	datos *Estructuras= (datos*)calloc(num_cubetas, sizeof(datos*));//Inicializa (asigna con ceros) un arreglo de n_cubetas estructuras 
	printf("Se han creado %d cubetas\n", num_cubetas);
	CrearCubeta (Estructuras, num_cubetas);
	printf ("CUBETAS CREADAS\n");
	printf ("\nCreando hilos cliente...\n");
	
	pthread_t* cliente= (pthread_t*)calloc(num_cubetas, sizeof(pthread_t));//Inicializa un arreglo de n_cubetas hilos
		
	//Creamos cada uno de los hilos que contendran una cubeta cada uno
	for (i=0; i<num_cubetas; i++)
    	pthread_create(&cliente [i], NULL, (void*)Cliente, &Estructuras[i]);//direccion del hilo a crear, el proceso que correrá, y lo que recibirá el proceso
    	
    //Esperamos a que un hilo termine para posteriporimente iniciar el siguiente, y asi hasta que se ejecuten todos los hilos
	for(i=0; i<num_cubetas; i++)
    	pthread_join(cliente[i], NULL); //hilo y donde se guardará lo que devolvera el proceso en caso de hacerlo
    	
    	
	usleep (10000);
	FILE *entrada, *salida;
	entrada= fopen ("numeros.txt", "w");
	salida= fopen("numeros_ordenados.txt", "w");

	for(i=0; i<ARRAY_LENGTH; i++){
		fprintf(entrada, "%d", numeros[i]);
		fprintf(salida, "%d", resultado[i]);
		
		if(i==ARRAY_LENGTH-1)
			continue;
			
		fprintf(entrada, ", ");
		fprintf(salida, ", ");
	}
		
	fclose (entrada);
	fclose (salida);
	
	printf("\nNumeros ordenados correctamente :D\n");
	return 0;
}

/*Función para generar el arreglo de números aleatorios*/
void GenerarNumeros()
{
	for(int i=0; i<ARRAY_LENGTH; i++)
		numeros[i]= rand()%999;
}


void CrearCubeta (datos *Estructuras, int num_cubetas)
{
	int limInf= 0, rango, modulo;
	rango= (NUM_MAX/num_cubetas)-1;//Establece la base para el rango de numeros que aceptará cada cubeta
	modulo= NUM_MAX%num_cubetas;
	
	for (int i=0; i<num_cubetas; i++)
	{
		printf("Inicializando cubeta: %d.\n", i);
		Estructuras[i].host_port= (5000+i);//Asigna el valor del puerto del servidor al cual será enviada la cubeta
		strcpy(Estructuras [i].host_name, "127.0.0.1");//Asigna la direccion ip del servidor al cual sera enviada la cubeta
		//strcpy(&*(Estructuras [i].host_name), "127.0.0.1");
		
		//En caso de sobren numeros del arreglo tras realizar todos los llenados de las cubetas, estos se añadiran a la ultima cubeta junto a los numeros que esta ya tenga
		if (modulo!=0 && i==(num_cubetas-1))
			LlenarCubeta(Estructuras, i, limInf, limInf+rango+modulo);				
		else
			LlenarCubeta(Estructuras, i, limInf, limInf+rango);
			
		limInf= limInf+rango+1;//Ajustamos el limite inferior para definir el rango de la siguiente cubeta
	}	
}

void LlenarCubeta(datos *Estructuras, int numBucket, int limInf, int limSup)
{
	int *numsRango= (int*)calloc(ARRAY_LENGTH, sizeof (int)); //inicializa un arreglo de 3500 enteros para meter los numeros dentro de la cubeta en cuestion
	int i, cont= 0;
	
	//Recorrera todos los numeros de nuestro arreglo de enteros "numeros", y si alguno de estos se encuentra en el rango definido por los limites superiores e inferiores, este será añadido al arreglo de enteros numsRango
	for(i=0; i<ARRAY_LENGTH; i++)
	{
		if(numeros[i]>=limInf && numeros[i]<= limSup)
		{
			numsRango[cont]= numeros[i];
			cont++;
		}
	}
	
	Estructuras[numBucket].size_bucket= cont;//Define el tamaño de la cubeta en cuestion a partir del contador cont
	Estructuras[numBucket].bucket= (int*)calloc(cont, sizeof(int));//Inicializa un arreglo de enteros del tamaño del contador cont para la cubeta Estructuras
	
	//Pasamos todos los valores de numsRango a el arreglo de enteros de la cubeta de Eastructuras
	for (i=0; i<cont; i++)
    	Estructuras[numBucket].bucket[i]= numsRango[i];
    
	//return count;
}

void *Cliente (datos *Estructura)
{
	int host_port= (*Estructura).host_port;//Puerto del servidor
	char *host_name = malloc(16*sizeof(char));
	strcpy(host_name, (*Estructura).host_name);//Direccion del servidor
	
	struct sockaddr_in serv_addr;
	int bytecount, socket_fd, err;
	int opcion= 1;

	socket_fd= socket (AF_INET, SOCK_STREAM, 0);//Descriptor de socket de flujo
	
	if(socket_fd==-1)
	{
		perror("\nError al abrir el socket");
		exit(1);
	}
	//Establecemos las opciones de SO_REUSEADDR y SO_KEEPALIVE en el socket
	if((setsockopt(socket_fd, SOL_SOCKET, SO_REUSEADDR, (char*)&opcion, sizeof(int)))==-1 || (setsockopt(socket_fd, SOL_SOCKET, SO_KEEPALIVE, (char*)&opcion, sizeof(int)))==-1)
	{
		perror("\nError al establecer las opciones del socket");
		exit(1);
	}

	serv_addr.sin_family= AF_INET;//Familia de la Dirección  
	serv_addr.sin_port= htons(host_port);//Puerto 
	serv_addr.sin_addr.s_addr= inet_addr(host_name);//Dirección

	//Conectamos el socket a un puerto definido en la direccion IP que se definio
	if((connect(socket_fd, (struct sockaddr*)&serv_addr, sizeof(serv_addr)))==-1)
	{
		if ((err=errno)!=EINPROGRESS)
		{
			printf("Error al conectar socket %d\n", errno);
			exit(1);
		}
	}
	
	//Enviamos el tamaño de la cubeta al servidor
	int tam_cubeta= htonl((*Estructura).size_bucket);
	bytecount= send(socket_fd, &tam_cubeta, sizeof(int),0);
	
	if(bytecount==-1)
	{
		perror("\nError al enviar datos del socket");
		exit(1);
	}
	
	//Enviamos cada uno de los numeros enteros que se encuentran en nuestra cubeta hacia el servidor
	int i;
		
	for (i=0; i<(*Estructura).size_bucket; i++)
	{
		int num= htonl((*Estructura).bucket [i]);
		bytecount= send(socket_fd, &num, sizeof(int),0);
		
		if(bytecount==-1)
		{
			perror("\nError al enviar datos del socket");
			exit(1);
		}
	}

	int n;
	
	for(i=0; i<(*Estructura).size_bucket; i++)
	{
		int dato;
		n= read(socket_fd, &dato, sizeof(int));
		
		if(n<0) 
			perror("Error al leer el socket");
		
		resultado[j]= ntohl(dato);
		j++;	
	}
}

