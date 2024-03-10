/*
Practica 7: PING
Redes de Computadoras
Hecho por Mauro Sampayo Hernandez

Compilación: gcc -o Practica7 Practica7.c
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

typedef struct sred
{
    int indice,paquete;
    unsigned char IPorigen[4];
    unsigned char MACorigen[6];
    unsigned char MascaraSubred[4];
    unsigned char IPenlace[4];
    unsigned char MACenlace[6];
}sred;

unsigned char IPdestino[4];
unsigned char MACdestino[6];
sred *red=NULL;
FILE *puerta, *IPpuerta;
int ctapack[3]={0,0,0},intime=0;
unsigned char ethertypePING[2]={0x08,0x00};
unsigned char trama_ARP_Solicitud[60]={0xff,0xff,0xff,0xff,0xff,0xff,0x00,0x00,0x00,0x00,
0x00,0x00,0x08,0x06,0x00,0x01,0x08,0x00,0x06,0x04,
0x00,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,'M','S','H'};
unsigned char trama_ECO_Solicitud[65]={/*Encabezado MAC*/0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x08,0x00,/*Encabezado IP(byte 14-33)*//*version IP*/0x45,/*tipo de servicio*/0x00,/*long IP*/0x00,0x00,/*identificador*/0x00,0x00,
/*banderas y desp*/0x00,0x00,/*ttl*/0x00,/*protocolo ICMP*/0x01,/*ckecksum*/0x00,0x00,/*direcciones*/0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,/*Encabezado ICMP*//*codigo*/0x08,0x00,/*checksum*/0x00,0x00,/*identificador*/0x00,0x00,
/*numero de secuencia*/0x00,0x00,/*datos*/0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00};
unsigned char trama_ARP_Respuesta[1514];
unsigned char opcoderespuesta[2]={0x00,0x02};

void Parametros(char *dest);
void ImprimirIP(unsigned char *IP);//imprimir datos del tIPo IP
void ImprimirMAC(unsigned char *MAC);//imprimir datos de tIPo MAC
sred * ObtenerDatos(char *interfaz,int descriptor_socket);
char* ConvertirHostnameAIP(char * hostname);
void EstadisticasPING(int *tiempopack,int pack);
int ComprobarRed(sred *red);//comprobar si la IP esta dentro o fuera de la subred
void Checksum(int limi, int lims, unsigned char *check0, unsigned char *check1, unsigned char *mtrama);
int RecibeTramaPING(sred *red,int *tiempopack,int sec,int tamtra, unsigned char* trama);
void EnviaTramaPING(sred *red,int *tiempopack,int sec,int tamtra, unsigned char *trama);
void EstructuraTramaPING(sred*red,int secuencia,int ttl,int bandera,int *tiempopack,char *mensaje, unsigned char *trama);
void RecibeARPRespuesta(sred *red,unsigned char* trama);
void ImprimirTrama(unsigned char *trama, int tam);
void EnviaARPSolicitud(sred *red, unsigned char *trama);
void EstructuraARP(sred *red,int bandera,unsigned char *trama);

