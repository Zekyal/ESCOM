/*
Practica 5: Calculadora IP
Redes de Computadoras
Hecho por Mauro Sampayo Hernández

Compilación: gcc -o Practica5 Practica5.c -lm
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

void MostrarInformacionIP();
int VerificarIP(char *);
void subredesA();
void subredesB();
void subredesC();
void CalcularSubredes();
char* AdaptarMascara(int,int);
void CalcularHosts();
void HostA();
void HostB();
void HostC();
void CalcularPrefijo();
void PrefijoA();
void PrefijoB();
void PrefijoC();
void MostrarSubred();
void MuestraSubred(char *, int , int );
void DesplegarHostA(int,int,int,int,int,int);
void DesplegarHostB(int,int,int,int,int,int);
void DesplegarHostC(int,int,int,int,int);

unsigned char IP[4];//IP a Subredar
int Identificado_IP,Oct1,Oct2,Oct3;
char *mascaraAdaptada;
char *DatosIP;
int Host;
int incrementarSubred;
int bits;

int main()
{
  int opcion;
  char ip[15];

  do
  {
    system("clear");
    printf("==========CALCULADORA IP==========\n\n");
    printf("Inserte IP: ");//Insertamos la IP a calcular
    scanf("%s", ip);
    fflush(stdin);

    if(VerificarIP(ip)==0)//Si la IP o es válida u ocurre un error
    {
      printf("\nPorfavor ingrese una IP Válida. Presione una tecla para continuar...\n\n");
      getchar();
      getchar();
    }
    else
    {
      printf("\n-----INFORMACION DE LA IP-----\n\n");
      MostrarInformacionIP();
      printf("\n1. Calcular por Host\n");
      printf("2. Calcular por Subredes\n");
      printf("3. Calcular por Prefijo\n");
      printf("4. Mostrar Subred Especifica\n");
      printf("5. Insertar otra IP\n");
      printf("6. Finalizar\n");
      printf("\nIngrese el numero de la opcion: ");
      scanf("%d", &opcion);

      switch(opcion)
      {
        case 1:CalcularHosts();break;
        case 2:CalcularSubredes();break;
        case 3:CalcularPrefijo();break;
        case 4:MostrarSubred();break;
        case 5:break;
      }
    }
  }while(opcion!=6);

  return 0;
}

int VerificarIP(char *IPVerificar)
{
  struct sockaddr_in adr_inet;
  int flag=1;
  memset(&adr_inet,0,sizeof adr_inet);

  /*Función que convierte una cadea de texto, a una direcciṕn de Red. Devuelve 1 en caso de éxito(Dirección de Red
  se convirtió con éxito). Devuelve 0 si src no contiene una cadena de caracteres que representa una Dirección de Red
  válida*/
  if (!inet_pton(AF_INET, IPVerificar ,&adr_inet.sin_addr))
  {
    perror("\nLa cadena que inserto no es una Direccion de Red");
    flag=0;
  }
  else
  {
    memcpy(IP,&adr_inet.sin_addr,4);//Pasamos la DIrección de Red(una vex esta convertida) a IP

    if(IP[0]==0)//si la IP es 0.0.0.0 o inicia con 0
    {
      printf("\nERROR: IP no válida");
      flag=0;
    }
    else//Si es válida, asignamos ada octeto a una variable global, para usarlas en funcione posteriores
    {
      Identificado_IP=IP[0];
      Oct1=IP[1];
      Oct2=IP[2];
      Oct3=IP[3];
    }
  }

  return flag;
}

void  MostrarInformacionIP()
{
  //Verificamos si la IP es del tipo A
  if (Identificado_IP<=127)
  {
    printf("IP: %d.%d.%d.%d\nClase: A\nMascara de Red: 255.0.0.0\nTipo: Publica\n",Identificado_IP,Oct1,Oct2,Oct3);

    if (Identificado_IP==10)
      printf("IP: %d.%d.%d.%d\nClase: A\nMascara de Red: 255.0.0.0\nTipo: Privada\n",Identificado_IP,Oct1,Oct2,Oct3);
  }
  //Verificamos si la IP es del tipo B
  if ((Identificado_IP>=128) && (Identificado_IP<=191))
  {
    printf("IP: %d.%d.%d.%d\nClase: B\nMascara de Red: 255.255.0.0\nTipo: Publica\n",Identificado_IP,Oct1,Oct2,Oct3);

    if (Identificado_IP==172 && Oct1==16)
      printf("IP: %d.%d.%d.%d\nClase: B\nMascara de Red: 255.255.0.0\nTipo: Privada\n",Identificado_IP,Oct1,Oct2,Oct3);
  }
  //Verificamos si la IP es del tipo C
  if ((Identificado_IP>=192) && (Identificado_IP<=223))
  {
    printf("IP: %d.%d.%d.%d\nClase: C\nMascara de Red: 255.255.255.0\nTipo: Publica\n",Identificado_IP,Oct1,Oct2,Oct3);

    if (Identificado_IP==192 && Oct1==168)
      printf("IP: %d.%d.%d.%d\nClase: C\nMascara de Red: 255.255.255.0\nTipo: Privada\n",Identificado_IP,Oct1,Oct2,Oct3);
  }
}

/*Función que realiza el calculo del número de host de una IP, usando funciones deoendiendo de a que clase pertenezca la IP*/
void CalcularHosts()
{
  if (Identificado_IP<=127)
    HostA();
  if (Identificado_IP >= 128 && Identificado_IP <= 191)
    HostB();
  if (Identificado_IP>=192 && Identificado_IP<=223)
    HostC();
}

