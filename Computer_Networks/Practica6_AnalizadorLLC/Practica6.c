/*
Practica 6: Analizador de Tramas LLC
Redes de Computadoras
Hecho por Mauro Sampayo HernÃandez

Compilacion: gcc -o Practica6 Practica6.c
*/
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <linux/if_packet.h>
#include <net/ethernet.h> /* the L2 protocols */
#include <sys/ioctl.h>
#include <net/if.h>

unsigned char trama_LLC[1514];
unsigned char MACorigen[6];
unsigned char MACorigenLLC[6];
unsigned char MACdestino[6];
unsigned char IPorigen[4];

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

//Funcion que analiza y determina el tipo de SAP de la trama LLC
void AnalisisSAP(unsigned char sap)
{
	switch(sap&0xFE)
	{
		case 0x00:printf("\n Null LSAP: ");break;
		case 0x02:printf("\n LLC Sublayer Management Function: ");break;
		case 0x04:printf("\n IBM SNA Path Control:");break;
		case 0x06:printf("\n ARPANET Internet Protocol (IP):");break;
		case 0x08:printf("\n SNA: ");break;
		case 0x0E:printf("\n PROWAY (IEC955) Network Management & Initialization: ");break;
		case 0x18:printf("\n Texas Instruments: ");break;
		case 0x42:printf("\n IEEE 802.1 Bridge Spanning Tree Protocol: ");break;
		case 0x4E:printf("\n EIA RS-511 Manufacturing Message Service: ");break;
		case 0x7E:printf("\n ISO 8208 (X.25 over IEEE 802.2 Type 2 LLC): ");break;
		case 0x80:printf("\n Xerox Network Systems (XNS: ");break;
		case 0x86:printf("\n Nestar: ");break;
		case 0x8E:printf("\n PROWAY (IEC 955) Active Station List Maintenance: ");break;
		case 0x98:printf("\n ARPANET Address Resolution Protocol (ARP): ");break;
		case 0xBC:printf("\n Banyan VINES: ");break;
		case 0xAA:printf("\n SubNetwork Access Protocol (SNAP): ");break;
		case 0xE0:printf("\n Novell NetWare: ");break;
		case 0xF0:printf("\n IBM NetBIOS: ");break;
		case 0xF4:printf("\n IBM LAN Management: ");break;
		case 0xF8:printf("\n IBM Remote Program Load (RPL): ");break;
		case 0xFA:printf("\n Ungermann-Bass: ");break;
		case 0xFE:printf("\n ISO Network Layer Protocol: ");break;
		case 0xFF:printf("\n Global LSAP: ");break;
		default:break;
	}
}

void TramaNoNumerada(unsigned char byte, int bandera)
{
	if(bandera==2)//P(Comando)
    {
        switch(byte&0xEC)
        {
            case 0x80:printf("Set normal response SNRM");break;  
            case 0xCC:printf("Set normal response extended mode SNRME");break;
            case 0x0C:printf("Set asincronous response SARM");break;
            case 0x4C:printf("Set asincronous response extended mode SARME");break;
            case 0x2C:printf("Set asincronous balance mode SABM");break;
            case 0x6C:printf("Set asincronous balance extended mode SABME");break;
            case 0x04:printf("Set inicialitation mode SIM");break;
            case 0x40:printf("Disconect DISC");break;                        
            case 0x20:printf("Unnumbered Poll Up");break;
            case 0x8C:printf("Reset RSET");break;
        }
    }
    if(bandera==1)//F(Respuesta)
    {
        switch(byte&0xEC)
        {
            case 0x60:printf("Unnumbered Acknowledgment UA");break;                        
            case 0x0C:printf("Disconect mode DM");break;
            case 0x40:printf("Request disconect RD");break;
            case 0x01:printf("Request Initialitacion Mode RIM");break;
            case 0x81:printf("Frame reject FRMR");break;
        }
    }

    switch(byte&0xEC)//P/F(C/R)
    {
        case 0x00:printf("Unnumered informacion UI");break;
        case 0xAC:printf("Exchange identification XID");break;
        case 0xE0:printf("Test TEST");break;
    }
}

