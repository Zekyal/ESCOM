#include <netdb.h> //getaddrinfo() getnameinfo() freeaddrinfo()
#include <string.h>
#include <stdlib.h>//exit()
#include <stdio.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <unistd.h>//read()
#include <pthread.h>
#include <fcntl.h>
#include <errno.h>
#include <netinet/in.h>
#include <resolv.h>
#include <arpa/inet.h>

/*Estructura de datos que se pasará al hilo*/
typedef struct
{
	char host_name [10];//Dirección del servidor que recibirá la cubeta
	int host_port;//Puerto de la aplicación servidor que recibirá la cubeta
	int *bucket;//Apuntador a cubeta
	int size_bucket;//Tamaño de la cubeta
}datos;

/*Recibe cada una de las cubetas desde el Cliente para realizar su ordenamiento, y posteriorimente las envia de vuelta al cliente ya ordenadas*/
void *Servidor(int *port);
/*Realiza el ordenamiento de los enteros de las cubetas*/
void ShellSort(int *array, int size);

int main()
{
	int i, puerto=5000, num_cubetas;
	int *puertos=(int*)malloc(num_cubetas*sizeof(int));
	
	printf("Numero de cubetas: ");
	scanf("%d", &num_cubetas);
	
	//Se crean tantos puertos como cubetas halla
	for (i=0; i<num_cubetas; i++)
		puertos[i]=(puerto+i);
		
	printf ("\nCreando %d hilos servidor\n", num_cubetas);
	pthread_t *servidor = (pthread_t*)calloc(num_cubetas, sizeof(pthread_t));//Inicializa un arreglo de n_cubetas hilos
	
	//Creamos cada uno de los hilos para recibir cada cubeta del cliente
	for (i= 0; i<num_cubetas; i++)
		pthread_create(&servidor[i], NULL, (void*)Servidor, &puertos[i]);
	
	//Esperamos a que un hilo termine para posteriporimente iniciar el siguiente, y asi hasta que se ejecuten todos los hilos	
	for (i=0; i<num_cubetas; i++)
		pthread_join(servidor[i], NULL);
		
	free(servidor);
	free(puertos);
	return 0;
}

void *Servidor(int *port)
{
	int host_port= *port;
	
	struct sockaddr_in serv_addr;
	struct sockaddr_in cl_addr;
	int socket_fd;
	int opcion= 1;
	socklen_t addr_size=0;
	int *client_socket;
	
	socket_fd= socket(AF_INET, SOCK_STREAM, 0);//Descriptor del socket
	
	if(socket_fd==-1)
	{
		perror("\nError al abrir el socket");
		exit(1);
	}
	//Establecemos las opciones de SO_REUSEADDR y SO_KEEPALIVE en el socket
	if ((setsockopt(socket_fd, SOL_SOCKET, SO_REUSEADDR, (char*)&opcion, sizeof(int)))==-1 || (setsockopt(socket_fd, SOL_SOCKET, SO_KEEPALIVE, (char*)&opcion, sizeof(int)))==-1)
	{
		perror("\nError al establecer las opciones del socket");
		exit(1);
	}
	
	serv_addr.sin_family= AF_INET ;
	serv_addr.sin_port= htons(host_port);	
	serv_addr.sin_addr.s_addr= INADDR_ANY;
	
	//Asociamos el socket con el puertodefinido previamente
	if(bind(socket_fd, (struct sockaddr*)&serv_addr, sizeof(serv_addr))==-1)
	{
		printf("Error binding socket %d\n",errno);
		exit(1);
	}
	//Espera una conexión
	if(listen(socket_fd, 10)==-1)
	{
		printf("Error listening %d\n",errno);
		exit(1);
	}
	
	addr_size= sizeof(struct sockaddr_in);

	while(1)
	{
		client_socket= (int*)malloc(sizeof(int));
		
		if ((*client_socket= accept(socket_fd, (struct sockaddr*)&cl_addr, &addr_size))!=-1)
		{
			printf ("Conexión recibida desde: %s\n", inet_ntoa(cl_addr.sin_addr));
			int bytecount, buffer;//el buffer es donde se guardará la información quer se reciba
			
			//Recibimos el tamaño del arreghlo de la cubeta
			bytecount= recv(*client_socket, &buffer, sizeof(int), 0);
			
			if(bytecount==-1)
			{
				perror("\nError al recibir datos del socket");
				exit(1);
			}
			
			//Recibimos cada uno de los numeros contenidos en el arreglo de la cubeta desde el cliente, y los guardamos en el arreglo numeros
			int i, tam_cubeta= ntohl(buffer);
			int *numeros= (int*)calloc(tam_cubeta, sizeof(int));
			
			for (i=0; i<tam_cubeta; i++)
			{
				bytecount= recv(*client_socket, &buffer, sizeof(int), 0);
				
				if(bytecount==-1)
				{
					perror("\nError al recibir datos del socket");
					exit(1);
				}
				
				numeros[i]= ntohl(buffer);
			}
			
			//Enviamos el arreglo de enteros recibido desde la cubeta para que sea ordenado
	      	ShellSort(numeros, tam_cubeta);
	      	
	      	//Enviamos el arreglo de enteros de vuelta al cliente una vez este ha sido ordenado
			for(i=0; i<tam_cubeta; i++)
			{
				int num= htonl(numeros[i]);
				bytecount= send(*client_socket, &num, sizeof (int), 0);
				
				if(bytecount==-1)
				{
					perror("\nError al enviar datos del socket");
					exit(1);
				}
			}
			
			free(client_socket);
			break;
		}else
			printf("Error al aceptar conexion %d\n", errno);
	}
}

void ShellSort(int *array, int size)
{
   int i, j, temp, k=size / 2;
	while (k>0)
	{
		for(i=k; i<size; i++)
		{
			temp= array[i];
			j= i-k;
			while (j>=0 && array[j]>temp)
			{
				array[j+k]= array [j];
				j= j-k;
			}
			array[j+k]= temp;
		}
		k= k/2;
	}
}
