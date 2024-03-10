//OPERACIONES EN POSFIJO (IMPLEMENTACIÓN ESTÁTICA)
//EQUIPO: SALCHIPAPAS
//FECHA: 28/FEB/2018
#include "TADPilaLista.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define TAM 27 //Este es el tamaño del arreglo para los valores de las literales
#define MAX 100
int validarParentesis(char[]); //Prototipo de función que recibe la cadena de caracteres para validar los paréntesis;
pila ConvertirPostfijo(char[]);//Prototipo de función que recibe la cadena de caracteres para convertirla en una expresión postfija;
pila AsignarValores(pila *); //Prototipo de función que recibe la cadena de caracteres EN POSTFIJO y asigna valores a literales;
float RealizarOperacion(pila *);
/*
A continuación, declaramos las subrutinas que tendrá la función 'RealizarOperacion()'
para llegar a su resultado:
Cabe resaltar que 'Restar()', 'Dividir()' y 'Potenciar()' reciben la pila de RealizarOperacion para consultarla,
dado que sus operaciones poseen condicionales de cambio dado el tamaño de esta pila.
*/
float Sumar(float,float);
float Restar(float,float,pila *);
float Multiplicar(float,float);
float Dividir(float,float,pila *);
float Potenciar(float,float,pila *);
int main()
{
	float resultado_final; //Variable para guardar nuestro resultado final
	char cadena[MAX];
	pila pilaLista,pilaPostfijo,pilaAEvaluar;
	InitializeStack(&pilaLista);
	InitializeStack(&pilaPostfijo);
	InitializeStack(&pilaAEvaluar);
	elemento aux1;
	printf("Introduce una expresion infija: ");
	gets(cadena);
	if(!validarParentesis(cadena)) //Si los par�ntesis NO son correctos, mata la ejecuci�n;
	{
		printf("\n\nLa sintaxis de los parentesis NO es correcta\n");
		system("pause");
		exit(1);
	}
	pilaPostfijo=ConvertirPostfijo(cadena);
	pilaAEvaluar=AsignarValores(&pilaPostfijo);
	resultado_final=RealizarOperacion(&pilaAEvaluar);
	printf("\nEL RESULTADO ES: %.2f",resultado_final);

}
/*
Función: Validar los paréntesis de la expresión
Recibe cadena de caracteres del main, y a través de un bucle, la evalúa sacando los paréntesis y acomodándoles en una pila
Al momento de ingresar un paréntesis de apertura '(', realiza push de ese elemento, posteriormente, cada que encuentra un paréntesis
de cierre ')', realiza un pop.
SALIDA: Regresa un 0 si está aún llena (EXPRESIÓN INCORRECTA)
      : Regresa 1 si está vacía (EXPRESIÓN CORRECTA)
*/
int validarParentesis(char cadena[])
{
	int res,i,tam;
	elemento e;
	pila s;
	InitializeStack(&s);
	tam=strlen(cadena);
	for(i=0;i<tam;i++)
	{
		if (cadena[i]== '(')
		{
			e.c= '(';
			Push(&s,e);
		}
		else
		{
			if (cadena[i]== ')')
			{
				Pop(&s);
			}
		}

	}
	if(EmptyStack(&s))
	{
		res=1;
	}
	else
	{
		res=0;
	}
	return res;
}

