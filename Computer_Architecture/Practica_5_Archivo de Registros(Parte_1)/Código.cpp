#include<iostream>
#include<stdlib.h>
#include<time.h>

using namespace std;

class archivoRegistros
{
	private:
		int writeData, readData1, readData2;
		char writeReg, readReg1, readReg2, shamt;
		int Banco[15];
		bool clr, clk, WR, SHE, DIR;
	public:
		void set();
		void get();
		void operacionSincrona(int, char, char, int, bool, bool, bool, bool);
		void operacionAsincrona(bool);
		void operacionAsincrona(bool, int, int);
};

void archivoRegistros::set()
{

	for(int i=0; i<16; i++)
		Banco[i]= rand()%10;	
}

void archivoRegistros::get()
{
	for(int i=0; i<16; i++)
	{
		cout<<Banco[i];
		
		if(i==15)
			continue;
			
		cout<<" ,";
	}
	
	cout<<"\n";
}

void archivoRegistros::operacionSincrona(int writeData, char writeReg, char shamt, int readReg1, bool clr, bool WR, bool SHE, bool DIR)
{
	if(clr)
		operacionAsincrona(clr);
	else
	{
		if(!WR && !SHE && !DIR){/*Banco=Banco*/}				
		else if(WR && !SHE)
			Banco[writeReg]= writeData;
		else if(WR && SHE && !DIR)
			Banco[writeReg]=Banco[readReg1]>>shamt;
		else if(WR && SHE && DIR)			
			Banco[writeReg]=Banco[readReg1]<<shamt;	
		else
			cout<<"ERROR: Operación inválida >:c";
	}
	
}

void archivoRegistros::operacionAsincrona(bool clr)
{
	for(int i=0; i<16; i++)
		Banco[i]= NULL;
}

void archivoRegistros::operacionAsincrona(bool clr, int readReg1, int readReg2)
{
	if(clr)
		operacionAsincrona(clr);
		
	readData1=Banco[readReg1];
	readData2=Banco[readReg2];
	cout<<readData1<<"\n";
	cout<<readData2<<"\n";
}

int main()
{
	archivoRegistros a;
	a.set();
	a.get();
	a.operacionSincrona(NULL, NULL, NULL, NULL, 1, 0, 0, 0);//1. Reset
	a.get();
	a.operacionSincrona(89, 1, NULL, NULL, 0, 1, 0, NULL);//2. Banco[1] =89
	a.get();
	a.operacionSincrona(72, 2, NULL, NULL, 0, 1, 0, NULL);//3. Banco[2] =72
	a.get();
	a.operacionSincrona(123, 3, NULL, NULL, 0, 1, 0, NULL);//4. Banco[3] =123
	a.get();
	a.operacionSincrona(53, 4, NULL, NULL, 0, 1, 0, NULL);//5. Banco[4] =53
	a.get();
	a.operacionAsincrona(NULL, 1, 2);//6. Leer Banco[1] y Banco[2]
	a.get();
	a.operacionAsincrona(NULL, 3, 4);//7. Leer Banco[3] y Banco[4]
	a.get();
	a.operacionSincrona(NULL, 2, 3, 1, 0, 1, 1, 1);//8. Banco[2]=Banco[1]<<3
	a.get();
	a.operacionSincrona(NULL, 4, 5, 3, 0, 1, 1, 0);//8. Banco[4]=Banco[3]<<5
	a.get();
	a.operacionAsincrona(NULL, 1, 2);//10. Leer Banco[1] y Banco[2]
	a.get();
	a.operacionAsincrona(NULL, 3, 4);//11. Leer Banco[3] y Banco[4]
	a.get();//12. Get()
	a.operacionSincrona(NULL, NULL, NULL, NULL, 1, 0, 0, 0);//13. Reset
	a.get();
	return 0;
}
