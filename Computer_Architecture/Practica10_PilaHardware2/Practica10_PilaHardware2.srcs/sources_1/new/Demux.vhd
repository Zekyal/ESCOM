library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Demux is
    Port ( WPC : in  STD_LOGIC;
		   SP: in STD_LOGIC_VECTOR(2 downto 0);
		   dex: out STD_LOGIC_VECTOR(7 downto 0));          
end Demux;

architecture Behavioral of Demux is

begin
    dex(0) <= WPC when SP = "000" else '0';
	dex(1) <= WPC when SP = "001" else '0';
	dex(2) <= WPC when SP = "010" else '0';
	dex(3) <= WPC when SP = "011" else '0';
	dex(4) <= WPC when SP = "100" else '0';
	dex(5) <= WPC when SP = "101" else '0';
	dex(6) <= WPC when SP = "110" else '0';
	dex(7) <= WPC when SP = "111" else '0';

end Behavioral;
