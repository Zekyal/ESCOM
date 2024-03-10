library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_arith.ALL;--Datos con signos y sin signo, y operaciones aritmeticas
use IEEE.STD_LOGIC_unsigned.ALL;--Realizar operaciones sin signo para los ST_LOGIC_VECTOR

entity Pila is
    generic ( N: integer :=3;
              M: integer :=16);
    Port ( PC_in : in  STD_LOGIC_VECTOR (M-1 downto 0);
           PC_out : out  STD_LOGIC_VECTOR (M-1 downto 0);
           clk, clr, UP, DW, WPC : in  STD_LOGIC);
end Pila;

architecture Behavioral of Pila is

type vectores is array (0 to 7) of std_logic_vector(M-1 downto 0);

begin
	pila: process(clk, clr)
		variable sp : std_logic_vector(N-1 downto 0);
		variable pcaux : vectores;
	begin
		if(clr = '1')then
			sp := "000";
			pcaux := (others => (others => '0'));
		elsif(rising_edge(clk))then
			if( wpc = '1' and up = '0' and dw = '0' )then -- jmp 
				pcaux(conv_integer(sp)) := pc_in;
			elsif( wpc= '1' and up = '1' and dw = '0' )then	-- call
				sp := sp + 1;
				pcaux(conv_integer(sp)) := pc_in;
			elsif( wpc = '0' and up = '0' and dw = '1' )then -- ret
				sp := sp - 1;
				pcaux(conv_integer(sp)) := pcaux(conv_integer(sp)) + 1;
			elsif( wpc = '0' and up = '0' and dw = '0' )then -- inc
				pcaux(conv_integer(sp)) := pcaux(conv_integer(sp)) + 1;
			end if;			
		end if;
		pc_out <= pcaux(conv_integer(sp));
	end process;
end Behavioral;