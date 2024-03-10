/*
Practica 3: Servidor ARP
Redes de Computadoras
Hecho por Mauro Sampayo Hernández

Compilación: gcc -o Practica3 $(mysql_config --cflags) Practica3.c $(mysql_config --libs)
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
#include <mysql.h>
#include <string.h>
#include <sys/socket.h>
#include <net/if_arp.h>
#include <linux/if_ether.h>
#include <net/ethernet.h> 
#include <ctype.h>

unsigned char MACorigen[6];
unsigned char IPorigen[4];
unsigned char MascaraSubred[4];
unsigned char trama_Solicitud_ARP_gratuito[60]={0xff,0xff,0xff,0xff,0xff,0xff,0x00,0x00,0x00,0x00,
0x00,0x00,0x08,0x06,0x00,0x01,0x08,0x00,0x06,0x04,
0x00,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,'M','S','H'};
unsigned char trama_ARP_Respuesta[60]={0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x08,0x06,0x00,0x01,0x08,0x00,0x06,0x04,
0x00,0x02,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,'M','S','H'};
unsigned char trama_ARP_gratuito[1514];
unsigned char ethertype[2]={0x08, 0x06};
unsigned char MACbroadcast[6]={0xff, 0xff, 0xff, 0xff, 0xff, 0xff};
unsigned char opcode[2]={0x00, 0x01};
unsigned char IPcero[4]={0,0,0,0};
int packet_socket, indice;

int ObtenerDatos(int descriptor_socket)
{
	struct ifreq nic;//nic es el nombre de la estructura ifreq
	int index, i;
	printf("\nInserta nombre de la interfaz donde que desea realizar la solicitud ARP: ");
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

//Función para verificar que la IP recibida en latrama este en la base de datos
int VerificarIPBaseDatos(unsigned char *IP)
{
	int flag=0;
	MYSQL *base_datos;
	base_datos=mysql_init(NULL);
	base_datos=mysql_real_connect(base_datos, "localhost", "root"/*usuario*/, "root"/*contraseña*/, "IPRecibeRespuesta", 0, NULL, 0 );

	if(base_datos==NULL)
	{
		fprintf(stderr, "%s\n", mysql_error(base_datos));
		exit(1);
	}

	char *consulta;
	consulta=(char*)malloc(200);
	sprintf(consulta, "SELECT IP_que_envia FROM Datos;");//Consultamos las IPs de la base de datos
	int qstate=0;
	qstate=mysql_query(base_datos, consulta);//se realiza la consulta de las IPs en la base de datos

	if(qstate==0)
		printf("\nElemento IP consultado con exito");
	else
		printf("\nError al consultar");

	MYSQL_RES *ip=mysql_use_result(base_datos);//Variable que contendra el resultado de la consulta
	MYSQL_ROW row;//VAriable que ontendra los campos por cada registro consultado

	while((row=mysql_fetch_row(ip))!=NULL)//Recorremos la consulta de las IPs mientras haya elementos en esta
	{
		if(strcmp(IP, row[0])==0)
			flag = 1;
	}

	free(consulta);
	//mysql_close(base_datos);
	return flag;
}

//Función que Consulta a MAC perteneciente a la IP Sender o a la IP Target
unsigned char* ConsultarMAC(unsigned char *IP)/*----PENDIENTE----*/
{
	int flag=0;
	char *MACip;
	MACip=(char*)malloc(sizeof(char));

	MYSQL *base_datos;
	base_datos=mysql_init(NULL);
	base_datos=mysql_real_connect(base_datos, "localhost", "root"/*usuario*/, "root"/*contraseña*/, "IPRecibeRespuesta", 0, NULL, 0 );

	if(base_datos==NULL)
	{
		fprintf(stderr, "%s\n", mysql_error(base_datos));
		exit(1);
	}

	char *consulta;
	consulta=(char*)malloc(200);
	sprintf(consulta, "SELECT MAC_IP_que_recibe FROM Datos WHERE IP_que_envia='%s'", IP);//Consultamos las IPs de la base de datos
	int qstate=0;
	qstate=mysql_query(base_datos, consulta);//se realiza la consulta de las IPs en la base de datos

	if(qstate==0)
		printf("\nElemento MAC consultado con exito");
	else
		printf("\nError al consultar");

	MYSQL_RES *mac=mysql_use_result(base_datos);//Variable que contendra el resultado de la consulta
	MYSQL_ROW row=mysql_fetch_row(mac);//VAriable que ontendra los campos por cada registro consultado

	sprintf(MACip,"%s",row[0]);//Copiamos el resultado de la consulta en la variable MAC

	free(consulta);
	mysql_close(base_datos);

	return MACip;
}

