library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Nivel is
    Port ( clk, clr : in  STD_LOGIC;
           NA : out  STD_LOGIC);
end Nivel;

architecture Behavioral of nivel is
	signal A: std_logic := '0';
	signal B: std_logic := '0';
begin
	process (clk) begin
		if (clk'event and clk = '1') then --rising_edge(clk)
			A <= NOT A;
		end if;
		if (clk'event and clk = '0') then --falling_edge(clk)
			B <= NOT B;
		end if;
	end process;
	
	NA <= '0' when clr='1' else (A XOR B);
end Behavioral;