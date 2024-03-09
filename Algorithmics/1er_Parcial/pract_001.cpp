#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<math.h>

int main()
{
	int fun;
	printf("Seleccione la operaci%cn que desea realizar tecleando el n%cmero correspondiente (^^):\n\n 1. a=bc \n 2. d=(b)^2-4ac \n 3. m=(y2-y1)/(x2-x1) \n 4. i=x+y-z \n 5. j= (x+y)/(z+w) \n 6. k= 5/(1+(x)^2) \n", 162, 163);
	scanf("%d", &fun);
	switch(fun)
	{
		case 1:
			float a,b,c;
			printf("Introduzca un valor para b: ");
			scanf("%f", &b);
			printf("Introduzca un valor para c: ");
			scanf("%f", &c);
			a=b*c;
			printf("El resultado es: %.4f", a);
			break;
		case 2:
			float d,b2,a2,c2;
			printf("Introduzca un valor para b: ");
			scanf("%f", &b2);
			printf("Introduzca un valor para a: ");
			scanf("%f", &a2);
			printf("Introduzca un valor para c: ");
			scanf("%f", &c2);
			d=pow(b2,2)-(4*a2*c2);
			printf("El resultado es: %.4f", d);
			break;			
		case 3:
		    float m,y2,y1,x2,x1;
			printf("Inroduzca un valor para x1: ");
			scanf("%f", &x1);	
			printf("Inroduzca un valor para x2: ");
			scanf("%f", &x2);
			printf("Inroduzca un valor para y1: ");
			scanf("%f", &y1);
			printf("Inroduzca un valor para y2: ");
			scanf("%f", &y2);	
			m=(y2-y1)/(x2-x1+0.0);
			printf("El resultado es: %.4f", m);
			break;
		case 4:
			float i,x,y,z;
		    printf("Introduzca un valor para x: ");
			scanf("%f", &x);	
			printf("Introduzca un valor para y: ");
			scanf("%f", &y);	
			printf("Introduzca un valor para z: ");
			scanf("%f", &z);
			i=x+y-z;
			printf("El resultado es: %.4f", i);
			break;
		case 5:
			float j,x5,y5,z5,w;
			printf("Inroduzca un valor para x: ");
			scanf("%f", &x5);
			printf("Inroduzca un valor para y: ");
			scanf("%f", &y5);
			printf("Inroduzca un valor para z: ");
			scanf("%f", &z5);
			printf("Inroduzca un valor para w: ");
			scanf("%f", &w);
			j=(x5+y5)/(z5+w+0.0);
			printf("El resultado es: %.4f", j);
			break;		
		case 6:
			float k,x6;
			printf("Inroduzca un valor para x: ");
			scanf("%f", &x6);
			k=5/(1+pow(x6,2)+0.0);
			printf("El resultado es: %.4f", k);
			break;
		default:
			printf("404 not found :'v'");
	}
	return 0;
}
