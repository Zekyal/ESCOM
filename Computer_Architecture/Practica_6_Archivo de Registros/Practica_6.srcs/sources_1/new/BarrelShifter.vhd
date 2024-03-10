library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity BarrelShifter is
	generic(n: integer := 3;
			t: integer := 15);
    Port ( dato : in  STD_LOGIC_VECTOR (t downto 0);
           shift : in  STD_LOGIC_VECTOR (n downto 0);--bits a recorrer
           dir : in  STD_LOGIC;--direccion del corrimiento
           res : out  STD_LOGIC_VECTOR (t downto 0));--salida (despues de corrimiento)
end BarrelShifter;

architecture Behavioral of BarrelShifter is 
begin
	process(dir, shift, dato)
		variable aux: STD_LOGIC_VECTOR (t downto 0);--variable (a diferencia de la señal, son aunxiliares sin significado físico)
	begin
		aux := dato;
		--Corrimiento a la Izquierda
		if dir='1' then
			for i in 0 to n loop--recorrido de los 3 niveles del shift
				for j in t downto 0 loop--recorre el arreglo desde la parte mas significativa, hasta la menos significativa
					if shift(i) = '1' then
						if j<2**i then--si shift(i)=1 y j<2^i
							aux(j) := '0';--determinar hasta donde se asignan los '0' del corrimiento
						else
							aux(j) := aux(j-(2**i));
						end if;
					end if;
				end loop;
			end loop;
		--Corrimiento a la Derecha
		else
			for i in 0 to n loop
				for j in 0 to t loop--recorre el arreglo desde la parte menos significativa, hasta la mas significativa
					if shift(i) = '1' then
						if j>(t-2**i) then
							aux(j) := '0';
						else
							aux(j) := aux(j+(2**i));
						end if;
					end if;
				end loop;
			end loop;
		end if;
		
		res <= aux;
	end process;
end Behavioral;