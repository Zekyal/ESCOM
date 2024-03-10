/*
Practica 9: Analizador UDP
Redes de Computadoras
Hecho por Mauro Sampayo Hernandez

Compilacion: gcc -o Practica9 Practica9.c
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ioctl.h>
#include <sys/socket.h>
#include <netpacket/packet.h>
#include <net/ethernet.h>
#include <sys/types.h>
#include <net/if.h>
#include <arpa/inet.h>
#include <asm/types.h>
#include <unistd.h>
#include <sys/time.h>
#include <errno.h> 
#include <netdb.h> 
#include <netinet/ip.h>
#include <net/if_arp.h> 
#include <netinet/udp.h>

typedef struct sred
{
    int indice,paquete;
    unsigned char IPorigen[4];
    unsigned char MACorigen[6];
    unsigned char MascaraSubred[4];
    unsigned char IPenlace[4];
    unsigned char MACenlace[6];
}sred;

unsigned char MACdestino[6];
unsigned char IPdestino[4];
unsigned char IPaux[4];
sred *red=NULL;
FILE *puerta, *IPpuerta;
unsigned char trama_ARP_Solicitud[60]={0xff,0xff,0xff,0xff,0xff,0xff,0x00,0x00,0x00,0x00,
0x00,0x00,0x08,0x06,0x00,0x01,0x08,0x00,0x06,0x04,
0x00,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,'M','S','H'};
unsigned char trama_ARP_Respuesta[1514];
unsigned char trama_DNS_Solicitud[62]={/*Encabezado MAC*/0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x08,0x00,/*Encabezado IP(byte 14-33)*//*version IP*/0x45,/*tipo de servicio*/0x00,/*long IP*/0x00,0x30,/*identificador*/0x00,0x01,
/*banderas y desp*/0x00,0x00,/*ttl*/0x00/*0x40?*/,/*protocolo ICMP*/0x11,/*ckecksum*/0x00,0x00,/*direcciones*/0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,/*Encabezado UDP*//*puerto origen*/0xbb,0xbb,/*puerto destino*/0x00,0x00/*0x35?*/,/*longitud(20+8 bytes)*/0x00,0x1C,
/*checksum*/0x00,0x00,/*datos*/0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00};
unsigned char pseudoencabezado_UDP[40]={/*Pseudocabecera UDP*//*direcciones*/0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,/*no usado*/0x00,/*protocolo*/0x11,
/*longitud*/0x00, 0x1C,/*Encabezado UDP*//*puerto origen*/0xbb,0xbb,/*puerto destino*/0x00,0x00,/*longitud(20+8 bytes)*/0x00,0x1C,/*checksum*/0x00,0x00,
/*datos*/0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
unsigned char trama_ICMP_error[1514];
unsigned char ethertypePING[2]={0x08,0x00};
unsigned char opcoderespuesta[2]={0x00,0x02};

sred* ObtenerDatos(char* interfaz, int descriptor_socket);
void Parametros(char* dest);
void ImprimirIP(unsigned char* IP);
void ImprimirMAC(unsigned char* MAC);
char* ConvertirHostnameAIP(char* hostname);
void ImprimirTrama(unsigned char* trama, int tam);
void EstructuraARPSolicitud(sred *red, int bandera, unsigned char *trama);
int ComprobarRed(sred *red);
int RecibeARPRespuesta(sred *red, unsigned char* trama);
void EnviaARPSolicitud(sred *red, unsigned char *trama);
void Checksum(int limi, int lims, unsigned char *check0, unsigned char *check1, unsigned char *trama);
int RecibeTramaICMP(sred *red, unsigned char* trama);
int EnviaTramaUDP(sred *red, unsigned char *trama);
int EstructuraTramaUDP(sred* red, int puerto_destino, int ttl, int bandera, unsigned char *trama);

int main()
{
	int packet_socket = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL));
	int i, ttl=64, ciclo, contopen=0, contclose=100;
	char *interfaz=(char*)malloc(32*sizeof(char));
	char *destino=(char*)malloc(32*sizeof(char));

	
	if(packet_socket==-1)
	{
		perror("\nError al abrir el socket");
		exit(1);
	}
	else
	{
		printf("Destino: ");
    	scanf("%s",destino);
    	printf("Interfaz por la que se realizara la Solicitud DNS: ");
        scanf("%s",interfaz);
        Parametros(destino);
        //printf("\n-----Datos interfaz de red-----");
        red=ObtenerDatos(interfaz,packet_socket);
        printf("\nAnalizando puertos de %s [", destino);
        ImprimirIP(IPdestino);
        printf("]\n");
		
		if(ComprobarRed(red))
        {
            printf("\nDestino dentro de la red");
            EstructuraARPSolicitud(red,1,trama_ARP_Solicitud);
            EnviaARPSolicitud(red, trama_ARP_Solicitud);

            for(ciclo=0;ciclo<100;ciclo++)
            {
                if(EstructuraTramaUDP(red, ciclo+1, ttl, 1, trama_DNS_Solicitud))
                {
                	printf("\nPuerto %d/ Abierto", ciclo+1);
                	contopen++;
                }
            }
        }
        else
        {
            printf("\nDestino fuera de la red");
            EstructuraARPSolicitud(red,0,trama_ARP_Solicitud);
            EnviaARPSolicitud(red,trama_ARP_Solicitud);

            for(ciclo=0; ciclo<100; ciclo++)
            {
                if(EstructuraTramaUDP(red, ciclo+1, ttl, 0, trama_DNS_Solicitud))
                {
                	printf("\nPuerto %d/ Abierto", ciclo +1);
                	contopen++;
                }
            }
        }
        //Estadisticas UDP

        contclose=100-contopen;
        printf("\n\nPUERTOS CERRADOS: %d\n", contclose);
        printf("PUERTOS ABIERTOS: %d\n", contopen);
    }

