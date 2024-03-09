#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<windows.h>

int main()
{
	float a, b, c, xo, yo, zo, L, LX, LY, LZ, aproximacion;
	int nofuncion;
	char ch;//Caracter para saber si el programa se volverá a ejecutar(línea 80)
	
	do{
		system("cls");
		printf("Seleccione la funci%cn que desee linealizar y aproximar a (x0+1, y0-1, zo+1):\n\n", 162);
		printf("1. f(x, y, z) = x^a + y^b + z^c en (x0, y0, z0)\n2. f(x, y, z) = (x^a)(y^b)(z^c) en (x0, y0, z0)\n3. f(x, y, z) = ln(ax + by + cz) en (x0, y0, z0)");
		scanf("%d", &nofuncion);
	
		if(nofuncion<=3 && nofuncion>0)//Solo accesa si se seleccionan alguna de las 3 opciones
		{
			printf("\na= "); scanf("%f", &a);
			printf("b= "); scanf("%f", &b);
			printf("c= "); scanf("%f", &c);
			printf("x0= "); scanf("%f", &xo);
			printf("y0= "); scanf("%f", &yo);
			printf("z0= "); scanf("%f", &zo);
		}
		
		switch(nofuncion)
		{
			case 1://Función 1
				system("cls");
				L=(1-a)*(pow(xo, a)+pow(yo, b)+pow(zo,c));
				LX= a*pow(xo, (a-1));
				LY= b*pow(yo, (b-1));
				LZ= c*pow(zo, (c-1));
				printf("Linealizaci%cn de f(x, y, z) = x^a + y^b + z^c en (%.3f, %.3f, %.3f) y aproximaci%cn en (%.3f, %.3f, %.3f)", 162, xo, yo, zo, 162, (xo+1), (yo-1), (zo+1));
				break;
				
			case 2://Función 1
				system("cls");
				L=pow(xo,a)*pow(yo ,b)*pow(zo, c)*(1-a-b-c);
				LX= a*pow(xo, (a-1))*pow(yo, b)*pow(zo,c);
				LY= b*pow(xo, a)*pow(yo, (b-1))*pow(zo,c);
				LZ= c*pow(xo, a)*pow(yo, b)*pow(zo, (c-1));
				printf("Linealizaci%cn de f(x, y, z) = (x^a)(y^b)(z^c) en (%.3f, %.3f, %.3f) y aproximaci%cn en (%.3f, %.3f, %.3f)", 162, xo, yo, zo, 162, (xo+1), (yo-1), (zo+1));
				break;
				
			case 3://Función 1
				system("cls");
				
				if((a*xo+b*yo+c*zo)<=0)
				{
					printf("\nERROR DE SINTAXIS");
				}
				else
				{
					L=log(a*xo+b*yo+c*zo)-1;
					LX=a/(a*xo+b*yo+c*zo);
					LY=b/(a*xo+b*yo+c*zo);
					LZ=c/(a*xo+b*yo+c*zo);
				}
				
				printf("Linealizaci%cn de f(x, y, z) = ln(ax + by + cz) en (%.3f, %.3f, %.3f) y aproximaci%cn en (%.3f, %.3f, %.3f)", 162, xo, yo, zo, 162, (xo+1), (yo-1), (zo+1));
				break;
				
			default:
				printf("\nComando no v%clido", 160);
		}
		
		if(nofuncion<=3 && nofuncion>0)//Solo accesa si se seleccionan alguna de las 3 opciones
		{
			printf("\n\nL(x, y, z) = %.3fx + %.3fy + %.3fz + %.3f", LX, LY, LZ, L);
			aproximacion=L+LX*(xo+1)+LY*(yo-1)+LZ*(zo+1);
			printf("\nL(%.3f, %.3f, %.3f) = %f", (xo+1), (yo-1), (zo+1), aproximacion);
		}
		
		printf("\n\n%cDesea continuar? (S/N): ", 168);
		scanf(" %c", &ch);
		
	}while(ch=='S' || ch=='s');
	
	return 0;
}
