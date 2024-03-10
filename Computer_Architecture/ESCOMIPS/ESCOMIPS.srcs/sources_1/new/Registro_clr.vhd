library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Registro_clr is
    Port ( clk, rclr: in STD_LOGIC;
           clr: out STD_LOGIC);
end Registro_clr;

architecture Behavioral of Registro_clr is
begin
    process(clk)
    begin
        if(FALLING_EDGE(clk)) then
            clr <= rclr;
        end if;
    end process;
end Behavioral;