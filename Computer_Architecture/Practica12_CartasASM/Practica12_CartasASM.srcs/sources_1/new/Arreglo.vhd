library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Arreglo is
    Port ( EA, LA, clk, clr : in  STD_LOGIC;
           DA : in  STD_LOGIC_VECTOR (8 downto 0);
           QA : out  STD_LOGIC_VECTOR (8 downto 0));
end Arreglo;

Architecture Behavioral of Arreglo is
begin
	process (clr, clk) 
        variable arr : std_logic_vector(8 downto 0);
	begin
		if (clr = '1') then
            arr := (others => '0');
		elsif (rising_edge(clk)) then
            if LA = '1' then
                arr := DA;
			elsif EA = '1' then
                for i in 0 to 8 loop
                    if (i > 7) then
                        arr(i):= '0';
				    else
					   arr(i):= arr(i+1);
				    end if;
				end loop;
			end if;
		end if;
		
		QA <= arr;
	end process;
end Behavioral;