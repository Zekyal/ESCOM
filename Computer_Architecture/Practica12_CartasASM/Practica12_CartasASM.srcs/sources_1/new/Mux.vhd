library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Mux is
    Port ( deco : in  STD_LOGIC_VECTOR (6 downto 0);
		   OP: in STD_LOGIC;
		   Q : out  STD_LOGIC_VECTOR (6 downto 0));
end Mux;

Architecture Behavioral of Mux is
begin
    Q <= deco when OP = '1' else "1111110";--guion "-"
end Behavioral;