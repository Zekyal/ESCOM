library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Practica_2 is
    Port ( a, b : in STD_LOGIC_VECTOR (7 downto 0);
           cin : in STD_LOGIC;
           cout : out STD_LOGIC;
           s : out STD_LOGIC_VECTOR (7 downto 0));
end Practica_2;

architecture Behavioral of Practica_2 is
begin
    
	process(a,b)
		variable g,p: std_logic_vector(7 downto 0);
		variable c: std_logic_vector(8 downto 0);--acarreo
		variable algo: std_logic;
	begin
			c(0) := cin;
			for i in 0 to 7 loop
				g(i) := a(i) and b(i);
				p(i) := a(i) xor b(i);
				s(i) <= p(i) xor c(i);
				
				c(i+1) := g(i);
				
				algo := cin; 
				for j in 0 to i loop
					algo := algo and p(j);
				end loop;
				
				c(i+1) := c(i+1) or algo; 
				
				for k in 0 to i-1 loop
					algo := p(k+1); 
					for l in k+1 to i loop
						algo :=  algo and g(k) and p(l);
					end loop;	
					c(i+1) := c(i+1) or algo;
				end loop;

			end loop;
			cout <= c(7);
	end process;
	
--	process(a, b, cin)
--    variable P,G: std_logic_vector(7 downto 0);
--    variable c: std_logic_vector(8 downto 0);
--    variable auxa, auxb, auxc, auxd: std_logic;
--    begin
--        c(0) := cin;
--        for i in 0 to 7 loop
--            P(i) := a(i) xor b(i);
--            G(i) := a(i) and b(i);
--            s(i) <= P(i) xor c(i);
--            auxc := '1';
--            --c(i+1) <= g(i) or c(i) and p(i);--no es el carreo anticipado
            
--            for j in 0 to i loop
--                auxc := auxc and P(j);
--            end loop;
            
--            auxa := auxc and c(0);
            
--            for k in 0 to i-1 loop
--                auxb := '1';
                
--                for m in k+1 to i loop
--                    auxb := auxb and P(m);
--                end loop;
                
--                auxd := auxd or (G(k) and auxb);
--            end loop;
            
--            c(i+1) := G(i) or auxa or auxb;
--        end loop;
--    end process;
    
end Behavioral;