void HostA()
{
  int octeto1,octeto2,octeto3;
  int redesSolicitadas,bitsdeRed,noSubRedes,noHost,bitsHost,incrementoSubred,findesubred=0,flag=0,flag1=0;
  int binarios[]={128,64,32,16,8,4,2,1,128,64,32,16,8,4,2,1,128,64,32,16,8,4,2,1};
  FILE *fp=fopen("Hosts.txt", "w+");
  FILE *fp1=fopen("Busqueda Subred.txt","w+");

  do
  {
    printf("Ingresa el número de hosts que desea(Minimo:4 máximo:4194304): ");
    scanf("%d",&noHost);
    if(noHost >= 4 && noHost <= 16777216)
      flag1=1;
    else
    {
      printf("ERROR: Número de hosts no válido\n");
      flag1=0;
    }
  }while(flag1 != 1);
  //Calculamos los bits de host
  bitsHost=ceil(log(noHost)/log(2));
  //Calculamos los host totales
  noHost=pow(2,bitsHost);
  Host=noHost;
  //Calculamos el número de bits para la mascara de red adaptada
  bitsdeRed=24-bitsHost;
  bits=bitsdeRed;
  //Caclculamos el nuḿero de subredes
  noSubRedes=pow(2,bitsdeRed);
  //Buscamos la mascara adptada y el final de subred
  int i=bitsdeRed-1;
  incrementoSubred=binarios[bitsdeRed-1];
  incrementarSubred=incrementoSubred;
  while (!flag)
  {
    findesubred+=binarios[i];
    if (binarios[i]==128)
      flag=1;
    i--;
  }

  //Masacara adaptada//
  mascaraAdaptada=AdaptarMascara(bitsdeRed,findesubred);
  printf("\n-----CALCULO POR HOST-----\n\n");
  printf("Número de Subredes: %d\n",noSubRedes);
  printf("Número de Host: %d\n",noHost);
  printf("Máscara de Subred: %s\n\n", mascaraAdaptada);

  int id=1;
  if(bitsdeRed<=8)
  {
    for (octeto1=0;octeto1<=findesubred;octeto1+=incrementoSubred)
    {
      printf("| %d | %d.%d.0.0 |\n",id,Identificado_IP,octeto1 );
      fprintf(fp, "| %d | %d.%d.0.0 |\n",id,Identificado_IP,octeto1);
      fprintf(fp1, "| %d | %d.%d.0.0 |\n",id,Identificado_IP,octeto1);
      id++;
    }
  }
  if (bitsdeRed>=9 && bitsdeRed <= 16)
  {
    for (octeto2=0;octeto2<=255;octeto2++)
    {
      for (octeto1=0;octeto1<=findesubred;octeto1+=incrementoSubred)
      {
        printf("| %d | %d.%d.%d.0 |\n",id,Identificado_IP,octeto2,octeto1);
        fprintf(fp, "| %d | %d.%d.%d.0 |\n",id,Identificado_IP,octeto2,octeto1);
        fprintf(fp1, "| %d | %d.%d.%d.0 |\n",id,Identificado_IP,octeto2,octeto1);
        id++;
      }
    }
  }
  if (bitsdeRed>=17 && bitsdeRed<=24)
  {
    for (octeto3=0; octeto3<=255;octeto3++)
    {
      for (octeto2=0; octeto2<=255; octeto2++)
      {
        for (octeto1 = 0; octeto1 <= findesubred; octeto1+=incrementoSubred)
        {
          printf("| %d | %d.%d.%d.%d |\n",id,Identificado_IP,octeto3,octeto2,octeto1);
          fprintf(fp, "| %d | %d.%d.%d.%d |\n",id,Identificado_IP,octeto3,octeto2,octeto1);
          fprintf(fp1, "| %d | %d.%d.%d.%d |\n",id,Identificado_IP,octeto3,octeto2,octeto1);
          id++;
        }
      }
    }
  }

  printf("\nPresiona una tecla para continuar...\n");
  getchar();
  getchar();
  fclose(fp);
  fclose(fp1);
}

char* AdaptarMascara(int nobits,int findesubred)
{
  char *mascaraAda;
  mascaraAda=(char*)malloc(15);
  //Verificamos si la IP es del tipo A
  if (Identificado_IP<=127)
  {
    if (nobits <= 8)
      sprintf(mascaraAda,"255.%d.0.0",findesubred);
    if (nobits >= 9 && nobits <= 16)
      sprintf(mascaraAda,"255.255.%d.0",findesubred);
    if (nobits >= 17 && nobits <= 24)
      sprintf(mascaraAda,"255.255.255.%d",findesubred);
  }
  //Verificamos si la IP es del tipo B
  if ((Identificado_IP>=128) && (Identificado_IP<=191))
  {
    if (nobits <= 8)
      sprintf(mascaraAda,"255.255.%d.0",findesubred);
    if (nobits >= 9 && nobits <= 14)
      sprintf(mascaraAda,"255.255.255.%d",findesubred);
  }
  //Verificamos si la IP es del tipo C
  if ((Identificado_IP>=192) && (Identificado_IP<=223))
  {
    if (nobits >= 1 && nobits <= 8)
      sprintf(mascaraAda,"255.255.255.%d",findesubred);
  }
  return mascaraAda;
}

