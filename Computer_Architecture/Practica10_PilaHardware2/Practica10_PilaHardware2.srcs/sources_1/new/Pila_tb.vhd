library IEEE;
LIBRARY STD;
USE STD.TEXTIO.ALL;
use IEEE.STD_LOGIC_1164.ALL;
USE IEEE.STD_LOGIC_TEXTIO.ALL;--PERMITE USAR STD_LOGIC 
USE IEEE.STD_LOGIC_1164.ALL;
USE IEEE.STD_LOGIC_UNSIGNED.ALL;
USE IEEE.STD_LOGIC_ARITH.ALL;

entity Pila_tb is
end Pila_tb;

architecture Behavioral of Pila_tb is

component Pila 
    Port ( PC_in : in  STD_LOGIC_VECTOR (15 downto 0);
           PC_out : out  STD_LOGIC_VECTOR (15 downto 0);
           clk, clr, UP, DW, WPC : in  STD_LOGIC;
		   SP: out STD_LOGIC_VECTOR (2 downto 0));
end component;

--Inputs
signal PC_in : STD_LOGIC_VECTOR (15 downto 0) := (others => '0');
signal clk : STD_LOGIC := '0';
signal clr : STD_LOGIC := '0';
signal UP : STD_LOGIC := '0';
signal DW : STD_LOGIC := '0';
signal WPC : STD_LOGIC := '0';

--Outputs
signal PC_out : STD_LOGIC_VECTOR (15 downto 0);
signal SP: STD_LOGIC_VECTOR (2 downto 0);

-- Clock period definitions
constant clk_period : time := 10 ns;

begin

    -- Instantiate the Unit Under Test (UUT)
    uut: pila PORT MAP (
        PC_in => PC_in,
        clk => clk,
        clr => clr,
        UP => UP,
        DW => DW,
        WPC => WPC,
        PC_out => PC_out,
		SP => SP
        );

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
        file ARCH_RES : TEXT;--archivo de resultados																		
	    variable LINEA_RES : line;--linea de resultado
    	file ARCH_VEC : TEXT;--archivo de vectores
	    variable LINEA_VEC : line;--linea de vectores
	
    	--Variables
	    variable V_PC_in, V_PC_out: STD_LOGIC_VECTOR(15 DOWNTO 0);
        variable v_SP : std_logic_vector(3 downto 0);
	    variable V_clr, V_UP, V_DW, V_WPC: STD_LOGIC;
	    --Cadena
	    variable CADENA : STRING(1 TO 4);
    begin		
		file_open(ARCH_VEC, "VECTORES.txt", READ_MODE); 	
		file_open(ARCH_RES, "RESULTADO.txt", WRITE_MODE); 	
	    
	    --Impresion de Cadenas	
		CADENA := "  IN";
		write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);
		CADENA := "  UP";
		write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);
		CADENA := "  DW";
		write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);
		CADENA := " WPC";
		write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);
		CADENA := " CLR";
		write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);
		CADENA := "  SP";
		write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);
		CADENA := "  PC";
		write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);
		writeline(ARCH_RES,LINEA_RES);--Escribe la linea en el archivo
	    
	    --Impresión de Resultados
		wait for 100 ns;
		for i in 0 to 25 loop
	       --Lectura de cadenas de VECTORES.txt
		    readline(ARCH_VEC, LINEA_VEC);--Lee una linea completa
			hread(LINEA_VEC, V_PC_in);
			PC_in <= V_PC_in;
			read(LINEA_VEC, V_UP);
			UP <= V_UP;
			read(LINEA_VEC, V_DW);
			DW <= V_DW;
			read(LINEA_VEC, V_WPC);
			WPC <= V_WPC;
			read(LINEA_VEC, V_clr);
			clr <= V_clr;

			wait until RISING_EDGE(clk); 
			V_PC_out := PC_out; -- asignando salida
			V_SP := '0' & SP;
			--Escribiendo Resultados
			Hwrite(LINEA_RES, V_PC_in, right, 5);
			write(LINEA_RES, V_UP, right, 5);
			write(LINEA_RES, V_DW, right, 5);
			write(LINEA_RES, V_WPC, right, 5);
			write(LINEA_RES, V_clr, right, 5);
			Hwrite(LINEA_RES, V_SP, right, 5);
			Hwrite(LINEA_RES, V_PC_out, right, 5);
		
			writeline(ARCH_RES,LINEA_RES);--Escribe la linea en el archivo
		end loop;
		file_close(ARCH_VEC);--Cierra el archivo
		file_close(ARCH_RES);--Cierra el archivo
      wait;
   end process;--Stimulus process	

end Behavioral;