void NR(unsigned char byte)
{
	/*unsigned char res=byte&0xFE;
	printf("|%.2x|", res);*/
	int NR;
	NR= byte/2;
	printf(" N(R): %d", NR);
}

void NS(unsigned char byte)
{
	int NS;
	NS= byte/2;
	printf(" N(S): %d", NS);
}

void TramaSupervision(unsigned char byte)
{
	switch((byte&0x0C))
    {
        case 0:printf("Receive ready (RR)");break;
        case 4:printf("Receive Not Ready (RNR)");break;
        case 8:printf("Reject (REJ)");break;
        case 12:printf("Selective Reject (SREJ)");break;
    }
}

//Funcion que realiza el analisis de los bits de la trama LLC
void AnalisisTramaLLC(unsigned char *trama, int longitud)
{
	int i, bandera=0;
	printf("\n----------Analisis Trama LLC recibida----------");
	
	//Analisis de la MACorigen y la MACdestino
	memcpy(MACdestino, trama+0, 6);
	memcpy(MACorigen, trama+6, 6);
	printf("\n\nMAC Destino: ");
	
	for(i=0; i<6; i++)
		printf("%.2x:", MACdestino[i]);
	
	printf("\nMAC Origen: ");
	
	for(i=0; i<6; i++)
		printf("%.2x:", MACorigen[i]);
		
	//Analisis de la longitud de la trama
	printf("\nLongitud: %d", longitud);
	
	//Analisis DSAP
	printf("\nDSAP");
	AnalisisSAP(trama[14]);

	if((trama[14]&0x01)==1)//Ultimo bit es 1
		printf("Trama de Grupo");
	if((trama[14]&0x01)==0)//Ultimo bit es 0
		printf("Trama Invividual");

	//Analisis SSAP
	printf("\nSSAP");
	AnalisisSAP(trama[15]);

	if((trama[15]&0x01)==1)//Ultimo bit es 1
	{
		printf("Trama de Respuesta");
		bandera=1;
	}
	if((trama[15]&0x01)==0)//Ultimo bit es 0
	{
		printf("Trama de Comando");
		bandera=2;
	}
	
	//Analisis Control
	printf("\nAnalisis Control");

	switch(trama[16]&0x03)
	{
		case 0x00: printf("\n Trama de información: "); NS(trama[16]); NR(trama[17]); break;
		case 0x01: printf("\n Trama de supervisión: "); TramaSupervision(trama[16]); NR(trama[17]); break;//Ultimos bits=01
		case 0x02: printf("\n Trama de información: "); NS(trama[16]); NR(trama[17]); break;//Ultimo bit=0
		case 0x03: printf("\n Trama no numerada: "); TramaNoNumerada(trama[16], bandera); break;//Ultimos bits=11
		default: break;
	}	
}

//Funcion que recibe una Solicitud ARP o Solicitud ARP gratuita en trama_ARP_gratuito y la filtra
void RecibeTramaLLC(int descriptor_socket, unsigned char *trama)
{
	int tam, tamanio;

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
			/*x<<y ---> x*2^y      x>>y ---> x/2^y*/
			tamanio=(trama[12]<<8)+trama[13];//(trama[12]*2^8)+trama[13] ---> (trama[12]*256)+trama[13]
			
			if(tamanio<1500)//Si el valor de la longitud de datos es menor a 1500(pag 163)
			{
				printf("\n\n----------Trama LLC recibida----------");
				ImprimirTrama(trama, tam);
				AnalisisTramaLLC(trama, tamanio);
				//break;
			}

		}	
	}
}

int main()
{
	int packet_socket;
	packet_socket=socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL));
	
	if(packet_socket==-1)
	{
		perror("\nError al abrir el socket");
		exit(1);
	}
	else
	{
		perror("\nExito al abrir el socket");
		RecibeTramaLLC(packet_socket, trama_LLC);
	}
	
	close(packet_socket);
	return 0;
}