void HostB()
{
  int octeto2,octeto3;
  int redesSolicitadas,bitsdeRed,noSubRedes,noHost,bitsHost,incrementoSubred,findesubred=0,flag=0,flag1=0;
  int binarios[]={128,64,32,16,8,4,2,1,128,64,32,16,8,4,2,1};
  FILE *fp=fopen( "Hosts.txt", "w+" );
  FILE *fp1=fopen("Busqueda Subred.txt","w+");
  
  do
  {
    printf("Ingresa el número de hosts que desea(Minimo:4 Maximo:16384): ");
    scanf("%d",&noHost);
    if(noHost >= 4 && noHost <= 16384)
      flag1=1;
    else
    {
      printf("ERROR: Número de hosts no válido\n");
      flag1=0;
    }
  }while(flag1 != 1);
  //Calculamos los bits de host
  bitsHost=ceil(log(noHost)/log(2));
  //Calculamos los host totales
  noHost=pow(2,bitsHost);
  Host=noHost;
  //Calculamos el número de bits para la mascara de red adaptada
  bitsdeRed=16-bitsHost;
  bits=bitsdeRed;
  //Caclculamos el nuḿero de subredes
  noSubRedes=pow(2,bitsdeRed);
  //Buscamos la mascara adptada y el final de subred
  int i=bitsdeRed-1;
  incrementoSubred=binarios[bitsdeRed-1];
  incrementarSubred=incrementoSubred;
  while (!flag)
  {
    //printf("%d\n", binarios[i]);
    findesubred+=binarios[i];
    if (binarios[i]==128)
      flag=1;
    i--;
  }
  
  //Masacara adaptada//
  mascaraAdaptada=AdaptarMascara(bitsdeRed,findesubred);
  printf("\n-----CALCULO POR HOST-----\n\n");
  printf("Número de Subredes:%d\n",noSubRedes);
  printf("Número de Host:%d\n",noHost);
  printf("Máscara de Subred:%s\n\n", mascaraAdaptada);

  int id=1;
  if(bitsdeRed<=8)
  {
    for (octeto2=0;octeto2<=findesubred;octeto2+=incrementoSubred)
    {
      printf("| %d | %d.%d.%d.0 |\n",id,Identificado_IP,Oct1,octeto2);
      fprintf(fp, "| %d | %d.%d.%d.0 |\n",id,Identificado_IP,Oct1,octeto2);
      fprintf(fp1, "| %d | %d.%d.%d.0 |\n",id,Identificado_IP,Oct1,octeto2);
      id++;
    }
  }
  if(bitsdeRed>=9 && bitsdeRed<=16)
  {
    for (octeto2=0; octeto2<=255; octeto2++)
    {
      for (octeto3=0; octeto3<=findesubred; octeto3+=incrementoSubred)
      {
        printf("| %d | %d.%d.%d.%d |\n",id,Identificado_IP,Oct1,octeto2,octeto3);
        fprintf(fp, "| %d | %d.%d.%d.%d |\n",id,Identificado_IP,Oct1,octeto2, octeto3);
        fprintf(fp1, "| %d | %d.%d.%d.%d |\n",id,Identificado_IP,Oct1,octeto2, octeto3);
        id++;
      }
    }

  }
  printf("\nPresiona una tecla para continuar...\n");
  getchar();
  getchar();
  fclose(fp);
  fclose(fp1);
}

void HostC()
{
  int redesSolicitadas,bitsdeRed,noSubRedes,noHost,bitsHost,incrementoSubred,findesubred=0,flag=0,flag1=0;
  int octeto3;
  int binarios[]={128,64,32,16,8,4,2,1};
  FILE *fp=fopen( "Hosts.txt", "w+" );
  FILE *fp1=fopen("Busqueda Subred.txt","w+");

  do
  {
    printf("Ingresa el número de hosts que desea(Minimo:4 máximo:64): ");
    scanf("%d",&noHost);
    if(noHost >= 4 && noHost <= 64)
      flag1=1;
    else
    {
      printf("ERROR: Número de hosts no válido\n");
      flag1=0;
    }
  }while(flag1 != 1);
  //Calculamos los bits de host
  bitsHost=ceil(log(noHost)/log(2));
  //Calculamos los host totales
  noHost=pow(2,bitsHost);
  Host=noHost;
  //Calculamos el número de bits para la mascara de red adaptada
  bitsdeRed=8-bitsHost;
  bits=bitsdeRed;
  //Caclculamos el nuḿero de subredes
  noSubRedes=pow(2,bitsdeRed);
  //Buscamos la mascara adptada y el final de subred
  int i=bitsdeRed-1;
  incrementoSubred=binarios[bitsdeRed-1];
  incrementarSubred=incrementoSubred;
  while (!flag)
  {
    //printf("%d\n", binarios[i]);
    findesubred+=binarios[i];
    if (binarios[i]==128)
      flag=1;
    i--;
  }

  //Masacara adaptada//
  mascaraAdaptada=AdaptarMascara(bitsdeRed,findesubred);
  printf("\n-----CALCULO POR HOST-----\n\n");
  printf("Número de Subredes: %d\n",noSubRedes);
  printf("Número de Host: %d\n",noHost);
  printf("Máscara de Subred: %s\n\n", mascaraAdaptada);

  int id=1;
  if(bitsdeRed<=6)
  {
    for (octeto3=0;octeto3<=findesubred;octeto3+=incrementoSubred)
    {
      printf("| %d | %d.%d.%d.%d |\n",id,Identificado_IP,Oct1,Oct2,octeto3);
      fprintf(fp, "| %d | %d.%d.%d.%d |\n",id,Identificado_IP,Oct1,Oct2, octeto3);
      fprintf(fp1, "| %d | %d.%d.%d.%d |\n",id,Identificado_IP,Oct1,Oct2, octeto3);
      id++;
    }
  }
  printf("\nPresiona una tecla para continuar...\n");
  getchar();
  getchar();
  fclose(fp);
  fclose(fp1);
}

