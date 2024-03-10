/*
Practica 1: Protocolo ARP
Redes de Computadoras
Hecho por Mauro Sampayo Hernández

Compilación: gcc -o Practica1 protocoloARP.c 
*/
//CAPITULO 5(Pag 171-187)
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

unsigned char MACorigen[6];
unsigned char IPorigen[4];
unsigned char MascaraSubred[4];
unsigned char IPdestino[4];
unsigned char trama_ARP_solicitud[60]={0xff,0xff,0xff,0xff,0xff,0xff,0x00,0x00,0x00,0x00,
0x00,0x00,0x08,0x06,0x00,0x01,0x08,0x00,0x06,0x04,
0x00,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,'M','S','H'};//estructura del encabezado MAC(primeros 13 bytes), y el mensaje ARP(a partir del byte 14)
/*En esta declaración, ya se ha dejado previamente el espacio del broadcast del MAC a buscar en los promeros 6 bytes, y la declaración del protovolo ARP en el
encabezado MAC, y el cual es el 0806; y las declaraaciones de los primeros 5 campos(chequear pag 172 y 178) del mensaje ARP del byte 14 al byte 21*/
unsigned char trama_ARP_respuesta[1514];
unsigned char ethertype[2]={0x08, 0x06};
unsigned char opcoderespuesta[2]={0x00, 0x02};

int ObtenerDatos(int descriptor_socket)
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
				/*En este caso la direccion IP tambien se guardara dentro de nic.ifr_addr.sa_data pero desde el bit 2*/
				memcpy(IPorigen, nic.ifr_addr.sa_data+2, 4);//la direccion IP se guardara en sa_data
				printf("\nDireccion IP: ");
				for(i=0; i<4; i++)
					printf("%d.", IPorigen[i]);

                if(ioctl(descriptor_socket, SIOCGIFNETMASK, &nic)==-1)//obtenemos la mascara de subred
                {
                    perror("\nError al obtener la mascara de subred");
                    exit(1);
                }
                else
                {
                    /*En este caso la mascara de subred  se guardara dentro de sa_data pero desde la variable netmask y desde el
                    bit 2*/
                    memcpy(MascaraSubred, nic.ifr_netmask.sa_data+2, 4);//la mascara de subred se guardara en sa_data
                    printf("\nMascara de Subred: ");
                    for(i=0; i<4; i++)
                        printf("%d.", MascaraSubred[i]);

                    printf("\nFamilia: %.4x", nic.ifr_netmask.sa_family);
                    //obtenemos la familia de protocolos a la que pertenece la mascara de subred
                }
			}
		}
	}

return index;
}

//Funcion para obtener la IP destino a la que sera enviada nuestro ARP
void ObtenerIPDestino()
{
	int i, ipdest;
	printf("IP Destino: ");
	
	for(i=0; i<3; i++)
	{
		IPdestino[i]=IPorigen[i];
		printf("%d.", IPdestino[i]);
	}
		
	//La ip destino es igual al ip origen, cambiando el ultimo byte
	scanf("%d", &ipdest);
	IPdestino[3]=ipdest;//Colocamos el ultimo byte
}

//Función que estructura el mensaje de la trama de solicitud ARP
void EstructuraARPSolicitud(unsigned char *trama)
{
	//Encabezado MAC
	memcpy(trama+6, MACorigen, 6);
	//Mensaje ARP
	memcpy(trama+22, MACorigen, 6);
	memcpy(trama+28, IPorigen, 4);
	memcpy(trama+32, "0x00", 6);//se llena con ceros debido a que esta sera la direccion MAC que se deberá obtener a partir de su IPdestino
	memcpy(trama+38, IPdestino, 4);
}

//Funcion para enviar el broadcast dek mensaje ARP por medio del indice
void EnviaARPSolicitud(int descriptor_socket, int indice, unsigned char *trama)
{
	int tam;
	struct sockaddr_ll capaEnlace;
	memset(&capaEnlace, 0x00, sizeof(capaEnlace));
	capaEnlace.sll_family=AF_PACKET;
	capaEnlace.sll_protocol=htons(ETH_P_ALL);
	capaEnlace.sll_ifindex=indice;
	tam=sendto(descriptor_socket, trama, 60, 0, (struct sockaddr*)&capaEnlace, sizeof(capaEnlace));

	if(tam==-1)
	{
		perror("\nErrror al enviar trama");
		exit(1);
	}
	else
		perror("\nExito al enviar trama");
}

void ImprimirTrama(unsigned char *trama, int tam)
{
	int i;

	for(i=0; i<tam; i++)
	{
		if(i%16==0)
			printf("\n");
		printf("%.2x", trama[i]);
	}
}

void RecibeARPRespuesta(int descriptor_socket, unsigned char *trama)
{
	int tam;

	while(1)
	{
		tam=recvfrom(descriptor_socket, trama, 1514, 0, NULL, 0);

		if(tam==-1)
		{
			perror("Error al recibir trama");
			exit(1);
		}
		else
		{
			if(!memcmp(trama+0, MACorigen, 6))
			{
				if(!memcmp(trama+12, ethertype, 2))
				{
					if(!memcmp(trama+20, opcoderespuesta, 2))
					{
						if(!memcmp(trama+28, IPdestino, 4))
						{
							if(!memcmp(trama+38, IPorigen, 4))//?
							{
								printf("\n----------Trama a recibir----------");
								ImprimirTrama(trama, tam);
								break;
							}
						}
					}
				}
			}

		}
	}
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
		indice=ObtenerDatos(packet_socket);//enviamos el descriptor de socket
		printf("\nEl indice es: %d \n", indice);
		ObtenerIPDestino();
		EstructuraARPSolicitud(trama_ARP_solicitud);//estructuramos la trama solicitud ARP a enviar
		printf("\n----------Trama a enviar----------");
		ImprimirTrama(trama_ARP_solicitud,	60);//imprimimos trama a enviar
		printf("\n");
		EnviaARPSolicitud(packet_socket, indice, trama_ARP_solicitud);//enviamos descriptor de socket, indice y trama a enviar(estructurada previamente)
		RecibeARPRespuesta(packet_socket, trama_ARP_respuesta);
	}

close(packet_socket);
return 0;
}

//ponerle un for a arp para encontrar las posibles ips con su MAC, y si tienen respuesta en ARP, guardarlas en una base de datos
