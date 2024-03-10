/*
Practica 2: Scanner ARP (vesión con archivos)
Redes de Computadoras
Hecho por Mauro Sampayo Hernández

Compilación: gcc -o Practica2 Practica2.c -lm
*/
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
#include <math.h>
#include <sys/time.h>

unsigned char MACorigen[6];
unsigned char IPorigen[4];
unsigned char MascaraSubred[4];
unsigned char IPdestino[4];
unsigned char DireccionRed[4];
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
int bitscadena[8];


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

//Función para Convertir de Decimal a Binario. La cadena resultante se guardara siempre en la variable global bits cadena
void ConvertirABinario(unsigned char *cadena, int posicion)//
{
	int j, r; 
	r=cadena[posicion];
	//printf("%d|", r);
		
	if(r==0)//Si el valor entero es cero, se llenan los 8 bits con 0´s
	{
		for(j=0; j<=7; j++)
    		bitscadena[7-j]=0;	
	}
	else if(r==1)//Si el valor entero es cero, se llenan los 7 primeros bits con 0´s y el octavo con 1
	{
		bitscadena[7]=1;
		for(j=1; j<=7; j++)
			bitscadena[7-j]=0;	
	}
	else
	{
		for(j=0; j<7; j++)
	    {
			bitscadena[7-j]=r%2;	
			r=r/2;
			//printf("%d", bitsIPorigen[7-j]);
			//printf("|%d|, (%d)", r, j);
			
			if(r==1)//Cuando la división r/2 nos de 1
			{
				j++;
				bitscadena[7-j]=r;
				//printf("--%d--", bitsIPorigen[7-j]);
				
				if(j<7)//Cuando los 8 bits aun no se han llenado cuando r==1, el resto se llenan con 0´s
				{
					j++;
					while(j<=7)
					{
						bitscadena[7-j]=0;
						j++;
					}
				}
			}
		}
    }
}

//Funcion para Convertir de Binario a Decimal
int ConvertirADecimal(int *cadena)//
{
	int i, suma=0;

	for(i=0; i<8; i++)
	{
		if(cadena[i]==1)
			suma=suma+pow(2, 7-i);
		if(cadena[i]==0)
			suma=suma+0;
	}
	
	return suma;
}

