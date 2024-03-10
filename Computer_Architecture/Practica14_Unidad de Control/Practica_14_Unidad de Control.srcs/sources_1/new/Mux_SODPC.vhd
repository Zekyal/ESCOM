library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Mux_SODPC is
    Port ( opCode : in  STD_LOGIC_VECTOR (4 downto 0);
           SDOPC : in  STD_LOGIC;
           salida : out  STD_LOGIC_VECTOR (4 downto 0));
end Mux_SODPC;

architecture Behavioral of Mux_SODPC is
begin
	salida <= opCode when SDOPC = '1' else "00000";
end Behavioral;