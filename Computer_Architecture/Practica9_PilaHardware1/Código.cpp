#include<iostream>
#include<stdlib.h>
#include<time.h>

using namespace std;

class Pila
{
	private:
		int SP, PCin, PCout;
		int pila[8];
		bool clr, clk, WPC, UP, DW;
	public:
		void set();
		void get();
		void operacion(int, bool, bool, bool, bool);
		void operacion();
};

void Pila::set()
{
	SP=0;
	srand (time(NULL));
	
	for(int i=0; i<8; i++)
		pila[i]= rand();	
}

void Pila::get()
{
	for(int i=0; i<8; i++)
	{
		cout<<pila[i];
		
		if(i==7)
			continue;
			
		cout<<", ";
	}
	
	cout<<"\n";
}

void Pila::operacion(int PCin, bool UP, bool DW, bool WPC, bool clr)
{
	if(clr)
	{
		for(int i=0; i<8; i++)
			pila[i]= NULL;
	}
	else
	{
		if(!WPC && !UP && !DW)//demas operaciones
			pila[SP]++;
			//SP=SP
		else if(WPC && !UP && !DW)//Saltos condicionales e incondicionales
			pila[SP]= PCin;
			//SP=SP
		else if(WPC && UP && !DW)//CALL
		{
			SP++;
			pila[SP]= PCin;
		}
		else if(!WPC && !UP && DW)//RETURN			
		{
			SP--;
			pila[SP]++;
		}	
		else
			cout<<"ERROR: Operación inválida >:c";
	}
	
	operacion();
}

void Pila::operacion()
{
	PCout= pila[SP];
	cout<< "PCout: " << PCout <<"\n";
}

int main()
{
	Pila p;
	
	p.set();
	p.get();
	p.operacion(NULL, 0, 0, 0, NULL);//1. LI R6, #87
	p.operacion(NULL, 0, 0, 0, NULL);//2. LI R8, #90
	p.operacion(34 , 0, 0, 1, NULL);//3. B 34	
	p.operacion(NULL, 0, 0, 0, NULL);//4. ADD R8, R2, R3
	p.operacion(NULL, 0, 0, 0, NULL);//5. SUB R1, R2, R3
	p.operacion(61, 1, 0, 1, NULL);//6. CALL 0x61
	p.operacion(NULL, 0, 0, 0, NULL);//7. LI R6, #87
	p.operacion(NULL, 0, 0, 0, NULL);//8. LI R8, #90
	p.operacion(100, 1, 0, 1, NULL);//9. CALL 100
	p.operacion(NULL, 0, 0, 0, NULL);//10. ADD R8, R2, R3
	p.operacion(NULL, 0, 0, 0, NULL);//11. SUB R1, R2, R3
	p.operacion(NULL, 0, 0, 0, NULL);//12. LI R6, #87
	p.operacion(NULL, 0, 1, 0, NULL);//13. RET
	p.operacion(NULL, 0, 0, 0, NULL);//14. SUB R1, R2, R3
	p.operacion(NULL, 0, 0, 0, NULL);//15. LI R6, #87
	p.operacion(NULL, 0, 1, 0, NULL);//16. RET
	p.operacion(300, 0, 0, 1, NULL);//17. B 300
	p.operacion(889, 1, 0, 1, NULL);//18. CALL 889
	p.operacion(NULL, 0, 0, 0, NULL);//19. ADD R8, R2, R3
	p.operacion(NULL, 0, 0, 0, NULL);//20. SUB R1, R2, R3
	p.operacion(NULL, 0, 0, 0, NULL);//21. LI R6, #87
	p.operacion(NULL, 0, 1, 0, NULL);//22. RET
	p.operacion(NULL, 0, 1, 0, NULL);//23. RET
	p.get();//24. get();
	
	return 0;
}
