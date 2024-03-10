library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Registro is
    Port(d : in STD_LOGIC_VECTOR (15 downto 0);
         q : out STD_LOGIC_VECTOR (15 downto 0);
         clr, clk, l : in STD_LOGIC);
end Registro;

architecture Behavioral of Registro is

begin
    process(clk,clr)--proceso de componente síncrono
    begin
        if (clr ='1') then--si clr=1 todo se hace 0
            q <= (others=>'0');
        elsif rising_edge(clk) then--cuando hay un pulso de subida
            if(l='1') then
                q <= d;--el registro carga a d
            end if;
        end if;
    end process;
end Behavioral;