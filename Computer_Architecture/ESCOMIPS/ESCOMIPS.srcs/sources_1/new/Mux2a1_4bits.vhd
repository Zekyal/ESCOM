library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Mux2a1_4bits is
    Port ( 	e0, e1 : in  STD_LOGIC_VECTOR (3 downto 0);
			condicion : in  STD_LOGIC;
			salida : out  STD_LOGIC_VECTOR (3 downto 0));
end Mux2a1_4bits;

architecture Behavioral of Mux2a1_4bits is
begin
	salida <= e1 when condicion='1' else e0;
end Behavioral;