return 0;
}

sred* ObtenerDatos(char *interfaz, int descriptor_socket)
{
    struct ifreq nic;
	sred *nvor;
    strcpy(nic.ifr_name, interfaz);//pasamos el nombre de la interfaz al nic
	nvor=(sred *)malloc(sizeof(sred));
	nvor->paquete=descriptor_socket;

    if(ioctl(descriptor_socket,SIOCGIFINDEX,&nic)==-1)
    {
        perror("\nError al obtener indice");
        exit(-1);
    }

    nvor->indice=nic.ifr_ifindex;
    //printf("\nEl índice es: %d", nic.ifr_ifindex);
        
    if(ioctl(descriptor_socket,SIOCGIFHWADDR,&nic)==-1)//obtenemos la direccion MAC
    {
        perror("\nError al obtener la direccion MAC");
        exit(1);
    }
    else
    {
        memcpy(nvor->MACorigen+0,nic.ifr_hwaddr.sa_data,6);//la direccion MAC se guardara en sa_data
        //printf("\nDIreccion MAC: ");
        //ImprimirMAC(nvorMACorigen);

        if(ioctl(descriptor_socket,SIOCGIFADDR,&nic)==-1)//obtenemos la direccion IP
        {
                perror("\nError al obtener la direccion IP");
                exit(1);
        }
        else
        {
            memcpy(nvor->IPorigen+0,nic.ifr_addr.sa_data+2,4);//la direccion IP se guardara en sa_data
            //printf("\nDireccion IP: ");
            //ImprimirIP(nvor->IP);
            
            if(ioctl(descriptor_socket,SIOCGIFNETMASK,&nic)==-1)//obtenemos la mascara de subred
            {
                    perror("\nError al obtener la mascara de subred");
                    exit(1);
            }
            else
            {
                memcpy(nvor->MascaraSubred,nic.ifr_netmask.sa_data+2,4);//la mascara de subred se guardara en sa_data
                /*Hace una llamada a la terminal para que esta muestre los datos de la tabla arp,para de esa manera obtener la puerta de enlace
                a la cual deberemos acceder para realizar el Ping. Este sera guardado posteriorimente en un archivo, el cual sera usado como un repositorio
                de los datos de la Puerta de Enlace y sera abierto en modo lectura para posteriorimente copiar los datos de la Puerta de Enlace
                y poder mostrarlos en pantalla*/
                //printf("\nMascara de Subred: ");
                //ImprimirIP(nvor->MascaraSubred);
                system("routel|grep default > PuertaEnlaceIP.txt");
                unsigned char a;
                unsigned char stripenlace[15];
                if((IPpuerta=fopen("PuertaEnlaceIP.txt","r"))!=NULL)
                {
                	while(a!='1' && a!='2' && a!='3' &&a!='4' &&a!='5' &&a!='6' &&a!='7' &&a!='8' &&a!='9' && a!='0')
                		a = fgetc(IPpuerta);	
                
	                int i=0;
    	            while(a != ' ')
        	        {
        	        	stripenlace[i]=a;
            	    	a = fgetc(IPpuerta);
                		i++;
                	}
                }
                else
                {
                    printf("\nError al abrir el archivo");
                    exit(-1);
                }
                
                printf("%s\n", stripenlace);
                unsigned char comando[50];
				sprintf(comando,"arp -an %s > PuertaEnlaceMAC.txt",stripenlace);
				printf("%s\n", comando);
                system(comando);
                
                if((puerta=fopen("PuertaEnlaceMAC.txt","r"))!=NULL)
                {
                    fscanf(puerta,"? (%d.%d.%d.%d) en %x:%x:%x:%x:%x:%x",(int*)&nvor->IPenlace[0],(int*)&nvor->IPenlace[1],(int*)&nvor->IPenlace[2],(int*)&nvor->IPenlace[3],(unsigned int*)&nvor->MACenlace[0],(unsigned int*)&nvor->MACenlace[1],(unsigned int*)&nvor->MACenlace[2],(unsigned int*)&nvor->MACenlace[3],(unsigned int*)&nvor->MACenlace[4],(unsigned int*)&nvor->MACenlace[5]);
                    printf("\nDireccion IP Puerta de Enlace: ");
                    ImprimirIP(nvor->IPenlace);
                    printf("\nDireccion MAC Puerta de Enlace: ");
                    ImprimirMAC(nvor->MACenlace);
                }
                else
                {
                    printf("\nError al abrir el archivo");
                    exit(-1);
                }
            }
        }
    }    
    
    fclose(puerta);
    return nvor;
}

