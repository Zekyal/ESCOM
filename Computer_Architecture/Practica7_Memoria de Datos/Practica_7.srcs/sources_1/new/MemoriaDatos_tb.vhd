library IEEE;
LIBRARY STD;
USE STD.TEXTIO.ALL;
USE IEEE.std_logic_TEXTIO.ALL;	--PERMITE USAR STD_LOGIC 
USE IEEE.std_logic_1164.ALL;
USE IEEE.std_logic_UNSIGNED.ALL;
USE IEEE.std_logic_ARITH.ALL;

entity MemoriaDatos_tb is
end MemoriaDatos_tb;

architecture Behavioral of MemoriaDatos_tb is

    component MemoriaDatos is
        Port (dataIn: in  STD_LOGIC_VECTOR (15 downto 0);
              add : in  STD_LOGIC_VECTOR (15 downto 0);
              clk, WD : in  STD_LOGIC;
              dataOut : out  STD_LOGIC_VECTOR (15 downto 0));
    end component;
    
    --Inputs
   signal dataIn : std_logic_vector(15 downto 0) := (others => '0');
   signal add : std_logic_vector(15 downto 0) := (others => '0');
   signal clk : std_logic := '0';
   signal WD : std_logic := '0';
 	--Outputs
   signal dataOut : std_logic_vector(15 downto 0);
   -- Clock period definitions
   constant clk_period : time := 10 ns;

    begin
        uut: MemoriaDatos Port Map(
          dataIn => dataIn,
          add => add,
          clk => clk,
          wd => wd,
          dataOut => dataOut);

        -- Clock process definitions
        clk_process :process
        begin
		  clk <= '0';
		  wait for clk_period/2;
		  clk <= '1';
		  wait for clk_period/2;
        end process;
    
        -- Stimulus process
        stim_proc: process
	       file ARCH_RES : TEXT;--Archivo de resultados																		
	       variable LINEA_RES : line;--Linea de resultado
	       file ARCH_VEC : TEXT;--Archivo de vectores
	       variable LINEA_VEC : line;--Linea de vectores
	
	       --Variables
	       variable V_DATAIN, V_ADD, V_DATAOUT: STD_LOGIC_VECTOR(15 DOWNTO 0);
	       variable V_WD: STD_LOGIC;
	       --Cadena
	       variable CADENA : STRING(1 TO 4);

           begin		
		      file_open(ARCH_VEC, "VECTORES.txt", READ_MODE); 	
		      file_open(ARCH_RES, "RESULTADO.txt", WRITE_MODE); 	
		      
              --Impresión de Encabezado	
		      CADENA := " ADD";
		      write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);	--"ADD"
		      CADENA := " DIN";
		      write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);	--"DATAIN"
		      CADENA := "  WD";
		      write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);	--"WRITE DATA"
		      CADENA := "DOUT";
		      write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);	--"DATAOUT"
		      writeline(ARCH_RES,LINEA_RES);--Escribe la linea en el archivo
	
	          --Impresión de Resultados
		      wait for 100 ns;
		      for i in 0 to 11 loop
	          
	          --lectura de VECTORES.TXT--
			  readline(ARCH_VEC,LINEA_VEC);--Lee una linea completa
			  Hread(LINEA_VEC, V_ADD);
			  ADD <= V_ADD;
			  Hread(LINEA_VEC, V_DATAIN);  
			  DATAIN <= V_DATAIN;
			  read(LINEA_VEC, V_WD);
			  WD <= V_WD;
			  
			  wait until RISING_EDGE(CLK);--Espera al Flanco de Subida 
			  V_DATAOUT := DATAOUT;--Asignación de salidas
			
			  --Escritura de Resultados
			  Hwrite(LINEA_RES, V_ADD, right, 5);
			  Hwrite(LINEA_RES, V_DATAIN, right, 5);
			  write(LINEA_RES, V_WD, right, 5);
			  Hwrite(LINEA_RES, V_DATAOUT, right, 5);
			  writeline(ARCH_RES,LINEA_RES);--Escribe la linea en el archivo
		  end loop;
		  
		  file_close(ARCH_VEC);--Cierra el archivo
		  file_close(ARCH_RES);--Cierra el archivo
          wait;
    end process;--Stimulus process	
end Behavioral;