int main()
{
    int packet_socket=socket(AF_PACKET,SOCK_RAW,htons(ETH_P_ALL)),ttl=64,pack=4,ciclo;
	char *mensaje=(char*)malloc(100*sizeof(char));
    strcpy(mensaje,"Mauro Sampayo Hernandez");
	char *interfaz=(char*)malloc(32*sizeof(char));
	char *destino=(char*)malloc(32*sizeof(char));

    if(packet_socket==-1)
    {
    	perror("error al abrir el socket");
    	return 1;
    }
    else
    {
        printf("PING ");
    	scanf("%s",destino);
    	printf("Interfaz por la que se realizara el ping: ");
        scanf("%s",interfaz);
        Parametros(destino);
        //printf("\n-----Datos interfaz de red-----");
        red=ObtenerDatos(interfaz,packet_socket);
		int tiempopack[pack];
        printf("\nHaciendo PING a %s [", destino);
        ImprimirIP(IPdestino);
        printf("]\n");
        //printf("\nMensaje:%s\n",mensaje);

        if(ComprobarRed(red))
        {
            printf("\nDestino dentro de la red");
            EstructuraARP(red,1,trama_ARP_Solicitud);
            EnviaARPSolicitud(red, trama_ARP_Solicitud);

            for(ciclo=0;ciclo<pack;ciclo++)
                EstructuraTramaPING(red,(ciclo)+1*(256),ttl,1,tiempopack,mensaje, trama_ECO_Solicitud); 
        }
        else
        {
            printf("\nDestino fuera de la red");
            EstructuraARP(red,0,trama_ARP_Solicitud);
            EnviaARPSolicitud(red,trama_ARP_Solicitud);

            for(ciclo=0;ciclo<pack;ciclo++)
                EstructuraTramaPING(red,(ciclo+1)*(256),ttl,0,tiempopack,mensaje, trama_ECO_Solicitud);
        }
        EstadisticasPING(tiempopack,pack);
    }
    return 0;
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

char* ConvertirHostnameAIP(char * hostname)
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

void RecibeARPRespuesta(sred *red, unsigned char* trama)
{
    int tam, bandera=1;
    struct timeval start, end;
    double time;
	gettimeofday(&start, NULL);
        
    while(time<2000)
    {
        tam=recvfrom(red->paquete, trama, 48 , 0, NULL, 0);

        if(tam==-1)
        {
            perror("\nError al recibir trama");
            exit(1);
        }
        else
        {
            if(!memcmp(trama+20,opcoderespuesta,2)&&!memcmp(trama+0,red->MACorigen,6)&&!memcmp(trama+28,IPdestino,4))
            {
                memcpy(MACdestino+0,trama+6,6);
                printf("\nLa MAC de la IP ");
                ImprimirIP(IPdestino);
                printf(" es; ");
                ImprimirMAC(MACdestino);
                printf("\n");
                bandera=0;
                break;
            }
        }
        gettimeofday(&end, NULL);
 	    time =(end.tv_sec - start.tv_sec)*1000 + (end.tv_usec - start.tv_usec)/1000.0;
    }

    if(bandera==1)
    	printf("\nRespuesta Fallida\n");
	
	printf("Elapsed time: %f milliseconds", time);
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
//
void EnviaARPSolicitud(sred *red,unsigned char *trama)
{
        int tam;
        struct sockaddr_ll capaEnlace;
        memset(&capaEnlace, 0x00, sizeof(capaEnlace));//?
        capaEnlace.sll_family=AF_PACKET;
        capaEnlace.sll_protocol=htons(ETH_P_ALL);
        capaEnlace.sll_ifindex = red->indice;
        tam = sendto(red->paquete, trama, 60, 0, (struct sockaddr *)&capaEnlace, sizeof(capaEnlace));

        if(tam==-1)     
        {
            perror("\nError al enviar trama");
            exit(1);
        }
        else
        {
        	//ImprimirTrama(trama, tam);
            RecibeARPRespuesta(red, trama_ARP_Respuesta);
        }
}
//
void EstructuraARP(sred *red,int bandera,unsigned char *trama)
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

void EstadisticasPING(int *tiempopack,int pack)
{
	int min, max, i, med=0;
	min=tiempopack[0];
	max=tiempopack[0];

	for(i=0;i<ctapack[1];i++)
	{
		//printf("%d  ",tiempopack[i]);
		if(tiempopack[i]<min)
			min=tiempopack[i];
		if(tiempopack[i]>max)
			max=tiempopack[i];
		med=med+tiempopack[i];
	}

	med=med/ctapack[1];
	printf("\n\nEstadísticas PING para ");
    ImprimirIP(IPdestino);
    printf(":");
	printf("\n\tPaquetes: Enviados=%d, Recibidos=%d, Perdidos=%d\t",ctapack[0],ctapack[1],ctapack[2]);
	printf("(%d %% ",(ctapack[2]*100)/pack);printf("perdidos)\n");
	printf("Iiempos aproximados de ida y vuelta en milisegundos:\n");
	printf("\tMinimo=%dms, Maximo=%dms, Media=%dms\n\n",min,max,med);
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

void Checksum(int limi, int lims, unsigned char *check0, unsigned char *check1, unsigned char *mtrama)
{
    int i;
	unsigned int suma=0;
	unsigned short aux;

	for(i=limi;i<lims;i+=2)
	{
		aux=mtrama[i];
		aux=(aux<<8)+mtrama[i+1];
		suma=suma+aux;
	}

	suma=(suma&0x0000FFFF)+(suma>>16);
	*check0=(unsigned char)~(suma);
    *check1=(unsigned char)~(suma>>8);
}

int RecibeTramaPING(sred *red,int *tiempopack,int sec,int tamtra, unsigned char* trama)
{
    int tam;
    struct timeval start, end;
    long int ptime=0;
	gettimeofday(&start, NULL);

    while(ptime < 100)//ciclo que recibira tramas
    {
        tam=recvfrom(red->paquete,trama,74,0,NULL,0);

        if(tam==-1)
        {
            perror("Error al recibir trama");
            exit(1);
        }
        else
        {
            //La IP destino recibe el paquete con exito
            if(!memcmp(trama,red->MACorigen,6)&&!memcmp(trama+12,ethertypePING,2)&&!memcmp(trama+26,IPdestino,4)&&!memcmp(trama+30,red->IPorigen,4))
            {
                gettimeofday(&end, NULL);
                ptime =(end.tv_sec - start.tv_sec)*1000 + (end.tv_usec - start.tv_usec)/1000;
                ctapack[1]++;
                tiempopack[intime]=ptime;
                intime++;
                printf("\nRespuesta desde: ");
                ImprimirIP(IPdestino);
                printf(": Bytes=74 Tiempo=%ldms TTL=%d",ptime,trama[22]);
				return 1;
            }
        }

        gettimeofday(&end, NULL);
        ptime =(end.tv_sec - start.tv_sec)*1000 + (end.tv_usec - start.tv_usec)/1000;
    }

    printf("\nRespuesta desde ");
    ImprimirIP(IPdestino);
    printf(": Tiempo de falla=%ldms TTL=%d",ptime,trama[22]);
    ctapack[2]++;
	return 0;
}

void EnviaTramaPING(sred *red,int *tiempopack,int sec,int tamtra, unsigned char *trama)
{
    //printf("Entre EnviaTramaPING");
    int tam;
    struct sockaddr_ll capaEnlace;
    memset(&capaEnlace, 0x00, sizeof(capaEnlace));
    capaEnlace.sll_family=AF_PACKET;
    capaEnlace.sll_protocol=htons(ETH_P_ALL);
    capaEnlace.sll_ifindex=red->indice;
    tam=sendto(red->paquete,trama,tamtra,0,(struct sockaddr*)&capaEnlace, sizeof(capaEnlace));
    
    if(tam==-1)
    {
        perror("\nError al enviar trama");
        exit(1);
    }
	else
	{
		//ImprimirTrama(trama, tam);
        ctapack[0]++;
        RecibeTramaPING(red,tiempopack,sec,tamtra,trama);
    }	
}

void EstructuraTramaPING(sred*red,int secuencia,int ttl,int bandera,int *tiempopack,char *mensaje, unsigned char *trama)
{
	memset(trama+24, 0x00, 2);
	memset(trama+36, 0x00, 2);

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
	trama[17]=28+strlen(mensaje);//longitud IP
	trama[18]=rand();
    trama[19]=0x00;
    trama[20]=0x00;
    trama[21]=0x00;	
    memcpy(trama+22,&ttl,1);
    trama[23]=0x01;
	memcpy(trama+26,red->IPorigen,4);
    memcpy(trama+30,IPdestino,4);
    trama[34]=0x08;
	Checksum(14,33,&trama[25],&trama[24],trama);
    trama[35]=0x00;
    trama[38]=0x01;
    trama[39]=0x00;;
    memcpy(trama+40,&secuencia,2);
	memcpy(trama+42,mensaje,strlen(mensaje));
	Checksum(34,65,&trama[37],&trama[36],trama);        
	EnviaTramaPING(red,tiempopack,secuencia,(42+strlen(mensaje)), trama_ECO_Solicitud);
}