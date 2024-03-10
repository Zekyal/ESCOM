//Simulación 3
//EQUIPO: SALCHIPAPAS
//FECHA DE ENTREGA: 4/Abril/2018
#include <stdio.h>
#include <windows.h>
#include <stdlib.h>
#include <conio.h>
#include "TADColaLista.h" 
/*TADColaDin.c puede ser sustituido por ‘TADColaEst.c’, o ‘TADColaCirc.c’ con la desventaja evidente de que, 
llegado el número tope de los elementos soportados por el arreglo estático, éste se desbordará.*/
#define TIEMPO_BASE 10 //Define el tiempo base, que son 10 ms
//VARIABLE GLOBAL inicio de tipo char[][], la cual permite manejar los datos gráficos de la función DibujarVentanillas();
char inicio[50][100] =
{
"  B         B         B         B         B         B         B         B         B         B  ",
"AAAAA     AAAAA     AAAAA     AAAAA     AAAAA     AAAAA     AAAAA     AAAAA     AAAAA     AAAAA",
"A   A     A   A     A   A     A   A     A   A     A   A     A   A     A   A     A   A     A   A",
"AAAAA     AAAAA     AAAAA     AAAAA     AAAAA     AAAAA     AAAAA     AAAAA     AAAAA     AAAAA",
"AAAAA     AAAAA     AAAAA     AAAAA     AAAAA     AAAAA     AAAAA     AAAAA     AAAAA     AAAAA",
};
//DECLARACIÓN DE FUNCIONES:
void DibujarVentanillas(int); //Prototipo de función que dibujará las ventanillas disponibles
void DibujarMarco(); //Prototipo de función para dibujar el marco del título.
void AtenderClientes(int,int,int,int,int);
void gotoxy(int,int);//Prototipo de función que ayuda a manejar el cursor
//FUNCIÓN PRINCIPAL:
int main()
{
  int cant_cajas,tiempo_cajeros,tiempo_clientes,tiempo_usuarios,tiempo_preferentes;
  printf("CANTIDAD DE CAJAS ABIERTAS: ");
  scanf("%i",&cant_cajas);
  printf("\nTIEMPO DE ATENCION DE LOS CAJEROS: ");
  scanf("%i",&tiempo_cajeros);
  printf("\nTIEMPO DE LLEGADA DE LOS CLIENTES: ");
  scanf("%i",&tiempo_clientes);
  printf("\nTIEMPO DE LLEGADA DE LOS USUARIOS: ");
  scanf("%i",&tiempo_usuarios);
  printf("\nTIEMPO DE LLEGADA DE LOS PREFERENTES: ");
  scanf("%i",&tiempo_preferentes);
  system("cls");
  DibujarMarco();
  gotoxy(40,2); printf("BANCO ESCOM UwU");
  DibujarVentanillas(cant_cajas);
  AtenderClientes(cant_cajas,tiempo_cajeros,tiempo_clientes,tiempo_usuarios,tiempo_preferentes);
  return 0;
}
/*
FUNCIÓN: gotoxy();
RECIBE: Dos enteros como coordenadas del plano dentro del CMD.
DEVUELVE: Dentro del CMD, una posición específica del cursor en (x,y).
*/
void gotoxy(int x, int y)
{
	HANDLE Id;
	COORD Posicion;
	Posicion.X= x;
	Posicion.Y= y;
	Id= GetStdHandle(STD_OUTPUT_HANDLE);
	SetConsoleCursorPosition(Id,Posicion);
}
/*
FUNCIÓN: DibujarVentanillas();
RECIBE: Variable 'a', que es el número de cajas abiertas.
DEVUELVE: Cajas dibujadas en el CMD.
*/
void DibujarVentanillas(int a)
{
  int i,j,k=0,s;
  //La variable 's' es empleada para el control del for, para imprimir sólo las cajas necesarias.
  s=a*10;
  for(i=0;i<5;i++)
  {
    for(j=0;j<s;j++)
    {
      if(inicio[i][j]=='A')
      {
          gotoxy(j+5,i+5); printf("*");
      }
      if(inicio[i][j]=='B')
      {
        k++;
        gotoxy(j+5,i+5); printf("%i",k);
      }
    }
  }
}
/*
FUNCIÓN: AtenderClientes();
RECIBE: tiempo de atención de los cajeros, tiempo de llegada de clientes, preferentes y usuarios.
DEVUELVE: Función de cajas en el CMD
*/
void AtenderClientes(int cant_cajas,int tiempo_cajeros,int tiempo_clientes,int tiempo_usuarios,int tiempo_preferentes)
{
  int tiempo,i=1,j=1,k=1,aux_fondoC=0,aux_fondoU=0,aux_fondoP=0,control_cajas=0;
  //Letras que identificarán qué tipo de cliente del banco es para cada caso
  char id_cliente='C',id_usuario='U',id_preferente='P';
  //Números que identificarán a cada miembro de cada cola dentro del banco
  int num_c=0,num_u=0,num_p=0;
  //Control de atendidos, para manejar la prioridad de las colas (Se inicializa en -3 para poder manipular correctamente los módulos dentro de las condicionales)
  int atendidos_c=-3,atendidos_u=-3,atendidos_p=-3;
  elemento e,aux,aux_grafico;
  cola cola_usuarios,cola_clientes,cola_preferentes;
  InitializeQueue(&cola_usuarios);
  InitializeQueue(&cola_clientes);
  InitializeQueue(&cola_preferentes);

    //Ciclo Infinito
    while (1)
    {
      Sleep(TIEMPO_BASE);
      tiempo++;
      //Llega un usuario a su cola
      if(tiempo % tiempo_usuarios == 0)
      {
        num_u++;
        e.c=id_usuario;
        e.num=num_u;
        Queue(&cola_usuarios,e);
		//Encolación gráfica
        if(i<29)
        {
          gotoxy(27,(i+14)); printf("%c%i",e.c,e.num);
          i++;
        }
        else
        {
          //Incrementamos el contador de los encolados que no se ven.
          aux_fondoU++;
          gotoxy(27,43); printf("%i +",aux_fondoU);
        }
      }
      //Llega un cliente a su cola
      if(tiempo % tiempo_clientes == 0)
      {
        num_c++;
        e.c=id_cliente;
        e.num=num_c;
        Queue(&cola_clientes,e);
		//Encolación gráfica
        if(j<29)
        {
          gotoxy(37,(j+14)); printf("%c%i",e.c,e.num);
          j++;
        }
        else
        {
          //Incrementamos el contador de los encolados que no se ven.
          aux_fondoC++;
          gotoxy(37,43); printf("%i +",aux_fondoC);
        }
      }
      //Llega un preferente a su cola
      if(tiempo % tiempo_preferentes == 0)
      {
        num_p++;
        e.c=id_preferente;
        e.num=num_p;
        Queue(&cola_preferentes,e);
		//Encolación gráfica
        if(k<29)
        {
          gotoxy(47,(k+14)); printf("%c%i",e.c,e.num);
          k++;
        }
        else
        {
          //Incrementamos el contador de los encolados que no se ven.
          aux_fondoP++;
          gotoxy(47,43); printf("%i +",aux_fondoP);
        }
      }
      //Se atiende a los clientes del banco:
      if(tiempo % tiempo_cajeros == 0)
      {
         //Se recorrerá cada una de las cajas para validar que se estén usando bajo los lineamientos del banco.
          control_cajas=0;
          while((control_cajas<cant_cajas) && (!EmptyQueue(&cola_clientes) || !EmptyQueue(&cola_usuarios) || !EmptyQueue(&cola_preferentes) ))
          {
            //PARA ATENDER PREFERENTES:
            //Si no hay nadie en usuarios ni en clientes, sigue atendiendo preferentes, siempre y cuando no esté vacía.
            if((!EmptyQueue(&cola_preferentes) && (atendidos_p % 2 != 0)) || (EmptyQueue(&cola_clientes) && EmptyQueue(&cola_usuarios) && !EmptyQueue(&cola_preferentes)))
            {
              if(atendidos_p == -3)//Si es el primer preferente atendido, cambia ahora sí el valor para aumentarlo de uno en uno.
              {
                atendidos_p=0;
              }
              aux=Dequeue(&cola_preferentes);
              //Ir a la caja correspondiente y poner a aquel que se está atendiendo
              gotoxy((6+(control_cajas*10)),7); printf("   "); gotoxy((6+(control_cajas*10)),7); printf("%c%i",aux.c,aux.num);
              atendidos_p++;
              //Recorremos gráficamente a la cola de preferentes para que queden bien ordenados.
              if(k>28)
              {
                aux_fondoP--;
                gotoxy(47,43); printf("%i +",aux_fondoP);
              }
              k=1;
              while(k<=SizeQueue(&cola_preferentes))
              {
                aux_grafico=ElementQueue(&cola_preferentes,k);
                if(k<29)
                {
                    gotoxy(47,(k+14)); printf("%c%i",aux_grafico.c,aux_grafico.num);
                }
                k++;
              }
              if(k<29)
              {
                  gotoxy(47,(k+14)); printf("   ");
              }
            }
            else
            {
              //PARA ATENDER CLIENTES: Sigue atendiendo aún las otras colas estén vacías.
              if((!EmptyQueue(&cola_clientes) && (atendidos_c % 2 != 0)) ||(EmptyQueue(&cola_preferentes) && EmptyQueue(&cola_usuarios) && !EmptyQueue(&cola_clientes)))
              {
                if(atendidos_c == -3)//Si es el primer cliente atendido, cambia ahora sí el valor para aumentarlo de uno en uno.
                {
                  atendidos_c=0;
                }
                aux= Dequeue(&cola_clientes);
                gotoxy((6+(control_cajas*10)),7); printf("   "); gotoxy((6+(control_cajas*10)),7); printf("%c%i",aux.c,aux.num);
                atendidos_c++;
                //Recorremos gráficamente a la cola de clientes para que queden bien ordenados.
                if(j>28)
                {
                  aux_fondoC--;
                  gotoxy(37,43); printf("%i +",aux_fondoC);
                }
                j=1;
                while(j<=SizeQueue(&cola_clientes))
                {
                  aux_grafico=ElementQueue(&cola_clientes,j);
                  if(j<29)
                  {
                      gotoxy(37,(j+14)); printf("%c%i",aux_grafico.c,aux_grafico.num);
                  }
                  j++;
                }
                if(j<29)
                {
                    gotoxy(37,(j+14)); printf("   ");
                }
              }
              //PARA ATENDER USUARIOS:
              else
              {
                if(!EmptyQueue(&cola_usuarios))
                {
                  if(atendidos_u == -3)//Si es el primer usuario atendido, cambia ahora sí el valor para aumentarlo de uno en uno.
                  {
                    atendidos_u=0;
                  }
                  aux= Dequeue(&cola_usuarios);
                  gotoxy((6+(control_cajas*10)),7); printf("   "); gotoxy((6+(control_cajas*10)),7); printf("%c%i",aux.c,aux.num);
                  atendidos_u++;
                  //Reiniciamos los contadores de clientes y preferentes para volver a validar las políticas de atención.
                  atendidos_c=-3;
                  atendidos_p=-3;
                  //Recorremos gráficamente a la cola de usuarios para que queden bien ordenados.
                  if(i>28)
                  {
                    aux_fondoU--;
                    gotoxy(27,43); printf("%i +",aux_fondoU);
                  }
                  i=1;
                  while(i<=SizeQueue(&cola_usuarios))
                  {
                    aux_grafico=ElementQueue(&cola_usuarios,i);
                    if(i<29)
                    {
                        gotoxy(27,(i+14)); printf("%c%i",aux_grafico.c,aux_grafico.num);
                    }
                    i++;
                  }
                  if(i<29)
                  {
                      gotoxy(27,(i+14)); printf("   ");
                  }
                }
              }
            }
            control_cajas++;
          }
      }
    }

}
/*
FUNCIÓN: DibujarMarco();
Realiza el marco del nombre del banco.
*/
void DibujarMarco()
{
int i;
  //Líneas verticales
  for(i=0;i<4;i++)
  {
    gotoxy(32,i); printf("%c",186);
    gotoxy(62,i); printf("%c",186);
  }
  //Líneas Horizontales:
  for(i=32;i<=62;i++)
  {
    gotoxy(i,0); printf("%c",205);
    gotoxy(i,4); printf("%c",205);
  }
  //Esquinas:
  gotoxy(32,0); printf("%c",201);
  gotoxy(62,0); printf("%c",187);
  gotoxy(32,4); printf("%c",200);
  gotoxy(62,4); printf("%c",188);
}