void CalcularSubredes()
{
  if (Identificado_IP<=127)
  {
    subredesA();
  }
  if (Identificado_IP >= 128 && Identificado_IP <= 191)
  {
    subredesB();
  }
  if (Identificado_IP>=192 && Identificado_IP<=223)
  {
    subredesC();
  }
}

/*Función que realiza el calculo de las subredes en la IP, usando funciones para cada una de las clases de las IPs*/
//IP tipo 19.0.0.0/8 de 2 a 64 subredes
void subredesA()
{
  int octeto1,octeto2,octeto3;
  int redesSolicitadas,bitsdeRed,noSubRedes,noHost,bitsHost,incrementoSubred,findesubred=0,flag=0,flag1=0;
  int binarios[]={128,64,32,16,8,4,2,1,128,64,32,16,8,4,2,1,128,64,32,16,8,4,2,1};
  FILE *fp=fopen( "Subredes.txt", "w+" );
  FILE *fp1=fopen("Busqueda Subred.txt","w+");

  do
  {
    printf("Ingresa el número de subredes que desea(Minimo:4 Maximo:4194304): ");
    scanf("%d",&redesSolicitadas);
    if(redesSolicitadas >= 4 && redesSolicitadas <= 16777216)
      flag1=1;
    else
    {
      printf("ERROR: Número de subredes no válido\n");
      flag1=0;
    }
  }while(flag1 != 1);
  //Calculamos el número de bits para la mascara de red adaptada
  bitsdeRed=ceil(log(redesSolicitadas)/log(2));
  bits=bitsdeRed;
  //Caclculamos el nuḿero real de subredes
  noSubRedes=pow(2,bitsdeRed);
  //Calculamos los bits de host
  bitsHost=24-bitsdeRed;
  //Calculamos los host totales
  noHost=pow(2,bitsHost);
  Host=noHost;
  //Buscamos la mascara adptada y el final de subred
  int i=bitsdeRed-1;
  incrementoSubred=binarios[bitsdeRed-1];
  incrementarSubred=incrementoSubred;
  while (!flag)
  {
    findesubred+=binarios[i];
    if (binarios[i]==128)
      flag=1;
    i--;
  }
   
  //Masacara adaptada//
  mascaraAdaptada=AdaptarMascara(bitsdeRed,findesubred);
  printf("\n-----CALCULO POR SUBRED-----\n\n");
  printf("Número de Subredes: %d\n",noSubRedes);
  printf("Número de Host: %d\n",noHost);
  printf("Máscara de Subred: %s\n\n", mascaraAdaptada);
  
  int id=1;
  if(bitsdeRed<=8)
  {
    for (octeto1=0;octeto1<=findesubred;octeto1+=incrementoSubred)
    {
      printf("| %d | %d.%d.0.0 |\n",id,Identificado_IP,octeto1);
      fprintf(fp, "| %d | %d.%d.0.0 |\n",id,Identificado_IP, octeto1);
      fprintf(fp1, "| %d | %d.%d.0.0 |\n",id,Identificado_IP, octeto1);
      id++;
    }
  }
  if (bitsdeRed>=9 && bitsdeRed <= 16)
  {
    for (octeto2=0;octeto2<=255;octeto2++)
    {
      for (octeto1=0;octeto1<=findesubred;octeto1+=incrementoSubred)
      {
        printf("| %d | %d.%d.%d.0 |\n",id,Identificado_IP,octeto2,octeto1 );
        fprintf(fp, "| %d | %d.%d.%d.0 |\n",id,Identificado_IP, octeto2, octeto1);
        fprintf(fp1, "| %d | %d.%d.%d.0 |\n",id,Identificado_IP, octeto2, octeto1);
        id++;
      }
    }
  }
  if (bitsdeRed>=17 && bitsdeRed<=24)
  {
    for (octeto3=0; octeto3<=255;octeto3++)
    {
      for (octeto2=0; octeto2<=255; octeto2++)
      {
        for (octeto1 = 0; octeto1 <= findesubred; octeto1+=incrementoSubred)
        {
          printf("| %d | %d.%d.%d.%d |\n",id,Identificado_IP,octeto3,octeto2,octeto1);
          fprintf(fp, "| %d | %d.%d.%d.%d |\n",id, Identificado_IP, octeto3, octeto2, octeto1);
          fprintf(fp1, "| %d | %d.%d.%d.%d |\n",id, Identificado_IP,octeto3, octeto2, octeto1);
          id++;
        }
      }
    }
  }
;
  printf("\nPresiona una tecla para continuar...\n");
  getchar();
  getchar();
  fclose(fp);
  fclose(fp1);
}
///Subneteo Subredes clase:B tipo 123.123.0.0
void subredesB()
{
  int octeto2,octeto3;
  int redesSolicitadas,bitsdeRed,noSubRedes,noHost,bitsHost,incrementoSubred,findesubred=0,flag=0,flag1=0;
  int binarios[]={128,64,32,16,8,4,2,1,128,64,32,16,8,4,2,1};
  FILE *fp=fopen( "Subredes.txt", "w+" );
  FILE *fp1=fopen("Busqueda Subred.txt","w+");
 
  do
  {
    printf("Ingresa el número de subredes que desea(Minimo:4 Maximo:16384): ");
    scanf("%d",&redesSolicitadas);
    if(redesSolicitadas >= 4 && redesSolicitadas <= 16384)
      flag1=1;
    else
    {
      printf("ERROR: Número de subredes no válido\n");
      flag1=0;
    }
  }while(flag1 != 1);
  //Calculamos el número de bits para la mascara de red adaptada
  bitsdeRed=ceil(log(redesSolicitadas)/log(2));
  bits=bitsdeRed;
  //Caclculamos el nuḿero real de subredes
  noSubRedes=pow(2,bitsdeRed);
  //Calculamos los bits de host
  bitsHost=16-bitsdeRed;
  //Calculamos los host totales
  noHost=pow(2,bitsHost);
  Host=noHost;
  //Buscamos la mascara adptada y el final de subred
  int i=bitsdeRed-1;
  incrementoSubred=binarios[bitsdeRed-1];
  incrementarSubred=incrementoSubred;
  while (!flag)
  {
    //printf("%d\n", binarios[i]);
    findesubred+=binarios[i];
    if (binarios[i]==128)
      flag=1;
    i--;
  }
  
  //Masacara adaptada//
  mascaraAdaptada=AdaptarMascara(bitsdeRed,findesubred);
  printf("\n-----CALCULO POR SUBRED-----\n\n");
  printf("Número de Subredes: %d\n",noSubRedes);
  printf("Número de Host: %d\n",noHost);
  printf("Máscara de Subred: %s\n\n", mascaraAdaptada);

  int id=1;
  if(bitsdeRed<=8)
  {
    for (octeto2=0;octeto2<=findesubred;octeto2+=incrementoSubred)
    {
      printf("| %d | %d.%d.%d.0 |\n",id,Identificado_IP,Oct1,octeto2);
      fprintf(fp, "| %d | %d.%d.%d.0 |\n",id,Identificado_IP,Oct1,octeto2);
      fprintf(fp1, "| %d | %d.%d.%d.0 |\n",id,Identificado_IP,Oct1,octeto2);
      id++;
    }
  }
  if(bitsdeRed>=9 && bitsdeRed<=16)
  {
    for (octeto2=0; octeto2<=255; octeto2++)
    {
      for (octeto3=0; octeto3<=findesubred; octeto3+=incrementoSubred)
      {
        printf("| %d | %d.%d.%d.%d |\n",id,Identificado_IP,Oct1,octeto2,octeto3);
        fprintf(fp, "| %d | %d.%d.%d.%d |\n",id,Identificado_IP,Oct1,octeto2, octeto3);
        fprintf(fp1, "| %d | %d.%d.%d.%d |\n",id,Identificado_IP,Oct1,octeto2, octeto3);
        id++;
      }
    }

  }

  printf("\nPresiona una tecla para continuar...\n");
  getchar();
  getchar();
  fclose(fp);
  fclose(fp1);
}
//Subneteo por subredes clase:C tipo 123.123.123.0
void subredesC()
{
  int redesSolicitadas,bitsdeRed,noSubRedes,noHost,bitsHost,incrementoSubred,findesubred=0,flag=0,flag1=0;
  int octeto3;
  int binarios[]={128,64,32,16,8,4,2,1};
  FILE *fp=fopen( "Subredes.txt", "w+" );
  FILE *fp1=fopen("Busqueda Subred.txt","w+");
  
  do
  {
    printf("Ingresa el número de subredes que desea(Minimo:4 Maximo:64): ");
    scanf("%d",&redesSolicitadas);
    if(redesSolicitadas >= 4 && redesSolicitadas <= 64)
      flag1=1;
    else
    {
      printf("ERROR: Número de subredes no válido\n");
      flag1=0;
    }
  }while(flag1 != 1);
  //Calculamos el número de bits para la mascara de red adaptada
  bitsdeRed=ceil(log(redesSolicitadas)/log(2));
  bits=bitsdeRed;
  //Caclculamos el nuḿero real de subredes
  noSubRedes=pow(2,bitsdeRed);
  //Calculamos los bits de host
  bitsHost=8-bitsdeRed;
  //Calculamos los host totales
  noHost=pow(2,bitsHost);
  Host=noHost;
  //Buscamos la mascara adptada y el final de subred
  int i=bitsdeRed-1;
  incrementoSubred=binarios[bitsdeRed-1];
  incrementarSubred=incrementoSubred;
  while (!flag)
  {
    //printf("%d\n", binarios[i]);
    findesubred+=binarios[i];
    if (binarios[i]==128)
      flag=1;
    i--;
  }
  
  //Masacara adaptada//
  mascaraAdaptada=AdaptarMascara(bitsdeRed,findesubred);
  printf("\n-----CALCULO POR SUBRED-----\n\n");
  printf("Número de Subredes: %d\n",noSubRedes);
  printf("Número de Host: %d\n",noHost);
  printf("Máscara de Subred: %s\n\n", mascaraAdaptada);

  int id=1;
  if(bitsdeRed<=6)
  {
    for (octeto3=0;octeto3<=findesubred;octeto3+=incrementoSubred)
    {
      printf("| %d | %d.%d.%d.%d |\n",id,Identificado_IP,Oct1,Oct2,octeto3);
      fprintf(fp, "| %d | %d.%d.%d.%d |\n",id,Identificado_IP,Oct1, Oct2, octeto3);
      fprintf(fp1, "| %d | %d.%d.%d.%d |\n",id,Identificado_IP,Oct1, Oct2, octeto3);
      id++;
    }
  }
  printf("\nPresiona una tecla para continuar...\n");
  getchar();
  getchar();
  fclose(fp);
  fclose(fp1);
}

