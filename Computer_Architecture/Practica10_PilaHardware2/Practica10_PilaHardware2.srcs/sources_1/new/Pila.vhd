library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_arith.ALL;--Datos con signos y sin signo, y operaciones aritmeticas
use IEEE.STD_LOGIC_unsigned.ALL;--Realizar operaciones sin signo para los ST_LOGIC_VECTOR

entity Pila is
    generic ( N: integer :=3;
              M: integer :=16);
    Port ( PC_in : in  STD_LOGIC_VECTOR (M-1 downto 0);
           PC_out : out  STD_LOGIC_VECTOR (M-1 downto 0);
           clk, clr, UP, DW, WPC : in  STD_LOGIC;
		   SP: out std_logic_vector(N-1 downto 0));
end Pila;

architecture Behavioral of Pila is

type banco is array (0 to (2**N)-1) of std_logic_vector(M-1 downto 0);
signal aux: banco;
signal SP1: integer range 0 to (2**N)-1;

begin
    process(clk, clr)
		variable SPout : integer range 0 to (2**N)-1;
	begin
		if(clr = '1')then
			SPout := 0;
			aux <= (others => (others => '0'));
		elsif(clk'event and clk = '1')then
		    if(WPC = '0' and UP = '0' and DW = '0')then--incremento
		        aux(SPout) <= aux(SPout)+1;
		    elsif(WPC = '1' and UP = '1' and DW = '0')then--CALL
				SPout := SPout + 1;
				aux(SPout) <= PC_in;
			elsif(WPC = '1' and UP = '0' and DW = '0')then--JUMP
				aux(SPout) <= PC_in;
			elsif(WPC = '0' and UP = '0' and DW = '1')then--RET
				SPout := SPout - 1;
				aux(SPout) <= aux(SPout)+1;
			end if;			
		end if;
		SP1 <= SPout;
	end process;
    
    SP <= conv_std_logic_vector(SP1, 3);
    PC_out <= aux(SP1);
    
end Behavioral;