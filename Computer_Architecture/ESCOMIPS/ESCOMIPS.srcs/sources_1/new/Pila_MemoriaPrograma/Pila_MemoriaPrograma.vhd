library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Pila_MemoriaPrograma is
    generic ( d : integer := 25;
		      a : integer := 16;
		      s : integer := 3);
	Port( PC_in : in  STD_LOGIC_VECTOR (a-1 downto 0);
		  clk, clr, UP, DW, WPC : in  STD_LOGIC;
		  PC_out : out  STD_LOGIC_VECTOR (a-1 downto 0);
		  Inst : out  STD_LOGIC_VECTOR (d-1 downto 0));
end Pila_MemoriaPrograma;

architecture Behavioral of Pila_MemoriaPrograma is

component Pila is
    Port ( PC_in : in  STD_LOGIC_VECTOR (a-1 downto 0);
           PC_out : out  STD_LOGIC_VECTOR (a-1 downto 0);
           clk, clr, UP, DW, WPC : in  STD_LOGIC);
end component;

component MemoriaPrograma is
    Port (PC : in STD_LOGIC_VECTOR (9 downto 0);
          Inst : out STD_LOGIC_VECTOR (d-1 downto 0));
end component;

signal PC: STD_LOGIC_VECTOR (a-1 downto 0);

begin

    Stack: pila 
    Port map( PC_in => PC_in, 
              clk => clk, 
              clr => clr, 
              UP => UP, 
              DW => DW, 
              WPC => WPC,
              PC_out => PC);
		   
    Memory: MemoriaPrograma
    Port map( PC => PC(9 downto 0),--el segundo PC es la señal :v
              Inst => Inst);
	          
	PC_out <= PC;

end Behavioral;