//Función que estructura el mensaje de la trama de solicitud ARP gratuito
void EstructuraSolicitudARPGratuito(unsigned char *trama, unsigned char *MACdefensor, unsigned char *IPdefensor)
{
	printf("Entro a Solicitud");
	//Encabezado MAC
	memcpy(trama+6, MACdefensor, 6);
	//Mensaje ARP
	memcpy(trama+22, MACdefensor, 6);
	memcpy(trama+28, IPdefensor, 4);
	memset(trama+32, 0x00, 6);
	memcpy(trama+38, IPdefensor, 4);
}

//Función que estructura el mensaje de la trama de respuesta ARP gratuito
void EstructuraRespuestaARPGratuito(unsigned char *trama, unsigned char *MACinfractor, unsigned char *MACdefensor, unsigned char *IPdefensor)
{
	printf("Entro a Respuesta");
	//Encabezado MAC
	memcpy(trama+0, MACinfractor, 6);
	memcpy(trama+6, MACdefensor, 6);
	//Mensaje ARP
	memcpy(trama+22, MACdefensor, 6);
	memcpy(trama+28, IPdefensor, 4);
	memcpy(trama+32, MACinfractor, 6);
	memcpy(trama+38, IPdefensor, 4);
}

//Funcion para enviar el broadcast dek mensaje ARP por medio del indice
void EnviarTrama(int descriptor_socket, int indice, unsigned char *trama)
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
		perror("\nError al enviar trama");
		exit(1);
	}
	else
		perror("\nExito al enviar trama");
}

void ImprimirTrama(unsigned char *trama, int tam)//
{
	int i;

	for(i=0; i<tam; i++)
	{
		if(i%16==0)
			printf("\n");
		printf("%.2x", trama[i]);
	}
}

unsigned char* MACsinpuntos(char *MACconpuntos)
{
	unsigned char *MACsinpuntos;
	MACsinpuntos=(unsigned char*)malloc(6);
	char punto=':';
	for (int i=0; i<6; ++i)
	{
		unsigned int iNumber = 0;
		char ch;

		//convierte las letras a mayusculas
		ch = tolower (*MACconpuntos++);

		if ((ch < '0' || ch > '9') && (ch < 'a' || ch > 'f'))
		{
			return NULL;
		}

		//convierte en numero. 
		//a. si el carcater es dígito entonces ch - '0'
		//	b. en caso contrario (ch - 'a' + 10)  
		//	porque con la suma de diez tome el correcto valor.
		iNumber = isdigit (ch) ? (ch - '0') : (ch - 'a' + 10);
		ch = tolower (*MACconpuntos);

		if ((i<5 && ch!=punto) || (i==5 && ch!='\0' && !isspace(ch)))
		{
			++MACconpuntos;

			if ((ch < '0' || ch > '9') && (ch < 'a' || ch > 'f'))
			{
				return NULL;
			}

			iNumber <<= 4;
			iNumber += isdigit (ch) ? (ch - '0') : (ch - 'a' + 10);
			ch = *MACconpuntos;

			if (i< 5 && ch!=punto)
			{
				return NULL;
			}
		}
		/*Se manda a la variable a retornar*/
		MACsinpuntos[i]=(unsigned char)iNumber;
		/*brinca el espacio*/
		++MACconpuntos;
	}
	return MACsinpuntos;
}

