library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Decodificador is
    Port ( QB : in  STD_LOGIC_VECTOR (3 downto 0);
           deco : out  STD_LOGIC_VECTOR(6 downto 0));
end Decodificador;

Architecture Behavioral of Decodificador is
	
    constant d0: STD_LOGIC_VECTOR :="0000001";
    constant d1: STD_LOGIC_VECTOR :="1001111";
    constant d2: STD_LOGIC_VECTOR :="0010010";
    constant d3: STD_LOGIC_VECTOR :="0000110";
    constant d4: STD_LOGIC_VECTOR :="1001100";
    constant d5: STD_LOGIC_VECTOR :="0100100";
    constant d6: STD_LOGIC_VECTOR :="0100000";
    constant d7: STD_LOGIC_VECTOR :="0001111";
    constant d8: STD_LOGIC_VECTOR :="0000000";
    constant d9: STD_LOGIC_VECTOR :="0000100";
    constant di: STD_LOGIC_VECTOR :="0110110";--ERROR
	
begin
	deco <=  d0	when QB = x"0" else
   			 d1	when QB = x"1" else
			 d2	when QB = x"2" else
			 d3	when QB = x"3" else
			 d4	when QB = x"4" else
			 d5	when QB = x"5" else
			 d6	when QB = x"6" else
			 d7	when QB = x"7" else
			 d8	when QB = x"8" else
			 d9 when QB = x"9" else
			 di; 
end Behavioral;
