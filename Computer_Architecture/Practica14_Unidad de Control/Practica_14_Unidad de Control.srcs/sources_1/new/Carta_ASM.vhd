library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Carta_ASM is
    Port ( TIPOR, BEQ, BNEQ, BLT, BLE, BGT, BGET, NA : in  STD_LOGIC;
           EQ, NEQ, LT, LE, GTI, GET : in  STD_LOGIC;
           clk, clr : in  STD_LOGIC;
           SDOPC, SM : out  STD_LOGIC);
end Carta_ASM;

architecture Behavioral of Carta_ASM is
begin

estados: process (clk, clr, TIPOR, BEQ, BNEQ, BLT, BLE, BGT, BGET, NA, EQ, NEQ, LT, LE, GTI, GET)
    begin
        if clr = '1' then
            SDOPC <= '0';
		    SM <= '0';
        elsif rising_edge(clk) then
		    if TIPOR = '1' then
                SDOPC <= '0';
				SM <= '0';
			else
                if BEQ = '1' then --BEQ
			        if NA = '1' then --VERIFICACION
						SDOPC <= '0';
						SM <= '1';
				elsif EQ = '1' then --SALTO
						SDOPC <= '1';
						SM <= '1';
				else
						SDOPC <= '0';
						SM <= '1';
			    end if;
			elsif BNEQ = '1' then--BNEQ
				if NA = '1' then --VERIFICACION
					SDOPC <= '0';
					SM <= '1';
				elsif NEQ = '1' THEN --SALTO
					SDOPC <= '1';
					SM <= '1';
				else 
					SDOPC <= '0';
					SM <= '1';
				end if;
			elsif BLT = '1' then --BLT
				if NA = '1' then --VERIFICACION
					SDOPC <= '0';
					SM <= '1';
				elsif LT = '1' then --SALTO
					SDOPC <= '1';
					SM <= '1';
				else
					SDOPC <= '0';
					SM <= '1';
				end if;
			elsif BLE = '1' then --BLE
				if NA = '1' then --VERIFICACION
					SDOPC <= '0';
					SM <= '1';
				elsif LE = '1' then --SALTO
					SDOPC <= '1';
					SM <= '1';
				else
					SDOPC <= '0';
					SM <= '1';
				end if;
			elsif BGT = '1' then --BGT
				if NA = '1' then --VERIFICACION
					SDOPC <= '0';
					SM <= '1';
				elsif GTI = '1' then --SALTO
					SDOPC <= '1';
					SM <= '1';
				else
					SDOPC <= '0';
					SM <= '1';
				end if;
			elsif BGET = '1' then --BGET
				if NA = '1' then --VERIFICACION
					SDOPC <= '0';
					SM <= '1';
				elsif GET = '1' then --SALTO
					SDOPC <= '1';
					SM <= '1';
				else
					SDOPC <= '0';
					SM <= '1';
				end if;
			end if;
		end if;
	end if;
end process;

end Behavioral;