void CalcularPrefijo()
{
  if (Identificado_IP<=127)
  {
    PrefijoA();
  }
  if (Identificado_IP >= 128 && Identificado_IP <= 191)
  {
    PrefijoB();
  }
  if (Identificado_IP>=192 && Identificado_IP<=223)
  {
    PrefijoC();
  }
}

void PrefijoA()
{
  int octeto1,octeto2,octeto3;
  int prefijo,redesSolicitadas,bitsdeRed,noSubRedes,noHost,bitsHost,incrementoSubred,findesubred=0,flag=0,flag1=0;
  int binarios[]={128,64,32,16,8,4,2,1,128,64,32,16,8,4,2,1,128,64,32,16,8,4,2,1};
  FILE *fp=fopen( "Prefijos.txt", "w+" );
  FILE *fp1=fopen("Busqueda Subred.txt","w+");

  do
  {
    printf("Ingrese el prefijo deseado para la IP:");
    scanf("%d",&prefijo);
    ///Se limita el prefijo a que sea mayor a 8 ya que si es menor a esta cantidad se estaría utilizando los bits reservados
    if(prefijo>8 && prefijo<=32)
      flag1=1;
    else
    {
      printf("ERROR: Prefijo no válido\n");
      flag1=0;
    }
  }while(flag1 != 1);
  //Calculamos el número de bits para la mascara de red adaptada
  bitsdeRed=prefijo-8;
  bits=bitsdeRed;
  //Caclculamos el nuḿero real de subredes
  noSubRedes=pow(2,bitsdeRed);
  //Calculamos los bits de host
  bitsHost=24-bitsdeRed;
  //Calculamos los host totales
  noHost=pow(2,bitsHost);
  Host=noHost;
  //Buscamos la mascara adptada y el final de subred
  int i=bitsdeRed-1;
  incrementoSubred=binarios[bitsdeRed-1];
  incrementarSubred=incrementoSubred;
  while (!flag)
  {
    findesubred+=binarios[i];
    if (binarios[i]==128)
      flag=1;
    i--;
  }
 
  //Masacara adaptada//
  mascaraAdaptada=AdaptarMascara(bitsdeRed,findesubred);
  printf("\n-----CALCULO POR PREFIJO-----\n\n");
  printf("Número de Subredes: %d\n",noSubRedes);
  printf("Número de Host: %d\n",noHost);
  printf("Máscara de Subred: %s\n\n", mascaraAdaptada);
  
  int id=1;
  if(bitsdeRed<=8)
  {
    for (octeto1=0;octeto1<=findesubred;octeto1+=incrementoSubred)
    {
      printf("| %d | %d.%d.0.0 |\n",id,Identificado_IP,octeto1);
      fprintf(fp, "| %d | %d.%d.0.0 |\n",id,Identificado_IP,octeto1);
      fprintf(fp1, "| %d | %d.%d.0.0 |\n",id,Identificado_IP,octeto1);
      id++;
    }
  }
  if (bitsdeRed>=9 && bitsdeRed <= 16)
  {
    for (octeto2=0;octeto2<=255;octeto2++)
    {
      for (octeto1=0;octeto1<=findesubred;octeto1+=incrementoSubred)
      {
        printf("| %d | %d.%d.%d.0 |\n",id,Identificado_IP,octeto2,octeto1 );
        fprintf(fp, "| %d | %d.%d.%d.0 |\n",id,Identificado_IP,octeto2,octeto1);
        fprintf(fp1, "| %d | %d.%d.%d.0 |\n",id,Identificado_IP,octeto2,octeto1);
        id++;
      }
    }
  }
  if (bitsdeRed>=17 && bitsdeRed<=24)
  {
    for (octeto3=0; octeto3<=255;octeto3++)
    {
      for (octeto2=0; octeto2<=255; octeto2++)
      {
        for (octeto1 = 0; octeto1 <= findesubred; octeto1+=incrementoSubred)
        {
          printf("| %d | %d.%d.%d.%d |\n",id,Identificado_IP,octeto3,octeto2,octeto1);
          fprintf(fp, "| %d | %d.%d.%d.%d |\n",id,Identificado_IP,octeto3,octeto2,octeto1);
          fprintf(fp1, "| %d | %d.%d.%d.%d |\n",id,Identificado_IP,octeto3,octeto2,octeto1);
          id++;
        }
      }
    }
  }
  printf("\nPresiona una tecla para continuar...\n");
  getchar();
  getchar();
  fclose(fp);
  fclose(fp1);
}
//Subneteo Ip clase B dado cierto prefijo
void PrefijoB()
{
  int octeto2,octeto3;
  int prefijo,redesSolicitadas,bitsdeRed,noSubRedes,noHost,bitsHost,incrementoSubred,findesubred=0,flag=0,flag1=0;
  int binarios[]={128,64,32,16,8,4,2,1,128,64,32,16,8,4,2,1};
  FILE *fp=fopen( "Prefijos.txt", "w+" );
  FILE *fp1=fopen("Busqueda Subnet.txt","w+");

  do
  {
    printf("Ingrese el prefijo deseado para la IP: ");
    scanf("%d",&prefijo);
    ///Se limita el prefijo a que sea mayor a 8 ya que si es menor a esta cantidad se estaría utilizando los bits reservados
    if(prefijo>16 && prefijo<=32)
      flag1=1;
    else
    {
      printf("ERROR: Prefijo no válido\n");
      flag1=0;
    }
  }while(flag1 != 1);
  //Calculamos el número de bits para la mascara de red adaptada
  bitsdeRed=prefijo-16;
  bits=bitsdeRed;
  //Caclculamos el nuḿero real de subredes
  noSubRedes=pow(2,bitsdeRed);
  //Calculamos los bits de host
  bitsHost=16-bitsdeRed;
  //Calculamos los host totales
  noHost=pow(2,bitsHost);
  Host=noHost;
  //Buscamos la mascara adptada y el final de subred
  int i=bitsdeRed-1;
  incrementoSubred=binarios[bitsdeRed-1];
  incrementarSubred=incrementoSubred;
  while (!flag)
  {
    //printf("%d\n", binarios[i]);
    findesubred+=binarios[i];
    if (binarios[i]==128)
      flag=1;
    i--;
  }
 
  //Masacara adaptada//
  mascaraAdaptada=AdaptarMascara(bitsdeRed,findesubred);
  printf("\n-----CALCULO POR PREFIJO-----\n\n");
  printf("Número de Subredes: %d\n",noSubRedes);
  printf("Número de Host: %d\n",noHost);
  printf("Máscara de Subred: %s\n\n", mascaraAdaptada);

  int id=1;
  if(bitsdeRed<=8)
  {
    for (octeto2=0;octeto2<=findesubred;octeto2+=incrementoSubred)
    {
      printf("| %d | %d.%d.%d.0 |\n",id,Identificado_IP,Oct1,octeto2);
      fprintf(fp, "| %d | %d.%d.%d.0 |\n",id,Identificado_IP,Oct1,octeto2);
      fprintf(fp1, "| %d | %d.%d.%d.0 |\n",id,Identificado_IP,Oct1,octeto2);
      id++;
    }
  }
  if(bitsdeRed>=9 && bitsdeRed<=16)
  {
    for (octeto2=0; octeto2<=255; octeto2++)
    {
      for (octeto3=0; octeto3<=findesubred; octeto3+=incrementoSubred)
      {
        printf("| %d | %d.%d.%d.%d |\n",id,Identificado_IP,Oct1,octeto2,octeto3);
        fprintf(fp, "| %d | %d.%d.%d.%d |\n",id,Identificado_IP,Oct1,octeto2,octeto3);
        fprintf(fp1, "| %d | %d.%d.%d.%d |\n",id,Identificado_IP,Oct1,octeto2,octeto3);
        id++;
      }
    }
  }

  printf("\nPresiona una tecla para continuar...\n");
  getchar();
  getchar();
  fclose(fp);
  fclose(fp1);
}