void VerificarSolicitudARPGratuita(unsigned char *trama, int descriptor_socket)
{
	unsigned char TPA[50];//Target IP con puntitos
	unsigned char SPA[50];//Sender IP con puntitos
	unsigned char MACtrama[100];
	char *MAC=(char*)malloc(sizeof(char));//Variable donde se guardara la MAC perteneiente a la IP que sea buscada en la base de datos 

	/*Guardamos lo datos de la trama recibid sin puntitos para poder utilizarlas en la estructuacion de las tramas
	de solicitud y respuesta ARP gratuito*/
	unsigned char MACsender[6];
	unsigned char IPsender[4];
	unsigned char MACtarget[6];
	unsigned char IPtarget[4];
	memcpy(MACsender, trama+6, 6);//MACinfractor
	memcpy(IPsender, trama+28, 4);//IPdefender o 0.0.0.0.
	memcpy(MACtarget, trama+32, 6);
	memcpy(IPtarget, trama+38, 4);//IPdefender

	if(!memcmp(trama+28, IPcero, 4))//si SPA=0.0.0.0, toamos TPA=IPdefender
	{
		sprintf(TPA, "%d.%d.%d.%d", trama_ARP_gratuito[38], trama_ARP_gratuito[39], trama_ARP_gratuito[40], trama_ARP_gratuito[41]);
		printf("\nTPA: %s", TPA);
		/*printf("TPA: ");

		for(int i=0; i<4; i++)
			printf("%s", TPA[i]);*/

		if(VerificarIPBaseDatos(TPA))//Verificamos que la IP target este en la Base de Datos
		{
                        printf("\nSi encontro IP tpa");
			MAC=ConsultarMAC(TPA);//MACdefender (con formato de puntitos)
			sprintf(MACtrama, "%2x:%2x:%2x:%2x:%2x:%2x", trama_ARP_gratuito[6], trama_ARP_gratuito[7], trama_ARP_gratuito[8], trama_ARP_gratuito[9], trama_ARP_gratuito[10], trama_ARP_gratuito[11]);

			if(!memcmp(MAC, MACtrama, 17))
			{
				/*No se hace nada, pues la MAC recibida en a trama esta registrada en la Base de Datos*/
			}
			else
			{
				EstructuraRespuestaARPGratuito(trama_ARP_Respuesta, MACsender, MACsinpuntos(MAC), IPtarget);
				printf("\n----------Respuesta ARP Gratuito----------");
				ImprimirTrama(trama_ARP_Respuesta,	60);//imprimimos trama a enviar
				printf("\n");
				EnviarTrama(packet_socket, indice, trama_ARP_Respuesta);

				EstructuraSolicitudARPGratuito(trama_Solicitud_ARP_gratuito, MACsinpuntos(MAC) , IPtarget);
				printf("\n----------Solicitd ARP Gratuito----------");
				ImprimirTrama(trama_Solicitud_ARP_gratuito,	60);//imprimimos trama a enviar
				printf("\n");
				EnviarTrama(packet_socket, indice, trama_Solicitud_ARP_gratuito);
			}
		}
	}
	else//si SPA=IP del defensor, lo tomamos
	{
		sprintf(SPA, "%d.%d.%d.%d", trama_ARP_gratuito[28], trama_ARP_gratuito[29], trama_ARP_gratuito[30], trama_ARP_gratuito[31]);
		printf("\nSPA: %s", SPA);

		/*printf("SPA: ");

		for(int i=0; i<4; i++)
			printf("%s", SPA[i]);*/

		if(VerificarIPBaseDatos(SPA))//Verificamos que la IP target este en la Base de Datos
		{
			printf("\nSi encontro IP spa");
			MAC=ConsultarMAC(SPA);
			sprintf(MACtrama, "%2x:%2x:%2x:%2x:%2x:%2x", trama_ARP_gratuito[6], trama_ARP_gratuito[7], trama_ARP_gratuito[8], trama_ARP_gratuito[9], trama_ARP_gratuito[10], trama_ARP_gratuito[11]);

			if(!memcmp(MAC, MACtrama, 17))
			{
				/*No se hace nada, pues la MAC recibida en a trama esta registrada en la Base de Datos*/
			}
			else
			{
				EstructuraRespuestaARPGratuito(trama_ARP_Respuesta, MACsender, MACsinpuntos(MAC), IPsender);
				printf("\n----------Respuesta ARP Gratuito----------");
				ImprimirTrama(trama_ARP_Respuesta,	60);//imprimimos trama a enviar
				printf("\n");
				EnviarTrama(packet_socket, indice, trama_ARP_Respuesta);

				EstructuraSolicitudARPGratuito(trama_Solicitud_ARP_gratuito, MACsinpuntos(MAC), IPsender);
				printf("\n----------Solicitd ARP Gratuito----------");
				ImprimirTrama(trama_Solicitud_ARP_gratuito,	60);//imprimimos trama a enviar
				printf("\n");
				EnviarTrama(packet_socket, indice, trama_Solicitud_ARP_gratuito);

			}
		}
	}
}

//FUncion que recibe una Solicitud ARP o Solicitud ARP gratuita en trama_ARP_gratuito y la filtra
void RecibeARPGratuito(int descriptor_socket, unsigned char *trama)
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
			if(!memcmp(trama+0, MACbroadcast, 6))//MACbroadcast=ff:ff:ff:ff:ff:ff
			{
				if(!memcmp(trama+12, ethertype, 2))//ethertype=0806
				{
					if(!memcmp(trama+20, opcode, 2))//opcode= 0001
					{
						if(!memcmp(trama+28, trama+38, 4) || !memcmp(trama+28, IPcero, 4))//IPorigen(SHA) = IPdestino(TPA) ó SHA=0.0.0.0
						{
									printf("\n----------Trama ARP Gratuita recibida----------");
									ImprimirTrama(trama, tam);
									VerificarSolicitudARPGratuita(trama, packet_socket);
									//break;
						}
					}	
				}
			}

		}	
	}
}

int main()
{
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
		RecibeARPGratuito(packet_socket, trama_ARP_gratuito);
	}

close(packet_socket);
return 0;
}