#include<iostream>
#include<stdlib.h>
#include<string.h>

using namespace std; 

int main()
{
	int h, min, h12;
	char c;
	
	cout<<"Conversor de notacion de 24 horas a notacion de 12 horas\n\n";
	cout<<"Insterte la hora deseada en notacion de 24 horas en el formato hh:mm (Ej: 05:00, 14:56, 02:06): \n\n";
	cin>>h>>c>>min;
	
	if(min<=59)
	{
		if(min>=0)
		{
			if(h>0)
        	{
        		if(h==24)
                {
         		    cout<<"12"<<c<<min<<" AM";
        	    }
        	    else if(h==12)
          	    {
        		    cout<<h<<c<<min<<" PM";
           	    }
          		else if(h>12)
           		{
         			if(h<24)
         			{
          				h12=h-12;
          				cout<<h12<<c<<min<<" PM";
          			}
          			else if(h>24)
              	    {
                  		cout<<"La hora no es valida";
                  	}
        		}
          		else if(h<12)
         		{
          			cout<<h<<c<<min<<" AM";
        		}
			}
     	}
	
        else if(h==0)
    	{
       		cout<<"12"<<c<<min<<" AM";
     	}
     	else
      	{
       		cout<<"La hora no es valida";
     	}
	}
	
	else 
	{
		cout<<"Los minutos no son validos";	
	}
		
    return 0;
}