void PrefijoC()
{
  int prefijo,redesSolicitadas,bitsdeRed,noSubRedes,noHost,bitsHost,incrementoSubred,findesubred=0,flag=0,flag1=0;
  int octeto3;
  int binarios[]={128,64,32,16,8,4,2,1};
  FILE *fp=fopen( "Prefijos.txt", "w+" );
  FILE *fp1=fopen("Busqueda Subred.txt","w+");

  do
  {
    printf("Ingrese el prefijo deseado para la IP: ");
    scanf("%d",&prefijo);
    //Se limita el prefijo a que sea mayor a 8 ya que si es menor a esta cantidad se estaría utilizando los bits reservados
    if(prefijo>24 && prefijo<=32)
      flag1=1;
    else
    {
      printf("ERROR: Prefijo no válido\n");
      flag1=0;
    }
  }while(flag1 != 1);
  //Calculamos el número de bits para la mascara de red adaptada
  bitsdeRed=prefijo-24;
  bits=bitsdeRed;
  //Caclculamos el nuḿero real de subredes
  noSubRedes=pow(2,bitsdeRed);
  //Calculamos los bits de host
  bitsHost=8-bitsdeRed;
  //Calculamos los host totales
  noHost=pow(2,bitsHost);
  Host=noHost;
  //Buscamos la mascara adptada y el final de subred
  int i=bitsdeRed-1;
  incrementoSubred=binarios[bitsdeRed-1];
  incrementarSubred=incrementoSubred;
  while (!flag)
  {
    //printf("%d\n", binarios[i]);
    findesubred+=binarios[i];
    if (binarios[i]==128)
      flag=1;
    i--;
  }
 
  //Masacara adaptada//
  mascaraAdaptada=AdaptarMascara(bitsdeRed,findesubred);
  printf("\n-----CALCULO POR PREFIJO-----\n\n");
  printf("Número de Subredes: %d\n",noSubRedes);
  printf("Número de Host: %d\n",noHost);
  printf("Máscara de Subred: %s\n\n", mascaraAdaptada);
  
  int id=1;
  if(bitsdeRed<=8)
  {
    for (octeto3=0;octeto3<=findesubred;octeto3+=incrementoSubred)
    {
      printf("| %d | %d.%d.%d.%d |\n",id,Identificado_IP,Oct1,Oct2,octeto3);
      fprintf(fp, "| %d | %d.%d.%d.%d |\n",id,Identificado_IP,Oct1,Oct2,octeto3);
      fprintf(fp1, "| %d | %d.%d.%d.%d |\n",id,Identificado_IP,Oct1,Oct2,octeto3);
      id++;
    }
  }

  printf("\nPresiona una tecla para continuar...\n");
  getchar();
  getchar();
  fclose(fp);
  fclose(fp1);
}

