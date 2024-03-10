library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity extDireccion is
  Port ( entrada: in  STD_LOGIC_VECTOR (11 downto 0);
         salida: out STD_LOGIC_VECTOR (15 downto 0));
end extDireccion;

architecture Behavioral of extDireccion is
begin
    salida <= "0000"&entrada;
end Behavioral;