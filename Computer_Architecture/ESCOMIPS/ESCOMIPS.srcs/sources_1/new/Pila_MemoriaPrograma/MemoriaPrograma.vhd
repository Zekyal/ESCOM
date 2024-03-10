library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_arith.ALL;
use IEEE.STD_LOGIC_unsigned.ALL;

entity MemoriaPrograma is
    generic ( d : integer := 25;
              a : integer := 10);
    Port (PC : in STD_LOGIC_VECTOR (a-1 downto 0);
          Inst : out STD_LOGIC_VECTOR (d-1 downto 0));
end MemoriaPrograma;

architecture Behavioral of MemoriaPrograma is

--INSTRUCCIONES
--Tipo I
constant LI : std_logic_vector(4 downto 0) := "00001";
constant LWI : std_logic_vector(4 downto 0) := "00010";
constant LW : std_logic_vector(4 downto 0) := "10111";
constant SWI : std_logic_vector(4 downto 0) := "00011";
constant SW : std_logic_vector(4 downto 0) := "00100";
constant ADDI : std_logic_vector(4 downto 0):= "00101";
constant SUBI : std_logic_vector(4 downto 0):= "00110";
constant ANDI: std_logic_vector(4 downto 0) := "00111";
constant ORI : std_logic_vector(4 downto 0) := "01000";
constant XORI : std_logic_vector(4 downto 0) := "01001";
constant NANDI : std_logic_vector(4 downto 0):= "01010";
constant NORI: std_logic_vector(4 downto 0) := "01011";
constant XNORI : std_logic_vector(4 downto 0):= "01100";
constant BEQI : std_logic_vector(4 downto 0):= "01101";
constant BNEI : std_logic_vector(4 downto 0):= "01110";
constant BLTI : std_logic_vector(4 downto 0):= "01111";
constant BLETI : std_logic_vector(4 downto 0):= "10000";
constant BGTI : std_logic_vector(4 downto 0):= "10001";
constant BGETI : std_logic_vector(4 downto 0):= "10010";

--Tipo R
constant TR : std_logic_vector(4 downto 0) := "00000";--Operación Tipo R
constant ADD : std_logic_vector(3 downto 0) := "0000";
constant SUB : std_logic_vector(3 downto 0) := "0001";
constant OpAND : std_logic_vector(3 downto 0) := "0010";
constant OpOR : std_logic_vector(3 downto 0) := "0011";
constant OpXOR : std_logic_vector(3 downto 0) := "0100";
constant OpNAND: std_logic_vector(3 downto 0) := "0101";
constant OpNOR : std_logic_vector(3 downto 0) := "0110";
constant OpXNOR : std_logic_vector(3 downto 0) := "0111";
constant OpNOT : std_logic_vector(3 downto 0) := "1000";
constant OpSLL : std_logic_vector(3 downto 0) := "1001";
constant OpSRL : std_logic_vector(3 downto 0) := "1010";
 
--Tipo J
constant B: std_logic_vector(4 downto 0):= "10011";
constant CALL : std_logic_vector(4 downto 0):= "10100";

--Otros
constant RET : std_logic_vector(4 downto 0):= "10101";
constant NOP : std_logic_vector(4 downto 0):= "10110";

--Sin Uso
constant SU : std_logic_vector(3 downto 0) := "0000";--Sin Uso
 
--REGISTROS
constant R0 : std_logic_vector(3 downto 0) := "0000";
constant R1 : std_logic_vector(3 downto 0) := "0001";
constant R2 : std_logic_vector(3 downto 0) := "0010";
constant R3 : std_logic_vector(3 downto 0) := "0011";
constant R4 : std_logic_vector(3 downto 0) := "0100";
constant R5 : std_logic_vector(3 downto 0) := "0101";
constant R6 : std_logic_vector(3 downto 0) := "0110";
constant R7 : std_logic_vector(3 downto 0) := "0111";
constant R8 : std_logic_vector(3 downto 0) := "1000";
constant R9 : std_logic_vector(3 downto 0) := "1001";
constant R10 : std_logic_vector(3 downto 0) := "1010";
constant R11 : std_logic_vector(3 downto 0) := "1011";
constant R12 : std_logic_vector(3 downto 0) := "1100";
constant R13 : std_logic_vector(3 downto 0) := "1101";
constant R14 : std_logic_vector(3 downto 0) := "1110";
constant R15 : std_logic_vector(3 downto 0) := "1111";
 
