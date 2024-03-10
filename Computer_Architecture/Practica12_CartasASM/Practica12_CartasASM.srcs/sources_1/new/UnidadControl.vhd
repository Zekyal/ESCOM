library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity UnidadControl is
    Port ( clk, clr, INI, z, A0 : in STD_LOGIC;
           LA, LB, EA, EB, EC : out STD_LOGIC);
end UnidadControl;

Architecture Behavioral of UnidadControl is

type estados is (e0, e1, e2);
signal edo_act, edo_sig : estados;

begin

    process (clk, clr)
    begin
        if (clr ='1') then
            edo_act <= e0;
        elsif (rising_edge(clk)) then
            edo_act <= edo_sig;
        end if;
    end process;

    process (edo_act, INI, z, A0)
    begin
        LA <= '0';
        EA <= '0';
        LB <= '0';
        EB <= '0';
        EC <= '0';
        
        case edo_act is
            when e0 =>--Estado 0
                LB <= '1';
                
                if (INI = '1') then
                    edo_sig <= e1;
                else
                    LA <= '1';
                    edo_sig <= e0;
                end if;
            when e1 =>--Estado 1
                EA <= '1';
                
                if (z = '1') then
				    edo_sig <= e2; 
				else
				    if (A0 = '1') then
					   EB <= '1';
					end if;
					
					edo_sig <= e1;
				end if;
            when e2 =>--Estado 2
                EC <= '1';
				
				if (INI = '1') then
				    edo_sig <= e2;
				else
					edo_sig <= e0;
			    end if;
            end case;
        end process;
end Behavioral;