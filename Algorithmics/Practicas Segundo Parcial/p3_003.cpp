#include<iostream>

using namespace std;

int main()
{
	int cont1=32, cont2=123;
	cout<<" Tabla de caracteres ASCII\n\n";
	cout<<(char)201<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205
	<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)187<<"\n";

	for(int i=32; i<97; i++)
	{
		cout<<(char)186<<"  C"<<(char)162<<"digo "<<cont1<<"  <------> "<<char(i)<<"  "<<(char)186<<"\n";
		cont1++;
	}
	
	for(int j=123; j<165; j++)
	{
		cout<<(char)186<<"  C"<<(char)162<<"digo "<<cont2<<" <------> "<<char(j)<<"  "<<(char)186<<"\n";
		cont2++;
	}
	
	cout<<(char)200<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205
	<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)205<<(char)188<<"\n";
	cout<<"*No incluye las min"<<(char)163<<"sculas (rango del 97 al 122)";
}