--COMANDOS :0
type banco is array (0 to (2**a)-1) of std_logic_vector(d-1 downto 0);
constant memProg : banco := (
--SUMA
--LI & R0 & x"0001", 			  --0. LI R0, #1
--LI & R1 & x"0007", 			  --1. LI R1, #7
--TR & R1 & R1 & R0 & SU & ADD, --2. SUMA: ADD R1, R1, R0
--SWI & R1 & x"0005", 		  --3. SWI R1, 5
--B & SU & x"0002", 			  --4. B CICLO

----FIBONACCI 15 ELEMENTOS
--LI & R0 & x"0000",				--0.  LI R0, #0
--LI & R1 & x"0001", 			--1.  LI R1, #1
--LI & R2 & x"0000",				--2.  LI R2, #0
--LI & R3 & x"000f",				--3.  LI R3, #15
--TR & R4 & R1 & R0 & SU & ADD,		--4.  SUMA: ADD R4, R1, R0
--ADDI & R0 & R1 & x"000",		--5.  ADDI R0 R1 0
--ADDI & R1 & R4 & x"000",		--6.  ADDI R1 R4 0
--ADDI & R2 & R2 & x"001",		--7.  ADDI R2 R2 1
--SWI & R1 & x"0026",			--8.  SWI R1, 26
--BNEI & R2 & R3 & x"ffb",		--9.  BNEI R2 R3
--NOP & SU & SU & SU & SU & SU,		--10. NOP
--B &SU & x"000a",			--11. B NOP

--ARREGLO DE IMPAREA INICIANDO DESDE 5 DE TAMAÑO 15
--LI&R0&x"0000", 			--0.  LI R0 #0
--LI&R1&x"0005", 			--1.  LI R1 #5
--LI&R2&x"000f", 			--2.  LI R2 #15
--SW&R1&R0&X"042", 			--3.  AQUI: SW R1 R0 42
--ADDI&R0&R0&X"001",		--4.  ADDI R0 R0 1
--ADDI&R1&R1&X"002",		--5.  ADDI R1 R1 2
--BLTI&R2&R0&X"ffd",   	--6.  BLTI R2, R0, -3 (1111 1111 1101) 
--NOP&X"00000",				--7.  NOP
--B&SU&x"0007", 				--8.  B NOP

-------BUBBLE SORT(en orden ascendente con arreglo tamaño 40 iniciando desde 251 y descendiendo de 1 en 1)--------------------------------------------------
	call & SU & x"0004", 					--0. CALL ARREGLO -> (4)
	call & SU & x"000c", 					--1. CALL BURBUJA -> (12)
	call & SU & x"0022",					--2. CALL MOSTRAR -> (26)
	B & SU & x"0002",						--3. B MOSTRAR
	
----ARREGLO----------------------------------------------------------								
	LI & R0 & x"00FB",						--4. R0 = 251 (Numeros del arreglo)  				
	LI & R1 & x"0000",						--5. R1 = 0 (Contador localidades de memoria)
	LI & R2 & x"0028",						--6. R2 = 40 (Tamaño arreglo)
	SW & R0 & R1 & x"000",					--7. BUCLE: mem[0+R1] = R0
	ADDI& R1 & R1 & x"001",					--8. R1 = R1+1             
	SUBI & R0 & R0 & x"001",				--9. R0 = R0-1             
	BGTI& R1 & R2 &X"FFD",					--10.BGTI R2>R1 goto BUCLE(7)
	RET & SU & SU & SU & SU & SU,			--11. FIN Arreglo   
	
----OREDENAR(BURBUJA)--------------------------------------------------------
	SUBI & R1 & R2 & x"001",				--12. R1 = 40 -1 
	LI & R3 & x"0000",						--13. R3 = (0 para ascendente y 1 para descendente)
	LI & R4 & x"0000",						--14. R4 = 0 (auxiliar)
	SUBI & R5 & R4 & x"001",				--15. R5 = R4 - 1 (contador i)
	LI & R6 & x"0000",					    --16. R6 = 0 (contador j)
	LI & R9 & x"0000",					    --17. R9 = 0 (1 si hubo un cambio, si no 0)
	LW & R7 & R6 & x"000",				    --18. R7 = MEM[R6+0(j)]
	LW & R8 & R6 & x"001",		  			--19. R8 = MEM[R6+1(j+1)]
	BEQI & R4 & R3 & x"006",				--20. R3 == R4 (determinar si es ascendente o descendente, si es ascendente va a 26)
    BGETI & R8 & R7 & x"006",				--21. R7 > R8 mem[j] > mem[j+1] ? va a 27
    -------swap-----
	SW & R8 & R6 & X"000",     				--22. MEM[j(R6+0)] = R8(R8 = MEM[j+1]) 
    SW & R7 & R6 & X"001",				    --23. MEM[j+1(R6+1)] = R7(R7 = MEM[j]) 
	LI & R9 & x"0001",				        --24. R9 = 1 (hubo un cambio)
	
	B & SU & x"001B",			            --25. B a 27
	BGETI & R8 & R7 & x"FFC",               --26. R7 > R8 mem[j] > mem[j+1] ? va a 22
	-------Incremento j-----
	ADDI & R6 & R6 & X"001",				--27. R6 = R6 +1 (j++)
	BLTI & R1 & R6 & X"FF6",				--28. R6 < R1 (j<TAM-1) ? va a 18
	BEQI & R4 & R9 & x"004",				--29. R9 == R4 (determinar si hubo o no cambio, va a 32)
	-------Incremento i-----
	ADDI & R5 & R5 & X"001",				--30. R5 = R5 +1 (i++)
	SUBI & R1 & R1 & X"001",				--31. R1 = R1 -1 (TAM-1)--
	BLTI & R2 & R5 & X"FF0",				--32. R5 < R2 (i<TAM) ? va a 16
	RET & SU & SU & SU & SU & SU,			--33. FIN Burbuja
	
---MOSTRAR--------------------------------------------------------------
	LI & R0  & x"0000",						--34. R0 = 0   				
	LI & R2  & x"0028",						--35. R2 = 40 
	LW & R1 & R0 & x"000",					--36. R1 = MEM[0+R0]
	SW & R1 & R0 & x"000",				    --37. MEM[0+R0] = R1
	ADDI & R0 & R0 & x"001",				--38. R0 = R0+1        
	BGTI & R0 & R2 & X"ffd",				--39. BGTI R2>R0 ? va a 36
	RET & SU & SU & SU & SU & SU,			--40. FIN Mostrar 

-- -----BUBBLE SORT(en orden descendente con arreglo tamaño 35 iniciando desde 87 y ascendiendo de 3 en 3)
--	call & SU & x"0004", 					--0. CALL ARREGLO -> (4)
--	call & SU & x"000c", 					--1. CALL BURBUJA -> (12)
--	call & SU & x"0022",					--2. CALL MOSTRAR -> (26)
--	B & SU & x"0002",						--3. B MOSTRAR
	
------ARREGLO						
--	LI & R0 & x"0057",						--4. R0 = 87 (Numeros del arreglo)  				
--	LI & R1 & x"0000",						--5. R1 = 0 (Contador localidades de memoria)
--	LI & R2 & x"0023",						--6. R2 = 35 (Tamaño arreglo)
--	SW & R0 & R1 & x"000",					--7. BUCLE: mem[0+R1] = R0
--	ADDI& R1 & R1 & x"001",					--8. R1 = R1+1             
--	ADDI & R0 & R0 & x"003",				--9. R0 = R0+3             
--	BGTI& R1 & R2 &X"FFD",					--10.BGTI R2>R1 goto BUCLE(7)
--	RET & SU & SU & SU & SU & SU,			--11. FIN Arreglo   
	
------OREDENAR(BURBUJA)
--	SUBI & R1 & R2 & x"001",				--12. R1 = 35 -1 
--	LI & R3 & x"0001",						--13. R3 = (0 para ascendente y 1 para descendente)
--	LI & R4 & x"0000",						--14. R4 = 0 (auxiliar)
--	SUBI & R5 & R4 & x"001",				--15. R5 = R4 - 1 (contador i)
--	LI & R6 & x"0000",					    --16. R6 = 0 (contador j)
--	LI & R9 & x"0000",					    --17. R9 = 0 (1 si hubo un cambio, si no 0)
--	LW & R7 & R6 & x"000",				    --18. R7 = MEM[R6+0(j)]
--	LW & R8 & R6 & x"001",		  			--19. R8 = MEM[R6+1(j+1)]
--	BEQI & R4 & R3 & x"006",				--20. R3 == R4 (determinar si es ascendente o descendente, si es ascendente va a 26)
--    BGETI & R8 & R7 & x"006",				--21. R7 > R8 mem[j] > mem[j+1] ? va a 27
--    -------swap-----
--	SW & R8 & R6 & X"000",     				--22. MEM[j(R6+0)] = R8(R8 = MEM[j+1]) 
--    SW & R7 & R6 & X"001",				    --23. MEM[j+1(R6+1)] = R7(R7 = MEM[j]) 
--	LI & R9 & x"0001",				        --24. R9 = 1 (hubo un cambio)
	
--	B & SU & x"001B",			            --25. B a 27
--	BGETI & R8 & R7 & x"FFC",               --26. R7 > R8 mem[j] > mem[j+1] ? va a 22
--	-------Incremento j-----
--	ADDI & R6 & R6 & X"001",				--27. R6 = R6 +1 (j++)
--	BLTI & R1 & R6 & X"FF6",				--28. R6 < R1 (j<TAM-1) ? va a 18
--	BEQI & R4 & R9 & x"004",				--29. R9 == R4 (determinar si hubo o no cambio, va a 32)
--	-------Incremento i-----
--	ADDI & R5 & R5 & X"001",				--30. R5 = R5 +1 (i++)
--	SUBI & R1 & R1 & X"001",				--31. R1 = R1 -1 (TAM-1)--
--	BLTI & R2 & R5 & X"FF0",				--32. R5 < R2 (i<TAM) ? va a 16
--	RET & SU & SU & SU & SU & SU,			--33. FIN Burbuja
	
----MOSTRAR
--	LI & R0  & x"0000",						--34. R0 = 0   				
--	LI & R2  & x"0023",						--35. R2 = 35
--	LW & R1 & R0 & x"000",					--36. R1 = MEM[0+R0]
--	SW & R1 & R0 & x"000",				    --37. MEM[0+R0] = R1
--	ADDI & R0 & R0 & x"001",				--38. R0 = R0+1        
--	BGTI & R0 & R2 & X"ffd",				--39. BGTI R2>R0 ? va a 36
--	RET & SU & SU & SU & SU & SU,			--40. FIN Mostrar  
others => (others => '0'));

begin
    Inst <= memProg(conv_integer(PC));
end Behavioral;