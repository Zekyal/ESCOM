library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_arith.ALL;
use IEEE.STD_LOGIC_unsigned.ALL;

entity StackPointer is
    Port ( clk, clr, UP, DW : in  STD_LOGIC;
		   SP: inout STD_LOGIC_VECTOR(2 downto 0));
end StackPointer;

architecture Behavioral of StackPointer is

begin
    process(clk, clr)
    begin
        if(clr = '1') then
            SP <= "000";
        elsif(RISING_EDGE(clk))then
            if(UP = '1')then
                SP <= SP + 1;
            elsif(DW = '1')then
                SP <= SP - 1;
            end if;
        end if;
    end process;

end Behavioral;