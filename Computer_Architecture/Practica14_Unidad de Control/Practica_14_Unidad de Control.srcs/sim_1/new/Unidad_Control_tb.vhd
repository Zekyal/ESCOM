library IEEE;
LIBRARY STD;
use STD.TEXTIO.ALL;
use IEEE.STD_LOGIC_TEXTIO.ALL;  --PERMITE USAR STD_LOGIC 
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;

entity Unidad_Control_tb is
end Unidad_Control_tb;

architecture Behavioral of Unidad_Control_tb is

component Unidad_Control is
    Port ( funCode, banderas : in  STD_LOGIC_VECTOR (3 downto 0);
           opCode : in  STD_LOGIC_VECTOR (4 downto 0);
           clk, clr, LF: in  STD_LOGIC;
           Microinstruccion : out  STD_LOGIC_VECTOR (19 downto 0);
		   LVL: OUT STD_LOGIC);
end component;

--Inputs
signal funCode : std_logic_vector(3 downto 0) := (others => '0');
signal banderas : std_logic_vector(3 downto 0) := (others => '0');
signal opCode : std_logic_vector(4 downto 0) := (others => '0');
signal clk : std_logic := '0';
signal clr : std_logic := '0';
signal LF : std_logic := '0';

--Outputs
signal Microinstruccion : std_logic_vector(19 downto 0);
signal LVL: STD_LOGIC;

-- Clock period definitions
constant CLK_period : time := 10 ns;

begin
    -- Instantiate the Unit Under Test (UUT)
    uut: Unidad_Control
        Port Map ( funCode => funCode,
                   banderas => banderas,
                   opCode => opCode,
                   clk => clk,
                   clr => clr,
                   LF => LF,
                   Microinstruccion => Microinstruccion,
                   LVL => LVL);

    -- Clock process definitions
    CLK_process :process
    begin
        CLK <= '0';
		wait for CLK_period/2;
		CLK <= '1';
		wait for CLK_period/2;
    end process;
 
    -- Stimulus process
    stim_proc: process
        file ARCH_RES : TEXT;--Archivo de resultados                                    
        variable LINEA_RES : line;--Linea de resultado
        file ARCH_VEC : TEXT;--Archivo de vectores
        variable LINEA_VEC : line;--Linea de vectores
  
        --Variables
        variable V_funCode, V_banderas: STD_LOGIC_VECTOR(3 DOWNTO 0);
        variable V_opCode: STD_LOGIC_VECTOR(4 DOWNTO 0);
        variable V_clr, V_LF, V_LVL: STD_LOGIC;
        variable V_Microinstruccion: std_logic_vector(19 downto 0);
        --Cadena
        VARIABLE CADENA : STRING(1 TO 7);
        
        begin    
            file_open(ARCH_VEC, "VECTORES.txt", READ_MODE);  
            file_open(ARCH_RES, "RESULTADO.txt", WRITE_MODE);  
            --Impresion de Cadenas 
            CADENA := "OP_CODE";
            write(LINEA_RES, CADENA, right, CADENA'LENGTH+1); --OP_CODE
            CADENA := "FUNCODE";
            write(LINEA_RES, CADENA, right, CADENA'LENGTH+1); --FUNC_CODE
            CADENA := "  FLAGS";
            write(LINEA_RES, CADENA, right, CADENA'LENGTH+1); --BANDERAS
            CADENA := "    CLR";
            write(LINEA_RES, CADENA, right, CADENA'LENGTH+1); --CLR
            CADENA := "     LF";
            write(LINEA_RES, CADENA, right, CADENA'LENGTH+1); --LF
            CADENA := "MICROIN";
            write(LINEA_RES, CADENA, right, CADENA'LENGTH+14); --MICROINSTRUCCION
            CADENA := "  NIVEL";
            write(LINEA_RES, CADENA, right, CADENA'LENGTH+1); --NIVEL
            writeline(ARCH_RES,LINEA_RES);--Escribe la linea en el archivo
            
            --Impresion de Resultados
            wait for 100 ns;
            
            for j in 0 to 46 loop
                --Lectura de VECTORES.TXT
                readline(ARCH_VEC,LINEA_VEC); -- lee una linea completa
                read(LINEA_VEC, V_opCode);
                opCode <= V_opCode;
                read(LINEA_VEC, V_funCode);
                funCode <= V_funCode;
                read(LINEA_VEC, V_banderas);
                banderas <= V_banderas;
                read(LINEA_VEC, v_clr);
                clr <= V_clr;
                read(LINEA_VEC, V_LF);
                LF <= V_LF;

                wait until RISING_EDGE(CLK);--Flanco de subida
                V_Microinstruccion := Microinstruccion; -- Asignacion de Salida
                V_LVL := LVL;
                --Escritura de Resultados
                write(LINEA_RES, V_opCode, right, 8);
                write(LINEA_RES, V_funCode, right, 8);
                write(LINEA_RES, V_banderas, right, 8);
                write(LINEA_RES, V_CLR, right, 8);
                write(LINEA_RES, V_LF, right, 8);
                write(LINEA_RES, V_Microinstruccion, right, 21);
            
                if(V_LVL = '1') then
                    CADENA := "   ALTO";
                    write(LINEA_RES, CADENA, right, 8);
                else
                    CADENA := "   BAJO";
                    write(LINEA_RES, CADENA, right, 8);
                end if;

                writeline(ARCH_RES,LINEA_RES);--Escribe la linea en el archivo
            end loop;
            
            file_close(ARCH_VEC);--Cierra el archivo
            file_close(ARCH_RES);--Cierra el archivo
            wait;
    end process;-- Stimulus process  
end Behavioral;