//Funcion para Obtener la Direccion de Red de la IPorigen por medio de una operacion and con su Mascara de Subred
void ObtenerDireccionRed()//
{
	int bitsIPorigen[8];//cadena para almacenar los bits de cada uno de los valores enteros de IPorigen
	int bitsMascaraSubred[8];//cadena para almacenar los bits de cada uno de los valores enteros de MascaraSubred
	int cadenaopand[8];//cadena para guardar el resultado entre la operacion and de los bits de IPorigen y MascaraSubred 
	int i, k, a, b, c;
	
	for(i=0; i<4; i++)
	{
		ConvertirABinario(IPorigen, i);
		
		for(k=0; k<8; k++)
			bitsIPorigen[k]=bitscadena[k];//copiamos la cadena en binario resultante a la variable local para IPorigen
		/*for(k=0; k<8; k++)
			printf("%d", bitsIPorigen[k]);//imprimir bis de IPorigen
		printf("\n");*/
		
		ConvertirABinario(MascaraSubred, i);
		
		for(k=0; k<8; k++)
			bitsMascaraSubred[k]=bitscadena[k];//copiamos la cadena en binario resultante a la variable local para MascaraSubred
		/*for(k=0; k<8; k++)
			printf("%d", bitsMascaraSubred[k]);//imprimir bis de MascaraSubred
		printf("\n");*/
	
		for(k=0; k<8; k++)//Se realiza la operacion and entre cada uno de los bits en binario de la IPorigen y la Mascara de Subred, por medio de un ciclo que recorrera ambas cadenas de bits
		{
			a=bitsIPorigen[k];
			b=bitsMascaraSubred[k];
			c=a&b;
			cadenaopand[k]=c;//se guarda el resuktado en una cadena aparte
		}
		
		/*for(k=0; k<8; k++)
			printf("%d", cadenaopand[k]);//imprimir resultado
		printf("\n\n");*/
		
		DireccionRed[i]=ConvertirADecimal(cadenaopand);//convertimos el resultado (en binario) de la operacion and entre los bits de IPorigen y los de MascaraSubred. a decimal
	}
	
	printf("Direccion de Red: ");//Imprimimos Direccion de Red
	for(i=0; i<4; i++)
		printf("%d.", DireccionRed[i]);
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
	memcpy(trama+38, DireccionRed, 4);
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

//Función para almacenar los datos de la IPdestino y MACdestino de donde se recibio una respuesta
void Base_Datos(FILE *archivo)
{
	fprintf(archivo, "IPorigen: %d.%d.%d.%d----------", DireccionRed[0], DireccionRed[1], DireccionRed[2], DireccionRed[3]);
	fprintf(archivo, "IP que contesto: %d.%d.%d.%d | ", IPdestino[0], IPdestino[1], IPdestino[2], IPdestino[3]);
	fprintf(archivo, "MAC de IP que contesto: %.2x:%.2x:%.2x:%.2x:%.2x:%.2x\n", trama_ARP_respuesta[6], trama_ARP_respuesta[7], trama_ARP_respuesta[8], trama_ARP_respuesta[9], trama_ARP_respuesta[10], trama_ARP_respuesta[11]);
	printf("Guardado");
}
void RecibeARPRespuesta(int descriptor_socket, unsigned char *trama, FILE *archivo)
{
	struct timeval start, end;//
    long mtime=0, seconds, useconds;//  
	int tam, bandera;//
	gettimeofday(&start, NULL);//

	//while(1)
	while(mtime<200)//esperara un maximo de 2 sefundos para recibir una respuesta//
	{
		bandera=0;//
		tam=recvfrom(descriptor_socket, trama, 1514, MSG_DONTWAIT, NULL, 0);//si falla, probar quitanfole el MSG_DONTWAIT
		/*if(tam==-1)
		{
			perror("Error al recibir trama");
			//exit(1);//no se si deba comentar esto xdxd
		}
		else
		{*/
			if(!memcmp(trama+0, MACorigen, 6))
			{
				if(!memcmp(trama+12, ethertype, 2))
				{
					if(!memcmp(trama+20, opcoderespuesta, 2))
					{
						if(!memcmp(trama+28, DireccionRed, 4))
						{
							//if(!memcmp(trama+38, IPorigen, 4))//?
							//{
								printf("\n----------Trama recibida----------");
								ImprimirTrama(trama, tam);
								Base_Datos(archivo);
								//break;
								bandera=1;//
							//}
						}
					}
				}
			}

		//}
		
		gettimeofday(&end, NULL);//
    	seconds  = end.tv_sec  - start.tv_sec;//
        useconds = end.tv_usec - start.tv_usec;//
    	mtime = ((seconds) * 1000 + useconds/1000.0) + 0.5;//

		if(bandera==1)//
			break;//
	}
	
	printf("\nElapsed time: %ld milliseconds\n\n\n", mtime);//
}

int main()
{
	int packet_socket, indice, i, j;
	packet_socket = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL));
	FILE *archivo=fopen("prueba.txt", "w");

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
		ObtenerIPDestino();//Obtenemos la IP destino
		ObtenerDireccionRed();//Obtenemos la Direccion de Red de la Ip destino

		for(i=1; i<255; i++)
		{
			DireccionRed[3]=i;
			
			printf("Direccion de Red: ");//Imprimimos Direccion de Red
			for(j=0; j<4; j++)
				printf("%d.", DireccionRed[j]);
			
			EstructuraARPSolicitud(trama_ARP_solicitud);//estructuramos la trama solicitud ARP a enviar
			
			printf("\n----------Trama a enviar----------");
			ImprimirTrama(trama_ARP_solicitud,	60);//imprimimos trama a enviar
			printf("\n");
						
			EnviaARPSolicitud(packet_socket, indice, trama_ARP_solicitud);//enviamos descriptor de socket, indice y trama a enviar(estructurada previamente)
			RecibeARPRespuesta(packet_socket, trama_ARP_respuesta, archivo);//editar
		}
	}

fclose(archivo);
close(packet_socket);
return 0;
}
