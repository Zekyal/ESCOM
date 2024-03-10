library IEEE;
LIBRARY STD;
USE STD.TEXTIO.ALL;
USE IEEE.std_logic_TEXTIO.ALL;	--PERMITE USAR STD_LOGIC 
USE IEEE.std_logic_1164.ALL;
USE IEEE.std_logic_UNSIGNED.ALL;
USE IEEE.std_logic_ARITH.ALL;

entity MemoriaPrograma_tb is
end MemoriaPrograma_tb;

architecture Behavioral of MemoriaPrograma_tb is
    component MemoriaPrograma is
        Port (PC : in  STD_LOGIC_VECTOR (15 downto 0);
              Inst : out  STD_LOGIC_VECTOR (24 downto 0));
    end component;
    
    --Inputs
    signal PC : std_logic_vector(15 downto 0);
 	--Outputs
    signal Inst : std_logic_vector(24 downto 0);
    
    begin
        uut: MemoriaPrograma Port Map (
            PC => PC,
            Inst => Inst);
            
    -- Stimulus process
    stim_proc: process
	   file ARCH_RES : TEXT;--archivo de resultados																		
	   variable LINEA_RES : line;--linea de resultado
	   file ARCH_VEC : TEXT;--archivo de vectores
	   variable LINEA_VEC : line;--linea de vectores
	
	   --Variables
	   variable V_PC: STD_LOGIC_VECTOR(15 downto 0);
	   variable V_INST: STD_LOGIC_VECTOR(24 downto 0);
	   --Cadena
	   variable CADENA : string(1 to 4);

    begin		
        file_open(ARCH_VEC, "VECTORES.txt", READ_MODE); 	
		file_open(ARCH_RES, "RESULTADO.txt", WRITE_MODE); 	
	
	    --Imprension del Encabezado
		CADENA := "   A";
		write(LINEA_RES, CADENA, right, CADENA'LENGTH+4);	
		CADENA := " COD";
		write(LINEA_RES, CADENA, right, CADENA'LENGTH);
		CADENA := "19..";
		write(LINEA_RES, CADENA, right, CADENA'LENGTH);	
		CADENA := "15..";
		write(LINEA_RES, CADENA, right, CADENA'LENGTH);
		CADENA := "11..";
		write(LINEA_RES, CADENA, right, CADENA'LENGTH);	
		CADENA := "7..4";
		write(LINEA_RES, CADENA, right, CADENA'LENGTH);	
		CADENA := "3..0";
		write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);	
		writeline(ARCH_RES,LINEA_RES);--Escribe la linea en el archivo
	
	    --Imprimiendo RESULTADOS
		wait for 10 ns;
		for i in 0 to 85 loop
            readline(ARCH_VEC,LINEA_VEC);
			Hread(LINEA_VEC, V_PC);
			PC<= V_PC;
			wait for 10 ns;
			
			V_INST := Inst; -- asignando salida
			Hwrite(LINEA_RES, V_PC,  right, 5);
			--write(LINEA_RES, " ", right, 1);
			write(LINEA_RES, V_INST, right, V_INST'LENGTH+1);
			writeline(ARCH_RES,LINEA_RES);--Escribe la linea en el archivo
		end loop;

		file_close(ARCH_VEC);--Cierra el archivo
		file_close(ARCH_RES);--Cierra el archivo
      wait;
   end process;-- Stimulus process
end Behavioral;
