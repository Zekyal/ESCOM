struct operandos{
	float operando1;
	float operando2;
};

program ARITHMETIC_PRG{
	version ARITHMETIC_VER{
		float suma(operandos) = 1;
		float resta(operandos) = 2;
		float multiplicacion(operandos) = 3;
		float division(operandos) = 4;
		float exponencial(operandos) = 5;
	} = 1;
} = 0x20000001;