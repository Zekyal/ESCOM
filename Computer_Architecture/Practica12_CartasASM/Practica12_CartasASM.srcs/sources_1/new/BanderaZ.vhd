library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity BanderaZ is
    Port ( Cz : in  STD_LOGIC_VECTOR (8 downto 0);
           z : out  STD_LOGIC);
end BanderaZ;

Architecture Behavioral of BanderaZ is
begin
	z <= NOT(Cz(8) OR Cz(7) OR Cz(6) OR Cz(5) OR Cz(4) OR Cz(3) OR Cz(2) OR Cz(1) OR Cz(0));	
end Behavioral;