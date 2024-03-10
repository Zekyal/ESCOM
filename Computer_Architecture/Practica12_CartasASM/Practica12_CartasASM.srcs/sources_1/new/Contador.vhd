library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_arith.ALL;
use IEEE.STD_LOGIC_unsigned.all;

entity Contador is
    Port ( clk, clr, LB, EB : in  STD_LOGIC;
           QB : out  STD_LOGIC_VECTOR (3 downto 0));
end Contador;

Architecture Behavioral of Contador is
begin
    process (clk, clr)
		variable DB : STD_LOGIC_VECTOR (3 downto 0);
	begin
        if (clr = '1') then
			DB := "0000";
		elsif (rising_edge(clk)) then
			if LB = '1' then
                DB := "0000";
			elsif EB = '1' then
				DB := DB + 1;
			end if;
		end if;
		
		QB <= DB;
	end process;
end Behavioral;