/*Funcion que realiza la busqueda de una subred especifica*/
void MostrarSubred()
{
  FILE *fp=fopen("Busqueda Subred.txt","r");
  int flag,id,idaux/*,opc*/;
  char /*IPdesubredAUX,*/*IPdesubred;

  printf("\n-----BUSQUEDA DE SUBREDES-----\n\n");
  /*printf("1.Busqueda por IP\n");
  printf("2.busqueda por número de subred\n"); 
  printf("Ingrese el numero de la opcion: ");
  scanf("%d",&opc);

  IPdesubredAUX=(char*)malloc(15);*/
  IPdesubred=(char*)malloc(15);

  /*if (opc == 1)
  {
    printf("Ingrese la IP a buscar: ");
    scanf("%s",IPdesubredAUX);
  }
  else
  {*/
    printf("Ingrese el número de la subred de la cual desea buscar los hosts: ");
    scanf("%d",&id);
  /*}*/

  while(!feof(fp))
  {
    flag=1;
    fscanf(fp,"| %d | %s |\n",&idaux,IPdesubred);
    if (id==idaux/* || !strcmp(IPdesubred,IPdesubredAUX)*/)
      break;
    flag=0;
  }

  if(flag)
    MuestraSubred(IPdesubred,bits,Host);
  else
  {
    printf("ERROR: Subred no encontrada.\n");
    printf("\nPresiona una tecla para continuar...\n");
    getchar();
    getchar();
  } 

  fclose(fp);
}

