//Manuales usados: 7 packet, netdevice, ioctl. CAPITULO 2 (Pag 86-114)
#include <sys/socket.h>
#include <linux/if_packet.h>
#include <net/ethernet.h> /* the L2 protocols */
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <net/if.h>
#include <string.h>
#include <sys/time.h>

unsigned char MACorigen[6];
unsigned char IPorigen[4];
unsigned char trama_Enviar[1514];
unsigned char trama_Recibir[1514];
unsigned char MACbroadcast[6]={0xff, 0xff, 0xff, 0xff, 0xff, 0xff};
unsigned char ethertype[12]={0x0c, 0x0c};

int obtenerDatos(int descriptor_socket)
{
	struct ifreq nic;//nic es el nombre de la estructura ifreq
	int index, i;
	printf("\nInserta nombre de la interfaz: ");
	scanf("%s", nic.ifr_name);//guarda la cadena en ifr_name

	if(ioctl(descriptor_socket, SIOCGIFINDEX, &nic)==-1)//obtenemos el indice
	{
		perror("\nError al obtener el indice");
		exit(1);
	}
	else
	{
		index=nic.ifr_ifindex;

		if(ioctl(descriptor_socket, SIOCGIFHWADDR, &nic)==-1)//obtenemos la direccion MAC
		{
			perror("\nError al obtener la direccion MAC");
			exit(1);
		}
		else
		{
			memcpy(MACorigen, nic.ifr_hwaddr.sa_data+0, 6);//la direccion MAC se guardara en sa_data
			printf("\nDireccion MAC: ");
			for(i=0; i<6; i++)
				printf("%.2x:", MACorigen[i]);

			if(ioctl(descriptor_socket, SIOCGIFADDR, &nic)==-1)//obtenemos la direccion IP
			{
				perror("\nError al obtener la direccion IP");
				exit(1);
			}
			else
			{
				/*En este caso la direccion IP tambien se guardara dentro de sa_data pero desde el bit 2*/
				memcpy(IPorigen, nic.ifr_addr.sa_data+2, 4);//la direccion IP se guardara en sa_data
				printf("\nDireccion IP: ");
				for(i=0; i<4; i++)
					printf("%d.", IPorigen[i]);
			}
		}
	}
//TAREA: buscar en que archivos de regitro estan los DNS y la puerta de enlace(man route)
return index;
}

//Función para realizar la estructuracion de la trama
void estructuraTrama(unsigned char *trama)
{
	//se realiza la estructuración de la trama
	//memcpy(trama+0, MACbroadcast, 6);
	memcpy(trama+0, "d8:cb:8a:d5:7f:2f", 6);
	memcpy(trama+6, MACorigen, 6);
	memcpy(trama+12, ethertype, 2);
	memcpy(trama+14, "Mauro Sampayo Hernandez", 40);
}

//Funcion para enviar la trama, una vez esta ya esta estructurada
void enviarTrama(int descriptor_socket, int indice, unsigned char *trama)
{
	int tam;
	struct sockaddr_ll interfaz;
	memset(&interfaz, 0x00, sizeof(interfaz));//se borra la estructura (en este caso interfaz), para posteriormente llenarla
	interfaz.sll_family=AF_PACKET;
	interfaz.sll_protocol=htons(ETH_P_ALL);
	interfaz.sll_ifindex=indice;
	tam=sendto(descriptor_socket, trama, 60, 0, (struct sockaddr*)&interfaz, sizeof(interfaz));

	if(tam==-1)
	{
		perror("Error al enviar");
		exit(1);
	}	
	else
	{
		perror("Exito al enviar");
		
	}
}

//Funcion para realizqar la impresion de una trama
void imprimirTrama(unsigned char *trama, int tam)
{
	int i;

	for(i=0; i<tam; i++)
	{
		if(i%16==0)
			printf("\n");
		printf("%.2x", trama[i]);//%.2x sirve para poner los datos en hexadecimal
	}
}

//Funcion para recibir una trama de algun lado
void recibeTrama(int descriptor_socket, unsigned char *trama)
{
	struct timeval start, end;
        long mtime=0, seconds, useconds;  
	int tam, bandera;
	gettimeofday(&start, NULL);

	//while(1)//infinitamos el recibimiento de tramas
	while(mtime<2000)//esperara un maximo de 2 sefundos para recibir una respuesta
	{
		bandera=0;
		tam=recvfrom(descriptor_socket, trama, 1514, MSG_DONTWAIT, NULL, 0);
		
		if(tam==-1)
		{
			perror("\nError al recibir");
			//exit(1);//PARA CUANDO LA BANDERA ES 0
		}
		else
		{
			/*Probarlo corriendo el programa y porsteriormente abriendo el navegador de internet para que este envie tramas dirigidas a mi interfaz*/
			/*Se puede modificar para poder filtrar otro tipo de datos como el ethertype*/
			if(!memcmp(trama+0, MACorigen, 6))//compara una trama a partir de 0 con mi MACorigen, para asi filtrar unicamente las tramas dirigidas mi interfaz
			{
				imprimirTrama(trama, tam);
				//break;//limitarlo a solo recibir una trama y romper el ciclo infinito
				bandera=1;
			}
		}

		gettimeofday(&end, NULL);
    	        seconds  = end.tv_sec  - start.tv_sec;
    		useconds = end.tv_usec - start.tv_usec;
    		mtime = ((seconds) * 1000 + useconds/1000.0) + 0.5;

		if(bandera==1)
			break;
	}

	printf("\nElapsed time: %ld milliseconds\n", mtime);
}

int main()
{
	int packet_socket, indice;
	packet_socket = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL));

	if(packet_socket==-1)
	{
		perror("\nError al abrir el socket");
		exit(1);
	}
	else
	{
		perror("\nExito al abrir el socket");
		indice=obtenerDatos(packet_socket);//enviamos el descriptor de socket
		printf("\nEl indice es: %d \n", indice);
		//estructuraTrama(trama_Enviar);
		//enviarTrama(packet_socket, indice, trama_Enviar);//enviamos descriptor de socket, indice y trama a enviar(estructurada previamente)
		recibeTrama(packet_socket, trama_Recibir);
	}

close(packet_socket);
return 0;
}

//MODO BLOQUEANTE: Espera a que se reciba algo para que el programa continue
//TAREA: Estudiar como funciona el protocolo ARP
