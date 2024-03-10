library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Registro_Estado is
    Port ( clk, clr, LF : in  STD_LOGIC;
           banderas : in  STD_LOGIC_VECTOR (3 downto 0);
           Q : out  STD_LOGIC_VECTOR (3 downto 0));
end Registro_Estado;

architecture Behavioral of Registro_Estado is
begin
	process(clk, clr) begin
		if clr = '1' then
			Q <= "0000";
		elsif (clk'event and clk='0') then
			if LF = '1' then
				Q <= banderas;
			end if;
		end if;
	end process;
end Behavioral;