void Parametros(char *destino)
{
    if(destino[0]=='w'&& destino[1]=='w' && destino[2]=='w')
    {
        char *IPhost;
        IPhost=ConvertirHostnameAIP(destino);//Obtener la IP del host a partir de su nombre
        //printf("Destino:%s \nIP:%s\n", destino,IPhost);
        sscanf(IPhost," %d.%d.%d.%d",(int*)&IPdestino[0],(int*)&IPdestino[1],(int*)&IPdestino[2],(int*)&IPdestino[3]);
    }
    else
    {
        //printf("Destino:%s\n", destino);
        sscanf(destino,"%d.%d.%d.%d",(int*)&IPdestino[0],(int*)&IPdestino[1],(int*)&IPdestino[2],(int*)&IPdestino[3]);
    }
}

char* ConvertirHostnameAIP(char *hostname)
{
    struct hostent *he;
    struct in_addr **addr_list;
    int i;
    char* ip;
    ip=(char*)malloc(15*sizeof(char)); 

    if ( (he = gethostbyname( hostname ) ) == NULL)// get the host info
        herror("gethostbyname");
 
    addr_list = (struct in_addr **) he->h_addr_list;
     
    for(i = 0; addr_list[i] != NULL; i++)
        strcpy(ip , inet_ntoa(*addr_list[i]));
     
    return ip;
}

void ImprimirIP(unsigned char *IP)
{
    int i;

	for(i=0;i<4;i++)
		printf("%d.",IP[i]);
}

