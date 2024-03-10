library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Unidad_Control is
    Port ( funCode, banderas : in  STD_LOGIC_VECTOR (3 downto 0);
           opCode : in  STD_LOGIC_VECTOR (4 downto 0);
           clk, clr, LF: in  STD_LOGIC;
           Microinstruccion : out  STD_LOGIC_VECTOR (19 downto 0);
		   LVL: OUT STD_LOGIC);
end Unidad_Control;

architecture Behavioral of Unidad_Control is

component Carta_ASM is
    Port ( TIPOR, BEQ, BNEQ, BLT, BLE, BGT, BGET, NA : in  STD_LOGIC;
           EQ, NEQ, LT, LE, GTI, GET : in  STD_LOGIC;
           clk, clr : in  STD_LOGIC;
           SDOPC, SM : out  STD_LOGIC);
end component;
	
component MfunCode is
    Port ( funCode : in  STD_LOGIC_VECTOR (3 downto 0);
           salidaD : out  STD_LOGIC_VECTOR (19 downto 0));
end component;
    
component MopCode is
    Port ( opCode : in  STD_LOGIC_VECTOR (4 downto 0);
           salidaD : out  STD_LOGIC_VECTOR (19 downto 0));
end component;
    
component Mux_SODPC is
    Port ( opCode : in  STD_LOGIC_VECTOR (4 downto 0);
           SDOPC : in  STD_LOGIC;
           salida : out  STD_LOGIC_VECTOR (4 downto 0));
end component;

component Mux_SM is
    Port ( MfunCode, MopCode : in  STD_LOGIC_VECTOR (19 downto 0);
           SM : in  STD_LOGIC;
           Microinstruccion : out  STD_LOGIC_VECTOR (19 downto 0));
end component;
    
component Decodificador_Instruccion is
    Port ( opCode : in  STD_LOGIC_VECTOR (4 downto 0);
           TIPOR, BEQI, BNEQI, BLTI, BLETI, BGTI, BGETI : out  STD_LOGIC);
end component;
    
component Nivel is
    Port ( clk, clr : in  STD_LOGIC;
           NA : out  STD_LOGIC);
end component;

component Registro_Estado is
    Port ( clk, clr, LF : in  STD_LOGIC;
           banderas : in  STD_LOGIC_VECTOR (3 downto 0);
           Q : out  STD_LOGIC_VECTOR (3 downto 0));
end component;

component Condicion is
    Port ( Q : in  STD_LOGIC_VECTOR (3 downto 0);
           EQ, NEQ, LT, LE, GTI, GET : out  STD_LOGIC);
end component;

signal OpR, OpNoR: STD_LOGIC_VECTOR(19 DOWNTO 0);
signal SM_Mux: STD_LOGIC_VECTOR(4 DOWNTO 0);
signal Q: STD_LOGIC_VECTOR(3 DOWNTO 0);
signal SDOPC, NA, SM: STD_LOGIC;
signal TIPOR, BEQI, BNEQI, BLTI, BLETI,BGTI,BGETI: STD_LOGIC; 
signal EQ, NEQ, LT, LE, GTI, GET : STD_LOGIC;
begin

MFunctCode: MFunCode 
    Port map ( funCode => funCode, 
			   salidaD => OpR);
			   
MOperationCode: MOpCode
    Port map ( opCode => SM_Mux,
			   salidaD => OpNoR);
			   
MuxSM: Mux_SM 
    Port map ( MfunCode => OpR, 
			   MopCode => OpNoR,
			   SM => SM,
			   Microinstruccion => Microinstruccion);

MuxSODPC: Mux_SODPC
    Port map ( opCode => opCode,
			   SDOPC => SDOPC,
			   salida => SM_Mux);
			   
Decodificador_de_Instruccion: Decodificador_Instruccion
    Port map( opCode => opCode,
			  TIPOR => TIPOR, 
			  BEQI => BEQI, 
			  BNEQI => BNEQI, 
			  BLTI => BLTI, 
			  BLETI => BLETI, 
			  BGTI => BGTI, 
			  BGETI => BGETI);
									
Level: Nivel 
    Port map ( clk => clk, 
			   clr => clr,
			   NA => NA);
					
Registro_de_Estado: Registro_Estado    
	Port map( clk => clk, 
			  clr => clr, 
			  LF => LF,
			  banderas => banderas,
			  Q => Q);
					
Condition: Condicion 
    Port map ( Q => Q,
			   EQ => EQ, 
			   NEQ => NEQ, 
			   LT => LT, 
			   LE => LE, 
			   GTI => GTI, 
			   GET => GET);

Unidad_de_Control: Carta_ASM
    Port map ( TIPOR => TIPOR,
			   BEQ => BEQI,
			   BNEQ => BNEQI,
			   BLT => BLTI, 
			   BLE => BLETI, 
			   BGT => BGTI, 
			   BGET => BGETI,
			   NA => NA,
			   EQ => EQ, 
			   NEQ => NEQ, 
			   LT => LT, 
			   LE => LE, 
			   GTI => GTI,
			   GET => GET,
			   clk => clk, 
			   clr => clr,
			   SDOPC => SDOPC, 
			   SM => SM);
LVL <= NA;
end Behavioral;