void MuestraSubred(char *IPsubred, int bits, int noHost)
{
  int Identificado_IP,oct1,oct2,oct3;
  sscanf(IPsubred,"%d.%d.%d.%d",&Identificado_IP,&oct1,&oct2,&oct3);

  if (Identificado_IP<=127)
    DesplegarHostA(Identificado_IP,oct1,oct2,oct3,bits,incrementarSubred);
  if (Identificado_IP>=128 && Identificado_IP<=191)
    DesplegarHostB(Identificado_IP,oct1,oct2,oct3,bits,incrementarSubred);
  if (Identificado_IP>=192 && Identificado_IP<=223)
    DesplegarHostC(Identificado_IP,oct1,oct2,oct3,noHost);
}
void DesplegarHostA(int Identificado_IP,int oct1,int oct2,int oct3,int bits,int incrementarSubred)
{
  int id=1;
  FILE *fp=fopen("Resultados Busqueda Subredes.txt","w+");
  //caso menor o igual a 8 bits de red
  if (bits<=8)
  {
      for (int i=oct1;i<oct1+incrementarSubred;i++)
      {
        for (oct2=0; oct2<=255 ;oct2++)
        {
          for (oct3=0; oct3<=255 ;oct3++)
          {
            printf("| %d | %d.%d.%d.%d |\n",id, Identificado_IP,i,oct2,oct3);
            fprintf(fp,"| %d | %d.%d.%d.%d |\n",id, Identificado_IP,i,oct2,oct3);
            id++;
          }
        }
      }
  }
  if (bits>=9 && bits<=16)
  {
    for (int i=oct2; i<oct2+incrementarSubred; i++)
    {
      for (oct3=0;oct3<=255;oct3++)
      {
        printf("| %d | %d.%d.%d.%d |\n", id,Identificado_IP,oct1,i,oct3);
        fprintf(fp,"| %d | %d.%d.%d.%d |\n", id,Identificado_IP,oct1,i,oct3);
        id++;
      }
    }
  }
  if (bits>=17 && bits<=24)
  {
    for (int i=oct3; i<oct3+incrementarSubred; i++)
    {
      printf("| %d | %d.%d.%d.%d |\n", id,Identificado_IP,oct1,oct2,i);
      fprintf(fp,"| %d | %d.%d.%d.%d |\n", id,Identificado_IP,oct1,oct2,i);
      id++;
    }
  }

  printf("\nPresiona una tecla para continuar...\n");
  getchar();
  getchar();
  fclose(fp);
}

void DesplegarHostB(int Identificado_IP,int oct1,int oct2,int oct3,int bits,int incrementarSubred)
{
  int id=1;
  FILE *fp=fopen("Resultados Busqueda Subredes.txt","w+");
  printf("%d,%d\n", bits,incrementarSubred);

  if (bits<=8)
  {
    for (int i=oct2; i<oct2+incrementarSubred; i++)
    {
      for (oct3=0;oct3<=255;oct3++)
      {
        printf("| %d | %d.%d.%d.%d |\n", id,Identificado_IP,oct1,i,oct3);
        fprintf(fp,"| %d | %d.%d.%d.%d |\n", id,Identificado_IP,oct1,i,oct3);
        id++;
      }
    }
  }
  if (bits>=9 && bits<=14)
  {
  	for (int i=oct3; i<oct3+incrementarSubred; i++)
  	{
      printf("| %d | %d.%d.%d.%d |\n", id,Identificado_IP,oct1,oct2,i);
    	fprintf(fp,"| %d | %d.%d.%d.%d |\n", id,Identificado_IP,oct1,oct2,i);
    	id++;
  	}
  }

  printf("\nPresiona una tecla para continuar...\n");
  getchar();
  getchar();
  fclose(fp);
}

void DesplegarHostC(int Identificado_IP,int oct1,int oct2,int oct3,int host)
{
  int id=1,i=0;
  FILE *fp=fopen("Resultados Busqueda Subredes.txt","w+");
  printf("IP: %d.%d.%d.%d\n",Identificado_IP,oct1,oct2,oct3);
  printf("Host: %d\n",host);

  while(i<host)
  {
    printf("| %d | %d.%d.%d.%d |\n", id,Identificado_IP,oct1,oct2,i);
    fprintf(fp,"| %d | %d.%d.%d.%d |\n", id,Identificado_IP,oct1,oct2,i);
    id++;
    i++;
  }

  printf("\nPresiona una tecla para continuar...\n");
  getchar();
  getchar();
  fclose(fp);
}