void ImprimirMAC(unsigned char *MAC)
{
    int i;

	for(i=0;i<6;i++)
        printf("%.2x:",MAC[i]);
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

int ComprobarRed(sred *red)
{
    int i;
    unsigned char IPori[4];
    unsigned char IPdest[4];

    for(i=0;i<4;i++)
    {
        IPori[i]=red->IPorigen[i]&red->MascaraSubred[i];
        IPdest[i]=IPdestino[i]&red->MascaraSubred[i];
    }

    if(!memcmp(IPori,IPdest,4))
        return 1;
    else
        return 0;
}

void EstructuraARPSolicitud(sred *red,int bandera,unsigned char *trama)
{
   	memcpy(trama+6,red->MACorigen,6);
	//Direccion Origen
   	memcpy(trama+22,red->MACorigen,6);
    memcpy(trama+28,red->IPorigen,4);
   	//Direccion Destino

    if(bandera==1)//Destino dentro de la red
	{
		memcpy(trama+32,MACdestino,6);
    	memcpy(trama+38,IPdestino,4);
	}
	else//Destino fuera de la red
	{
		memcpy(trama+32,red->MACenlace,6);
    	memcpy(trama+38,red->IPenlace,4);
	}
}

void EnviaARPSolicitud(sred *red, unsigned char *trama)
{
    int tam;
    struct sockaddr_ll capaEnlace;
    memset(&capaEnlace, 0, sizeof(capaEnlace));//?
    capaEnlace.sll_family=AF_PACKET;
    capaEnlace.sll_protocol=htons(ETH_P_ALL);
    capaEnlace.sll_ifindex = red->indice;
    tam = sendto(red->paquete, trama, 65, 0, (struct sockaddr *)&capaEnlace, sizeof(capaEnlace));

    if(tam==-1)     
    {
        perror("\nError al enviar trama ARP");
        exit(1);
    }
    else
    {
        ImprimirTrama(trama, tam);
        if(RecibeARPRespuesta(red, trama_ARP_Respuesta))
            printf("\nRespuesta Fallida");
    }
}

int RecibeARPRespuesta(sred *red, unsigned char* trama)
{
    int tam;
    struct timeval start, end;
    double time;
	gettimeofday(&start, NULL);
        
    while(time<200)
    {
        tam=recvfrom(red->paquete, trama, 1514, 0, NULL, 0);
        //ImprimirTrama(trama, tam);

        if(tam==-1)
        {
            perror("\nError al recibir trama ARP");
            exit(1);
        }
        else
        {
            if(!memcmp(trama+20,opcoderespuesta,2)&&!memcmp(trama+0,red->MACorigen,6)&&!memcmp(trama+28,IPdestino,4)&&!memcmp(trama+28,IPdestino,4))
            {
                memcpy(MACdestino,trama+6,6);
                printf("\nLa MAC de la IP ");
                ImprimirIP(IPdestino);
                printf(" es: ");
                ImprimirMAC(MACdestino);
                printf("\n");
                return 0;
            }
        }
        gettimeofday(&end, NULL);
        time =(end.tv_sec - start.tv_sec)*1000 + (end.tv_usec - start.tv_usec)/1000.0;
    }
    
    printf("Elapsed time: %f milliseconds", time);
    return 1;
}

void Checksum(int limi, int lims, unsigned char *check0, unsigned char *check1, unsigned char *trama)
{
    int i;
	unsigned int suma=0;
	unsigned short aux;

	for(i=limi;i<lims;i+=2)
	{
		aux=trama[i];
		aux=(aux<<8)+trama[i+1];
		suma=suma+aux;
	}

	suma=(suma&0x0000FFFF)+(suma>>16);
	*check0=(unsigned char)~(suma);
    *check1=(unsigned char)~(suma>>8);
}

int RecibeTramaICMP(sred *red, unsigned char* trama)
{
    //printf("RecibeTramaPING\n");
    int tam;
    struct timeval start, end;
    long int ptime=0;
	gettimeofday(&start, NULL);

    while(ptime < 200)//ciclo que recibira tramas
    {
        tam=recvfrom(red->paquete,trama,1514,0,NULL,0);

        if(tam==-1)
        {
            perror("Error al recibir trama ICMP");
            exit(1);
        }
        else
        {
            if(trama[34]==0x03&&trama[35]==0x03&&!memcmp(trama+54,red->IPorigen,4)&&!memcmp(trama+58,IPdestino,4))//Contesta un ICMP, indicando que el destino es inalcanzable, pero que esta abierto
                return 1;
        }
        gettimeofday(&end, NULL);
        ptime =(end.tv_sec - start.tv_sec)*1000 + (end.tv_usec - start.tv_usec)/1000;
        //printf("no\n");
    }

    return 0;//Host cerrado :c
}

int EnviaTramaUDP(sred *red, unsigned char *trama)
{
    //printf("EnviaTramaPING\n");
    int tam;
    struct sockaddr_ll capaEnlace;
    memset(&capaEnlace, 0x00, sizeof(capaEnlace));//?
    capaEnlace.sll_family=AF_PACKET;
    capaEnlace.sll_protocol=htons(ETH_P_ALL);
    capaEnlace.sll_ifindex=red->indice;
    tam=sendto(red->paquete, trama,62 ,0,(struct sockaddr*)&capaEnlace, sizeof(capaEnlace));
    
    if(tam==-1)
    {
        perror("\nError al enviar trama");
        exit(1);
    }
	else
	{
        //ImprimirTrama(trama, tam);
        if(RecibeTramaICMP(red, trama_ICMP_error))
            return 1;
        else
            return 0;
    }		
}

int EstructuraTramaUDP(sred* red, int puerto_destino, int ttl, int bandera, unsigned char *trama)
{
	memset(trama+24, 0x00, 2);
	memset(trama+40, 0x00, 2);

	if(bandera)//Destino dentro de la red
		memcpy(trama+0, MACdestino, 6);
	else//Destino fuera de la red
		memcpy(trama+0, red->MACenlace, 6);

    memcpy(trama+6, red->MACorigen, 6);
    trama[12]=0x08;
    trama[13]=0x00;    
    trama[14]=0x45;
    trama[15]=0x00;
    trama[16]=0x00;
	trama[17]=0x30;
	trama[18]=0x00;
    trama[19]=0x01;
    trama[20]=0x00;
    trama[21]=0x00;	
    memcpy(trama+22, &ttl, 1);
    trama[23]=0x11;//protocolo
	memcpy(trama+26, red->IPorigen, 4);
    memcpy(trama+30, IPdestino, 4);
	Checksum(14, 33, &trama[25],&trama[24], trama);

	//Trama UDP y ancabezado
	trama[34]=pseudoencabezado_UDP[12]=0xbb;//Puerto Origen
    trama[35]=pseudoencabezado_UDP[13]=0xbb;
    trama[36]=pseudoencabezado_UDP[14]=0x00;//Puerto Destino
    memcpy(trama+37, &puerto_destino, 1);
    memcpy(pseudoencabezado_UDP+15, &puerto_destino, 1);
    trama[38]=pseudoencabezado_UDP[16]=0x00;//Longitud UDP
    trama[39]=pseudoencabezado_UDP[17]=0x1C;

    //Pseudoencabezado
    memcpy(pseudoencabezado_UDP+0, red->IPorigen, 4);
    memcpy(pseudoencabezado_UDP+4, IPdestino, 4);
    pseudoencabezado_UDP[8]=0x00;
    pseudoencabezado_UDP[9]=0x11;//protocolo
    pseudoencabezado_UDP[10]=0x00;//Longitud UDP
    pseudoencabezado_UDP[11]=0x1C;

	Checksum(0, 39, &trama[41],&trama[40],pseudoencabezado_UDP);   //?     
	
	if(EnviaTramaUDP(red, trama_DNS_Solicitud))
		return 0;
    else
        return 1;
}