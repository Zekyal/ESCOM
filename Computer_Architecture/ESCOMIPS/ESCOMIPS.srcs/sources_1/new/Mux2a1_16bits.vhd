library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Mux2a1_16bits is
    Port ( e0, e1 : in  STD_LOGIC_VECTOR (15 downto 0);
		   condicion : in std_logic;
		   salida : out  STD_LOGIC_VECTOR (15 downto 0));
end Mux2a1_16bits;

architecture Behavioral of Mux2a1_16bits is
begin
	salida <= e1 when condicion='1' else e0;
end Behavioral;