/*
	NOMBRE: ConvertirPostfijo
	FUNCIÓN: Transforma la ecuación recibida en una expresión postfija para ser entregada a 'AsignarValores(); y después ser evaluada';
	Recibe: Cadena de caracteres ingresada por el usuario, previamente validada en uso de paréntesis
	Devuelve: Cadena de caracteres en postfijo para, posteriormente, ser evaluada;
*/
pila ConvertirPostfijo(char cadena[])
{
	int i,tamanio,operadorEntrada,operadorTop;
	/*
	Creamos 2 pilas, una para controlar los operadores y los paréntesis, así como una para almacenar la salida ("convertirPostfijo");
	El algoritmo funciona de la siguiente manera:
	Si lee una literal, la introduce dentro de la pila 'convertirPostfijo' directamente; De lo contrario, se explicará más adelante
	*/
	pila parentesisOperadores,cadenaConvertida;
	elemento e,topOperadores,auxtop,auxcambio;
	InitializeStack(&parentesisOperadores);
	InitializeStack(&cadenaConvertida);
	tamanio=strlen(cadena); //Valor tope para el iterador
	for(i=0;i<tamanio;i++)
	{
		e.c=cadena[i];
		if(e.c == '+' || e.c == '-' || e.c == '*' || e.c == '/' || e.c == '^' || e.c == '(') //Aquí sólo entran operadores y paréntesis de apertura
		{
			if(e.c == '(') //El paréntesis de apertura '(' siempre entra a la pila, no importando lo que esté en el tope
			{
				Push(&parentesisOperadores,e);
			}
			if(EmptyStack(&parentesisOperadores))//Si la pila está vacía, no importa qué operador sea, ingresa.
			{
				Push(&parentesisOperadores,e);
			}
			else //Si la pila no está vacía, tenemos que evaluar varios casos:
			{
				if(e.c == '+' || e.c == '-')
				{
					operadorEntrada=1;
				}
				if(e.c == '*' || e.c == '/')
				{
					operadorEntrada=2;
				}
				if(e.c == '^')
				{
					operadorEntrada=3;
				}
				auxtop=Top(&parentesisOperadores); //Consultamos el top de operadores para compararlo en el siguiente Switch()
				if(auxtop.c == '(')
				{
					operadorTop=0;
				}
				if(auxtop.c == '+' || auxtop.c == '-')
				{
					operadorTop=1;
				}
				if(auxtop.c == '*' || auxtop.c == '/')
				{
					operadorTop=2;
				}
				if(auxtop.c == '^')
				{
					operadorTop=3;
				}
				switch(operadorEntrada)
				{
					case 1: //Caso en el que se quiera ingresar un '+' o un '-' a la pila
						switch (operadorTop)
						{
							case 0: //En caso de que se encuentre un paréntesis de apertura '(' en el tope de la pila
								Push(&parentesisOperadores,e);
								break;
							case 1: //Caso en el que se encuentre un '+' o un '-' en el tope de la pila
								while(!EmptyStack(&parentesisOperadores) && auxtop.c != '(')
								{
									auxtop=Top(&parentesisOperadores);
									auxcambio=Pop(&parentesisOperadores);
									Push(&cadenaConvertida,auxcambio);
								}
								Push(&parentesisOperadores,e);
								break;
							case 2: //Caso en el que se encuentre un '*' o un '/' en el tope de la pila
								while(!EmptyStack(&parentesisOperadores) && auxtop.c != '(')
								{
									auxtop=Top(&parentesisOperadores);
									auxcambio=Pop(&parentesisOperadores);
									Push(&cadenaConvertida,auxcambio);
								}
								Push(&parentesisOperadores,e);
								break;
							case 3: //Caso en el que se enucentre un '^' en el tope de la pila
								while(auxtop.c !='(' && !EmptyStack(&parentesisOperadores))
								{
									auxtop=Top(&parentesisOperadores);
									auxcambio=Pop(&parentesisOperadores);
									Push(&cadenaConvertida,auxcambio);
								}
								Push(&parentesisOperadores,e);
								break;
						}
						break;
					case 2: //Caso en el que se intente ingresar un '*' o un '/' a la pila
						switch(operadorTop)
						{
							case 0: //Caso en el que se encuentre a un '(' en el tope de la pila
								Push(&parentesisOperadores,e);
								break;
							case 1: //Caso en el que se encuentre a un '+' o un '-' en el tope de la pila
								Push(&parentesisOperadores,e);
								break;
							case 2: //Caso en el que se encuentre a un '*' o un '/' en el tope de la pila
								while( auxtop.c !='(' && !EmptyStack(&parentesisOperadores))
								{
									auxtop=Top(&parentesisOperadores);
									auxcambio=Pop(&parentesisOperadores);
									Push(&cadenaConvertida,auxcambio);
								}
								Push(&parentesisOperadores,e);
								break;
							case 3: //Caso en el que se encuentre a un '^' en el tope de la pila
								while(auxtop.c !='(' && !EmptyStack(&parentesisOperadores))
								{
									auxtop=Top(&parentesisOperadores);
									auxcambio=Pop(&parentesisOperadores);
									Push(&cadenaConvertida,auxcambio);
								}
								Push(&parentesisOperadores,e);
								break;
						}
						break;
					case 3: //Caso en el que se intente ingresar un '^' a la pila
					 	if(operadorTop == 3) //Caso en el que se encuentre a un '^' en el tope de la pila
						{
							while(auxtop.c !='(' && !EmptyStack(&parentesisOperadores))
							{
								auxtop=Top(&parentesisOperadores);
								auxcambio=Pop(&parentesisOperadores);
								Push(&cadenaConvertida,auxcambio);
							}
							Push(&parentesisOperadores,e);
						}
						else //Si encuentra a cualquier otro operador en el tope, se ingresa, dada su jerarquía
						{
							Push(&parentesisOperadores,e);
						}
						break;
				}
			}
		}
		else
		{
			if(e.c == ')') //Aquí entran únicamente paréntesis de cierre
			{
				auxtop=Top(&parentesisOperadores);
				while(auxtop.c != '(' )
				{
					auxcambio=Pop(&parentesisOperadores);
					Push(&cadenaConvertida,auxcambio);
					auxtop=Top(&parentesisOperadores);
				}
				Pop(&parentesisOperadores); //Sacamos ese paréntesis de apertura de parentesisOperadores;
			}
			else //Aquí sólo entran literales
			{
				Push(&cadenaConvertida,e);
			}
		}
	}
	//Ya que terminamos de recorrer la cadena de caracteres, hacemos una última "limpieza" de la pila parentesisOperadores, para almacenar en la pila cadenaConvertida lo que haya faltado
		while(!EmptyStack(&parentesisOperadores))
		{
			auxcambio=Pop(&parentesisOperadores);
			Push(&cadenaConvertida,auxcambio);
		}
	return cadenaConvertida;
}

