library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
LIBRARY STD;
USE STD.TEXTIO.ALL;
USE IEEE.std_logic_TEXTIO.ALL;	--PERMITE USAR STD_LOGIC 

USE IEEE.std_logic_1164.ALL;
USE IEEE.std_logic_UNSIGNED.ALL;
USE IEEE.std_logic_ARITH.ALL;

entity ArchivodeRegistros_tb is
end ArchivodeRegistros_tb;

architecture Behavioral of ArchivodeRegistros_tb is
    component ArchivodeRegistros is
        Port(readReg1, readReg2, writeReg, shamt : in  STD_LOGIC_VECTOR (3 downto 0);
             writeData : in  STD_LOGIC_VECTOR (15 downto 0);
             readData1, readData2 : inout  STD_LOGIC_VECTOR (15 downto 0);
             WR, SHE, dir, clk , clr : in  STD_LOGIC);
    end component;
    
    --Inputs
    signal readReg1 : std_logic_vector(3 downto 0) := (others => '0');
    signal readReg2 : std_logic_vector(3 downto 0) := (others => '0');
    signal writeReg : std_logic_vector(3 downto 0) := (others => '0');
    signal shamt : std_logic_vector(3 downto 0) := (others => '0');
    signal writeData : std_logic_vector(15 downto 0) := (others => '0');
    signal WR : std_logic := '0';
    signal SHE : std_logic := '0';
    signal dir : std_logic := '0';
    signal clk : std_logic := '0';
    signal clr : std_logic := '0';

	--InOuts
    signal readData1 : std_logic_vector(15 downto 0);
    signal readData2 : std_logic_vector(15 downto 0);

    -- Clock period definitions
    constant clk_period : time := 10 ns;
    
    begin
        uut: ArchivodeRegistros Port Map(
            readReg1 => readReg1,
            readReg2 => readReg2,
            writeReg => writeReg,
            shamt => shamt,
            writeData => writeData,
            readData1 => readData1,
            readData2 => readData2,
            WR => WR,
            SHE => SHE,
            dir => dir,
            clk => clk,
            clr => clr
        );

    clk_process :process
        begin
		  clk <= '0';
		  wait for clk_period/2;
		  clk <= '1';
		  wait for clk_period/2;
    end process;
			
    stim_proc: process
        file ARCH_RES : TEXT;--archivo de resultados																		
	    variable LINEA_RES : line;--linea de resultado
	    file ARCH_VEC : TEXT;--archivo de vectores
	    variable LINEA_VEC : line;--linea de vectores
	
	    --Variables
	    variable V_READREG1, V_READREG2, V_WRITEREG, V_SHAMT: STD_LOGIC_VECTOR(3 DOWNTO 0);
	    variable V_WRITEDATA, V_READDATA1, V_READDATA2: STD_LOGIC_VECTOR(15 DOWNTO 0);
	    variable V_WR, V_SHE, V_DIR, V_CLR: STD_LOGIC;
        
        --Cadena
	    VARIABLE CADENA : STRING(1 TO 4);
	
        begin		
		  file_open(ARCH_VEC, "VECTORES.txt", READ_MODE); 	
		  file_open(ARCH_RES, "RESULTADO.txt", WRITE_MODE); 	
	       
	      --ENCABEZADO
		  CADENA := " RR1";
		  write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);	
		  CADENA := " RR2";
		  write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);
		  CADENA := "SHAM";
		  write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);
		  CADENA := "WREG";
		  write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);
		  CADENA := "  WD";
		  write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);
		  CADENA := "  WR";
		  write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);
		  CADENA := " SHE";
		  write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);
		  CADENA := " DIR";
		  write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);
		  CADENA := " CLR";
		  write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);
		  CADENA := " RD1";
		  write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);
		  CADENA := " RD2";
		  write(LINEA_RES, CADENA, right, CADENA'LENGTH+1);
		  
		  writeline(ARCH_RES,LINEA_RES);-- Escribe la linea(Encabezado) en el archivo
	
	      --IMPRIMIR RESULTADOS
          wait for 100 ns;
		  for i in 0 to 11 loop
		      readline(ARCH_VEC,LINEA_VEC); -- lee una linea completa
		      --ASIGNACION DE DATPS DE ENTRADA A LOS ESTÍMULOS
			  Hread(LINEA_VEC, V_READREG1);--Lee en hexadecinales
			  readReg1 <= V_READREG1;
			  Hread(LINEA_VEC, V_READREG2);
			  readReg2 <= V_READREG2;
			  Hread(LINEA_VEC, V_SHAMT); 
			  shamt <= V_SHAMT;
			  Hread(LINEA_VEC, V_WRITEREG); 
			  writeReg <= V_WRITEREG;
			  Hread(LINEA_VEC, V_WRITEDATA);
			  writeData <= V_WRITEDATA;
			  read(LINEA_VEC, V_WR);--Lee en binario
			  WR <= V_WR;
			  read(LINEA_VEC, V_SHE);
			  SHE <= V_SHE;
			  read(LINEA_VEC, V_DIR);
			  dir <= V_DIR;
			  read(LINEA_VEC, V_CLR);
			  clr <= V_CLR;

			  WAIT UNTIL RISING_EDGE(CLK);--Espera al flanco de subida
			  --ESCRIBE EL ARCHIVO DE SALIDA
			  V_READDATA1 := readData1;
			  V_READDATA2 := readData2;
			  Hwrite(LINEA_RES, V_READREG1, right, 5);
			  Hwrite(LINEA_RES, V_READREG2, right, 5);
			  Hwrite(LINEA_RES, V_SHAMT, right, 5);
			  Hwrite(LINEA_RES, V_WRITEREG, right, 5);
			  Hwrite(LINEA_RES, V_WRITEDATA, right, 5);
			  write(LINEA_RES, V_WR, right, 5);
			  write(LINEA_RES, V_SHE, right, 5);
			  write(LINEA_RES, V_DIR, right, 5);
			  write(LINEA_RES, V_CLR, right, 5);
			  Hwrite(LINEA_RES, V_READDATA1, right, 5);
			  Hwrite(LINEA_RES, V_READDATA2, right, 5);
			  writeline(ARCH_RES,LINEA_RES);-- Escribe la linea en el archivo
		end loop;
		file_close(ARCH_VEC);--Cierra el archivo
		file_close(ARCH_RES);--Cierra el archivo
      wait;
   end process;-- Stimulus process		
end Behavioral;
