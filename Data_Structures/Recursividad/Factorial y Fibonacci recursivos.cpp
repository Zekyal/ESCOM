#include<stdio.h>

unsigned long long Fibonacci(int n)
{
	if(n<=1)
	{
		return n;
	}
	else
	{
		return Fibonacci(n-1)+Fibonacci(n-2);
	}
}

unsigned long long Factorial(int n)
{
	if(n==0)
	{
		return 1;
	}
	else
	{
		return Factorial(n-1)*n;
	}
}

/* FIBONACCI NO RECURSIVO
int a=0, b=1;

for(i=2; i<=n, i++)
{
	c= a+b;
	a=b;
	b=c;
}
*/