/*
FUNCI�N: AsignarValores
Recibe: Cadena de caracteres previamente convertida a postfijo por la funci�n ConvertirPostfijo();
Realiza: Asignaci�n de valores a las literales asignadas por el usuario
Devuleve: Una pila de los caracteres en postfijo, pero
*/
pila AsignarValores(pila *almacenarPop)
{
	float abc[TAM][2];
	int tamArreglada,i,j;
	elemento e;
	abc[TAM][1]=-1;
	tamArreglada=SizeStack(almacenarPop);
	pila pilaAsignada;
	InitializeStack(&pilaAsignada);
	elemento aux;
	while(!EmptyStack(almacenarPop))
	{
		aux=Pop(almacenarPop);
		if(aux.c!='+' || aux.c!='-' || aux.c!='*' || aux.c!='/' || aux.c!='^' ) //Aqu� entran s�lo literales
		{
			for(j=65;j<91;j++) //Recorre todas las letras en el  c�digo ascii
			{
				if(aux.c==j) //S�lo entra aqu� si la letra de la Cadena es igual a su hom�nimo en ascii
				{
					if(abc[j-65][1]!=3) //S�lo entra aqu� si la literal no ha sido asignada
					{
						printf("\nDAME EL VALOR DE LA LITERAL %c: ",j);
						scanf("%f",&abc[j-65][0]);
						abc[j-65][1]=3;
					}
					aux.num=abc[j-65][0];
				}
			}
			Push(&pilaAsignada,aux);
		}
		else //Aqu� s�lo entran operadores
		{
			Push(&pilaAsignada,aux);
		}
	}

	return pilaAsignada;
}
/*
FUNCI�N: RealizarOperaci�n()
RECIBE: Pila de caracteres y n�meros previamente convertida en una expresi�n en postfijo por la funci�n 'ConvertirPostfijo()' y
		con los valores de las literales asignadas a trav�s de la funci�n 'AsignarValores()'
DEVUELVE: El resultado FINAL de la expresi�n
*/
float RealizarOperacion(pila *pilaAsignada)
{
	float a,b; //Variables donde almacenaremos los valores de la pila manejoDatos para ser operados.
	pila manejoDatos; //Pila que almacenará tanto las variables, así como los resultados de las subrutinas.
	elemento auxA,auxB,auxtop,auxres,auxAlmacenarRes;
	InitializeStack(&manejoDatos);
	while(!EmptyStack(pilaAsignada))
	{
			auxtop=Pop(pilaAsignada);

			if(auxtop.c=='+'|| auxtop.c=='-' ||auxtop.c=='*'|| auxtop.c=='/' ||auxtop.c=='^')
				{
					//Si lo que se lee de 'pilaAsignada' es un operador, entonces sacamos dos elementos de la pila 'manejoDatos', y los operamos seg�n sea el operador:
					auxA=Pop(&manejoDatos);
					a=auxA.num;
					auxB=Pop(&manejoDatos);
					b=auxB.num;
					if(auxtop.c=='+')
					{
						auxAlmacenarRes.num=Sumar(a,b);
						Push(&manejoDatos,auxAlmacenarRes);
					}
					if(auxtop.c=='-')
					{
						auxAlmacenarRes.num=Restar(a,b,&manejoDatos);
						Push(&manejoDatos,auxAlmacenarRes);
					}
					if(auxtop.c=='*')
					{
						auxAlmacenarRes.num=Multiplicar(a,b);
						Push(&manejoDatos,auxAlmacenarRes);
					}
					if(auxtop.c=='/')
					{
						auxAlmacenarRes.num=Dividir(a,b,&manejoDatos);
						Push(&manejoDatos,auxAlmacenarRes);
					}
					if(auxtop.c=='^')
					{
						auxAlmacenarRes.num=Potenciar(a,b,&manejoDatos);
						Push(&manejoDatos,auxAlmacenarRes);
					}

				}
				else //Aquí entran sólo números
					{
						Push(&manejoDatos,auxtop);
					}
	}
	auxres=Pop(&manejoDatos);
	return auxres.num;
}
/*
Las siguientes son las subrutinas de la funci�n 'RealizarOperacion()'
Reciben los valores de la pila 'manejoDatos',
cabe destacar que los valores de Restar, Dividir, y Potenciar, cambia debido a que estas operaciones no son Conmutativas,
por ende, se eval�a primero una condici�n para saber qu� variable se restar�/dividir�/potenciar� con cual.
*/
float Sumar(float a ,float b)
{
	float res;
	res=a+b;
	return res;
}
float Restar(float a ,float b,pila *manejoDatos)
{
	float res;
	if(SizeStack(manejoDatos)==2)
	{
		res=b-a;
	}
	else
	{
		res=a-b;
	}
	return res;
}
float Multiplicar(float a ,float b)
{
	float res;
	res=a*b;
	return res;
 }
float Dividir(float a ,float b,pila *manejoDatos)
{
	float res;
	if(SizeStack(manejoDatos)==2)
	{
		res=b/a;
	}
	else
	{
		res=a/b;
	}
	return res;
}
float Potenciar(float a ,float b,pila *manejoDatos)
{
	float res;
	if(SizeStack(manejoDatos)==2)
	{
		res=pow(a,b);
	}
	else
	{
		res=pow(b,a);
	}
	return res;
}
