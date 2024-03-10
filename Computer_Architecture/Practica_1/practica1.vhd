library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
entity practica1 is
    Port ( a, b : in  STD_LOGIC_VECTOR(3 downto 0);
           cin : in  STD_LOGIC;
			  s: out std_logic_vector(3 downto 0);
           cout, cinL : out  STD_LOGIC);
end practica1;

architecture Behavioral of practica1 is
signal c: std_logic_vector(4 downto 0);
signal eb: std_logic_vector(3 downto 0);
begin

	--s(0) <= a(0) xor b(0) xor cin;
	--c(1) <= (a(0) and b(0)) or (a(0) and cin) or (b(0) and cin);
	
	--s(1) <= a(1) xor b(1) xor c(1);
	--c(2) <= (a(1) and b(1)) or (a(1) and c(1)) or (b(1) and c(1));
	
	--s(2) <= a(2) xor b(2) xor c(2);
	--c(3) <= (a(2) and b(2)) or (a(2) and c(2)) or (b(2) and c(2));
	
	--s(3) <= a(3) xor b(3) xor c(3);
	--c(4) <= (a(3) and b(3)) or (a(3) and c(3)) or (b(3) and c(3));
	cinL <= cin;
	c(0) <= cin;
	ciclo: for i in 0 to 3 generate
		s(i) <= a(i) xor eb(i) xor c(i);
		eb(i) <= b(i) xor cin;
		c(i+1) <= (a(i) and eb(i)) or (a(i) and c(i)) or (eb(i) and c(i));
	end generate;
	cout <= c(4);
	
	--for <variable> in <rango> generate
		--codigo concurrente
		--end generate;
	
end Behavioral;