library IEEE;
LIBRARY STD;
USE STD.TEXTIO.ALL;
USE IEEE.STD_LOGIC_TEXTIO.ALL;--PERMITE USAR STD_LOGIC 
USE IEEE.STD_LOGIC_1164.ALL;
USE IEEE.STD_LOGIC_UNSIGNED.ALL;
USE IEEE.STD_LOGIC_ARITH.ALL;

entity Pila_MemoriaPrograma_tb is
end Pila_MemoriaPrograma_tb;

architecture Behavioral of Pila_MemoriaPrograma_tb is

component Pila_MemoriaPrograma is
	Port( PC_in : in  STD_LOGIC_VECTOR (15 downto 0);
		  clk, clr, UP, DW, WPC : in  STD_LOGIC;
		  PC_out : out  STD_LOGIC_VECTOR (15 downto 0);
		  Inst : out  STD_LOGIC_VECTOR (24 downto 0);
		  SP : out STD_LOGIC_VECTOR(2 downto 0));
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
signal Inst : STD_LOGIC_VECTOR (24 downto 0);
signal SP : STD_LOGIC_VECTOR(2 downto 0);

-- Clock period definitions
constant clk_period : time := 10 ns;

begin

    -- Instantiate the Unit Under Test (UUT)
    uut: Pila_MemoriaPrograma PORT MAP ( 
        PC_in => PC_in,
        clk => clk,
        clr => clr,
        UP => UP,
        DW => DW,
        WPC => WPC,
        Inst => Inst,
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
    file ARCH_RES : TEXT;--Archivo de resultados																		
	variable LINEA_RES : line;--linea de resultado
	file ARCH_VEC : TEXT;--Archivo de vectores
	variable LINEA_VEC : line;--Linea de vectores
	
	--Variables
	variable v_PC_in: STD_LOGIC_VECTOR(15 DOWNTO 0);
	variable v_SP : STD_LOGIC_VECTOR (2 downto 0);
	variable v_PC_out : std_logic_vector(15 downto 0);
	variable v_OP_CODE: STD_LOGIC_VECTOR(4 DOWNTO 0);
	variable v_Rd, v_Rt, v_Rs, v_shamt, v_FUNC_CODE: STD_LOGIC_VECTOR(3 DOWNTO 0);
	variable v_clr, v_UP, v_DW, v_WPC: STD_LOGIC;
	--Cadena
	variable CADENA : STRING(1 TO 6);
	
    begin		
        file_open(ARCH_VEC, "VECTORES.txt", READ_MODE); 	
		file_open(ARCH_RES, "RESULTADO.txt", WRITE_MODE); 	
        --Impresión de Cadenas	
		CADENA := "    SP";
		write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);
		CADENA := "    PC";
		write(LINEA_RES, CADENA, right, CADENA'LENGTH+2);
		CADENA := "OPCODE";
		write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);
		CADENA := "    Rd";
		write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);
		CADENA := "    Rt";
		write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);	
		CADENA := "    Rs";
		write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);
		CADENA := " Shamt";
		write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);
		CADENA := "F_CODE";
		write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);
		writeline(ARCH_RES,LINEA_RES);--Escribe la linea en el archivo
	    
	    --Impresion de Resultados
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

			wait until RISING_EDGE(CLK);
			
			
			--Asignación de Salidas :0
			v_SP := SP;
			v_PC_out := PC_out;
			
			v_OP_CODE(4) := Inst(24);
			v_OP_CODE(3) := Inst(23);
			v_OP_CODE(2) := Inst(22);
			v_OP_CODE(1) := Inst(21);
			v_OP_CODE(0) := Inst(20);
			
			v_Rd(3) := Inst(19);
			v_Rd(2) := Inst(18);
			v_Rd(1) := Inst(17);
			v_Rd(0) := Inst(16);
			
			v_Rt(3) := Inst(15);
			v_Rt(2) := Inst(14);
			v_Rt(1) := Inst(13);
			v_Rt(0) := Inst(12);
			
			v_Rs(3) := Inst(11);
			v_Rs(2) := Inst(10);
			v_Rs(1) := Inst(9);
			v_Rs(0) := Inst(8);
			
			v_shamt(3) := Inst(7);
			v_shamt(2) := Inst(6);
			v_shamt(1) := Inst(5);
			v_shamt(0) := Inst(4);
			
			v_FUNC_CODE(3) := Inst(3);
			v_FUNC_CODE(2) := Inst(2);
			v_FUNC_CODE(1) := Inst(1);
			v_FUNC_CODE(0) := Inst(0);
			
			--Escritura de Resultados
			Hwrite(LINEA_RES, v_SP, right, 7);
			Hwrite(LINEA_RES, v_PC_out, right, 7);
			write(LINEA_RES, v_OP_CODE, right, 7);
			write(LINEA_RES, v_Rd, right, 7);
			write(LINEA_RES, v_Rt, right, 7);
			write(LINEA_RES, v_Rs, right, 7);
			write(LINEA_RES, v_shamt, right, 7);
			write(LINEA_RES, v_FUNC_CODE, right, 7);
			
			writeline(ARCH_RES,LINEA_RES);--Escribe la linea en el archivo
		end loop;
		file_close(ARCH_VEC);--Cierra el archivo
		file_close(ARCH_RES);--Cierra el archivo
      wait;
   end process;-- Stimulus process	
   
end Behavioral;
