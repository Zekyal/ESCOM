library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Condicion is
    Port ( Q : in  STD_LOGIC_VECTOR (3 downto 0);
           EQ, NEQ, LT, LE, GTI, GET : out  STD_LOGIC);
end Condicion;

architecture Behavioral of Condicion is
begin
	--(0, N, Z, C) 
	EQ <= '1' when Q= "0010" else '0';--Z
	NEQ <= not Q(1);--not(Z)
	LT <= Q(2);--not(C)
	LE <=(Q(2) or Q(1));--Z + not(C)
	GTI <= not Q(2);--not(Z) and C
	GET <=((not Q(2)) or Q(1));--C
end Behavioral;