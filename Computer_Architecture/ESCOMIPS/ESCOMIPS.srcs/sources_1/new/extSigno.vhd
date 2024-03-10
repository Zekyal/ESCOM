library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity extSigno is
  Port ( entrada: in  STD_LOGIC_VECTOR (11 downto 0);
         salida: out STD_LOGIC_VECTOR (15 downto 0));
end extSigno;

architecture Behavioral of extSigno is

signal condicion: STD_LOGIC; 

begin
    condicion <= entrada(11);
    salida <= "0000"&entrada when condicion='0' else "1111"&entrada;
end Behavioral;